from django import forms

class crawlForm(forms.Form):
    url = forms.URLField()
