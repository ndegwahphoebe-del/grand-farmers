# soilhealth/forms.py
from django import forms
from .models import SoilSample

class SoilSampleForm(forms.ModelForm):
    class Meta:
        model = SoilSample
        fields = ["farmer_name", "location", "ph", "organic_matter", "crop"]
        widgets = {
            "farmer_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your full name"}),
            "location": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your farm location"}),
            "ph": forms.NumberInput(attrs={"class": "form-control", "step": "0.1", "placeholder": "Soil pH (e.g. 5.8)"}),
            "organic_matter": forms.NumberInput(attrs={"class": "form-control", "step": "0.1", "placeholder": "Organic Matter %"}),
            "crop": forms.Select(attrs={"class": "form-control"}),
        }