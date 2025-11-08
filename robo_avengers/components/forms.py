from django import forms
from .models import Component

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ['name', 'description', 'quantity', 'price']  # Adjust fields as necessary
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }