from .models import Category, SubCategory


def menu_links(request):
    links = Category.objects.all()
    sub_links = SubCategory.objects.all()
    return dict(links=links, sub_links=sub_links)
