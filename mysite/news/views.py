from django.shortcuts import render

from .models import Article


def year_archive(request):
    a_list = Article.objects.filter(pub_date__year=2022)
    context = {'year': 2022, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)
