from django import forms

class AnswerCreationForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

