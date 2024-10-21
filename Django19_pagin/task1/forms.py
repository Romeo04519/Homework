from django import forms

class ContactForm(forms.Form):
    post_number = forms.CharField(max_length=3, label='Выберете количество постов на странице')