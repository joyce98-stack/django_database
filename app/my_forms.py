from django import forms

from app.models import Book

# django forms
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields=('title','category','isbn','cost','year','published','cover')

