from django.contrib import admin
from .models import Post, Comment, Camdo
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment

class CamdoInline(admin.TabularInline):
    model = Camdo

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    list_filter = ['date']
    search_fields = ['title','id']
    inlines = [CamdoInline,CommentInline]
admin.site.register(Post,PostAdmin)