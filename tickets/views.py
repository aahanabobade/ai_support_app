from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Ticket
from .forms import TicketForm
from django.http import JsonResponse
import os
import requests  # to make API calls
import google.generativeai as genai
from django.contrib.auth.models import User




gemini_api_key = genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def customer_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.is_staff = False  # ensure it's a customer, not admin
            user.save()
            messages.success(request, "Registration successful! You can now login.")
            return redirect('login')  # <-- redirect to the existing login page

    return render(request, 'tickets/customer_register.html', {})


# -------------------
# Login / Logout
# -------------------
def user_login(request):
    role = request.GET.get('role')  # <-- get role from URL query parameter

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role_post = request.POST.get('role')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if role_post == 'admin' and not user.is_staff:
                messages.error(request, 'You do not have admin privileges.')
            elif role_post == 'customer' and user.is_staff:
                messages.error(request, 'Staff cannot login as customer.')
            else:
                login(request, user)
                # Redirect based on role
                if role_post == 'admin':
                    return redirect('admin_ticket_list')
                else:
                    return redirect('customer_ticket_list')

        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'tickets/login.html', {'role': role})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

# -------------------
# Home page
# -------------------
def home(request):
    # Home page just shows links to Customer or Admin login
    return render(request, 'tickets/home.html')

# -------------------
# Customer Views
# -------------------
@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.customer = request.user
            ticket.ai_generated = False  # new tickets are not AI responses
            ticket.ai_classified = True

            # -------------------------
            # AI-powered ticket classification (strict prompt)
            # -------------------------
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                prompt = (
                    "You are a support ticket classifier. "
                    "Classify the following customer support ticket strictly into one category: "
                    "Billing, Technical, or General. "
                    "Do not add extra words or explanations. "
                    f"Ticket Message: {ticket.message}\n\n"
                    "Category (only choose one of Billing, Technical, General):"
                )
                response = model.generate_content(prompt)
                predicted_category = response.text.strip().title()  # normalize capitalization

                # Validate prediction
                if predicted_category not in ['Billing', 'Technical', 'General']:
                    predicted_category = 'General'  # fallback

                ticket.category = predicted_category

            except Exception as e:
                print("AI classification error:", e)
                ticket.category = 'General'  # fallback if AI fails

            ticket.save()
            return redirect('customer_ticket_list')
    else:
        form = TicketForm()
    return render(request, 'tickets/create_ticket.html', {'form': form})


@login_required
def customer_ticket_list(request):
    tickets = Ticket.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'tickets/customer_ticket_list.html', {'tickets': tickets})

# -------------------
# Admin Views
# -------------------
@staff_member_required
def admin_ticket_list(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    return render(request, 'tickets/admin_ticket_list.html', {'tickets': tickets})

@staff_member_required
def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    if request.method == 'POST' and 'submit_response' in request.POST:
        response_text = request.POST.get('response_text')
        ticket.response = response_text
        ticket.responder = request.user
        ticket.status = 'Replied'
        ticket.ai_generated = request.POST.get('ai_generated') == 'true'
        ticket.save()
        return redirect('admin_ticket_list')



    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})


@staff_member_required
def generate_ai_response(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    
    prompt = (
        f"You are a customer support agent at EduvanceAI. "
        f"Write a professional, polite, and clear response to the customer ticket below. "
        f"Do not use stars or markdown formatting. "
        f"Use proper paragraphs, numbering if needed, and maintain a formal tone.\n\n"
        f"Ticket Subject: {ticket.subject}\n"
        f"Customer Message: {ticket.message}\n\n"
        f"Response:"
    )
    
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        ai_text = response.text.strip()

        # Save AI-generated response to the ticket
        ticket.response = ai_text
        ticket.ai_generated = True
        ticket.responder = request.user
        ticket.status = 'Replied'
        ticket.save()

    except Exception as e:
        ai_text = f"Error: {str(e)}"

    return JsonResponse({"ai_response": ai_text})


@login_required
def customer_ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id, customer=request.user)
    return render(request, 'tickets/customer_ticket_detail.html', {'ticket': ticket})



'''@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.customer = request.user
            ticket.ai_generated = False  # new tickets are not AI responses
            ticket.ai_classified = True
            
            # -------------------------
            # AI-powered ticket classification
            # -------------------------
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                prompt = f"Classify the following customer support ticket into one of these categories: Billing, Technical, General.\n\nMessage: {ticket.message}\n\nCategory:"
                response = model.generate_content(prompt)
                predicted_category = response.text.strip()

                # Make sure the prediction matches one of the valid choices
                if predicted_category in ['Billing', 'Technical', 'General']:
                    ticket.category = predicted_category
                else:
                    ticket.category = 'General'  # fallback
            except Exception as e:
                print("AI classification error:", e)
                ticket.category = 'General'  # fallback if AI fails

            ticket.save()
            return redirect('customer_ticket_list')
    else:
        form = TicketForm()
    return render(request, 'tickets/create_ticket.html', {'form': form})'''
