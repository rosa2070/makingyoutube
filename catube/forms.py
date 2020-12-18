from django import forms
from .models import Video, Comment


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            'title',
            'description',
            'file',
            'photo',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        models = Comment
        fields = '__all__'