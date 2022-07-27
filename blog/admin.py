from django.contrib import admin
# Eu add abaixo
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    # Repopulate slug field with title field
    prepopulated_fields = {'slug': ('title',)}
    # Add a box on the side to filer by
    list_filter = ('status', 'created_on')
    # List posts showing those infos on list
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


