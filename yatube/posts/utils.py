from django.core.paginator import Paginator


def paginate_page(request, posts):
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj
