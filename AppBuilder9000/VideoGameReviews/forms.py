from django import forms
from .models import VideoReviews


class VideoReviewsForm(forms.ModelForm):
    class Meta:
        model = VideoReviews
        fields = ['GameName', 'GameGenre', 'GameReview', 'GameRating']
