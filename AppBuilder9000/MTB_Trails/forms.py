from django.forms import ModelForm
from .models import ReviewTrail

class TrailReview(ModelForm):
    class Meta:
        model = ReviewTrail
        fields = '__all__'

