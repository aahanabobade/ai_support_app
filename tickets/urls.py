from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/customer/', views.customer_register, name='customer_register'),
    path('tickets/create/', views.create_ticket, name='create_ticket'),
    path('tickets/customer/', views.customer_ticket_list, name='customer_ticket_list'),
    path('tickets/admin/', views.admin_ticket_list, name='admin_ticket_list'),
    path('tickets/detail/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('tickets/generate_ai/<int:ticket_id>/', views.generate_ai_response, name='generate_ai_response'),
    
    path('ticket/<int:ticket_id>/', views.customer_ticket_detail, name='customer_ticket_detail'),

]
