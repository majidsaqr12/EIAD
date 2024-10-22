from django import forms

class ProgramRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nom")
    email = forms.EmailField(label="E-mail")
    phone = forms.CharField(max_length=15, label="Téléphone")
    age = forms.IntegerField(label="Âge")
    whatsapp_number = forms.CharField(max_length=15, label="Numéro WhatsApp")
