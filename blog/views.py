from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Camdo
from .forms import CommentForm, CamdoForm
from django.http import HttpResponseRedirect

# Create your views here.

def post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    camdo = CamdoForm()
    if request.method == 'POST':
        camdo = CamdoForm(request.POST, author = request.user, post=post)
        if camdo.is_valid():
            camdo.save()
            return HttpResponseRedirect(request.path)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author = request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'blog/post.html', {"post":post, "camdo":camdo, "form":form})