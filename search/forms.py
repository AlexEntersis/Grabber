from django import forms

class SearchForm(forms.Form):
    location = forms.CharField(label='location', max_length=100, required=False, widget=forms.TextInput(attrs={'id': 'location_field', 'class': "form-control", "style": "width: 150px; margin: 10px", "placeholder":"Location"}))
    skills = forms.CharField(label='skills', max_length=100, required=False, widget=forms.TextInput(attrs={'id': 'skill_field','class': "form-control", "style": "width: 150px; margin: 10px", "placeholder":"Skills"}))
    title = forms.CharField(label='title', max_length=100, required=False, widget=forms.TextInput(attrs={'id': 'title_field', 'class': "form-control", "style": "width: 150px; margin: 10px", "placeholder":"Title"}))

    #location = forms.CharField(label='Location', max_length=100)


    #title = forms.CharField(label='Title', max_length=100)
