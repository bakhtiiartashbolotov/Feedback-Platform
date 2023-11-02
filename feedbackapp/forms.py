from django import forms
from .models import Comment, Feedback

class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']