from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Question

class AnswerCreationForm(forms.Form):
    text = forms.CharField(widget=CKEditorWidget())


class QuestionCreationForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Question
        fields = ['title', 'description']