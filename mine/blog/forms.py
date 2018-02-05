from django import forms

class NewEssay(forms.Form):
    topic = forms.CharField()
    author = forms.CharField()
    content = forms.CharField()