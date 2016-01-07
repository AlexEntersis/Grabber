__author__ = 'Alex'

from django import forms

class CommentForm(forms.Form):
    text = forms.CharField(label='text', max_length=100, required=False,
                           widget=forms.TextInput(attrs={'id': 'text_field', 'class': "form-control",
                                                         "style": "width: 150px; margin: 10px",
                                                         "placeholder": "Text "})
                           )
    vacancy = forms.CharField(label='vacancy', max_length=100, required=False,
                              widget=forms.TextInput(attrs={'id': 'vacancy_field', 'class': "form-control",
                                                            "style": "width: 150px; margin: 10px",
                                                            "placeholder": "Vacancy"})
                              )

