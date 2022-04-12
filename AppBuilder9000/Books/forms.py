from django .forms import ModelForm
from .models import AddBook


class AddBookForm(ModelForm):
    class Meta:
        model = AddBook
        fields = '__all__'