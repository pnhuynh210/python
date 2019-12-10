from django import forms
from .models import Comment, Camdo

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author',None)
        self.post = kwargs.pop('post',None)
        super().__init__(*args, **kwargs)
    def save(self, commit = True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()
    class Meta:
        model = Comment
        fields = ["body"]

class CamdoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author',None)
        self.post = kwargs.pop('post',None)
        super().__init__(*args, **kwargs)
    def save(self, commit = True):
        camdo = super().save(commit=False)
        camdo.author = self.author
        camdo.post = self.post
        camdo.save()
    class Meta:
        model = Camdo
        fields = ["name","product",
        #"image"
        ]