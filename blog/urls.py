from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('contact/', TemplateView.as_view(template_name="contact.html")),
    path('newest/', views.NewPostList.as_view(), name='new_posts'),
    path('search/', views.SearchPost.as_view(), name='search'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('category/<slug:slug>/', views.CategoryPost.as_view(), name='category_post'),


]