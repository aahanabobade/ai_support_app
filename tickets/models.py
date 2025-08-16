from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    CATEGORY_CHOICES = [
        ('Billing', 'Billing'),
        ('Technical', 'Technical'),
        ('General', 'General'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Replied', 'Replied'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    

    # Add these fields
    response = models.TextField(blank=True, null=True)
    responder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='responses')
    ai_generated = models.BooleanField(default=False)
    ai_classified = models.BooleanField(default=False)  # new field

    def __str__(self):
        return self.subject
