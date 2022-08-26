from .models import Post, Category


def categories(request):
    categories = Category.objects.all()
    return {"categories": categories}
