from django.shortcuts import render, get_object_or_404, reverse
# Custom added
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Category
from .forms import CommentForm
from django.db.models import Count
from django.views.generic import TemplateView, FormView


class PostList(generic.ListView):
    model = Post
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    # Order by most liked posts
    queryset = Post.objects.filter(status=1) \
        .annotate(liked=Count('likes')) \
        .order_by('-liked')
    template_name = 'index.html'
    paginate_by = 8


class NewPostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'new_posts.html'
    paginate_by = 8


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CategoryPost(View):
    paginate_by = 8

    def get(self, request, slug, *args, **kwargs):
        # queryset = Post.objects.filter(category='teste')
        # post = get_object_or_404(queryset)

        category = get_object_or_404(Category, slug=slug)
        category_posts = Post.objects.filter(category=category)

        return render(
            request,
            "category_posts.html",
            {
                "category": category,
                "category_posts": category_posts,
            },
        )


# class SearchPost(View):
#     paginate_by = 8
#
#     def get(self, request, search, *args, **kwargs):
#         # queryset = Post.objects.filter(category='teste')
#         # post = get_object_or_404(queryset)
#
#         post_list = Post.objects.filter(content__icontains=search)
#
#         return render(
#             request,
#             "search.html",
#             {
#                 "post_list": post_list,
#                 "term": search,
#             },
#         )
class SearchPost(generic.ListView):
    model = Post
    template_name = 'search.html'
    paginate_by = 8

    # Query
    def get_queryset(self):
        # Get what came from form with name=search
        query = self.request.GET.get("search")
        # Search inside post content for provided term, insensible case
        post_list = Post.objects.filter(content__icontains=query)
        return post_list

    def get_context_data(self, **kwargs):
        # Pass what returned from get_queryset to context variable
        context = super(SearchPost, self).get_context_data(**kwargs)
        # Add what was searched to term variable inside template
        context['term'] = self.request.GET.get("search") or None
        return context

