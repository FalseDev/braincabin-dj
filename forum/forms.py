from django import forms
from ckeditor.widgets import CKEditorWidget

class AnswerCreationForm(forms.Form):
    text = forms.CharField(widget=CKEditorWidget())

