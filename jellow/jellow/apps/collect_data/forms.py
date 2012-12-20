from django import forms
from collect_data.models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
