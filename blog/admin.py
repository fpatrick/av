from django.contrib import admin
# Eu add abaixo
from .models import Post, Comment, Category
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
    exclude = ('',)

    # Save as logged author instead of user input
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        logged_user = request.user

        qs = super().get_queryset(request)
        if logged_user.is_superuser:
            return qs
        else:
            self.exclude = ('likes', 'excerpt')
            return qs.filter(author=logged_user)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['disable_comments', 'enable_comments']

    exclude = ('',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            self.exclude = ('approved', 'post')
            return qs.filter(name=request.user)

    def disable_comments(self, request, queryset):
        queryset.update(approved=False)

    def enable_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category',)}
    list_display = ('category',)
