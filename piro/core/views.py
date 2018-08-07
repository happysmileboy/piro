from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from .models import Article, Comment, Tag
# Create your views here.


def article_list(request):
    article_list = Article.objects.all()
    ctx = {
        'article_list': article_list,
    }
    return render(request, 'article_list.html', ctx)


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    ctx = {
        'article': article,
    }
    return render(request, 'article_detail.html', ctx)


def article_create(request):
    ctx = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            article = Article.objects.create(
                title=title,
                content=content,
            )
            url = reverse('core:article_detail', kwargs={
                'pk': article.pk,
            })
            return redirect(url)
        else:
            error_msg = {}
            if not title:
                error_msg.update({'title': '제목을 입력해주세요.'})
            if not content:
                error_msg.update({'content': '내용을 입력해주세요.'})
            ctx.update({'error': error_msg, })

    return render(request, 'article_create.html', ctx)