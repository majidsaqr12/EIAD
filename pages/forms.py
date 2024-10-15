from django import forms
from .models import Contact, Subscription

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'company', 'message']

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']