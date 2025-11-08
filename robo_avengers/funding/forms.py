from django import forms
from .models import Funding

class FundingForm(forms.ModelForm):
    class Meta:
        model = Funding
        fields = ['title', 'amount', 'description', 'date']  # Adjust fields as necessary
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }