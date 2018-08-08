from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.http import Http404
from .models import Article, Comment, Tag
# Create your views here.


def article_list(request):
    article_list = Article.objects.all()
    ctx = {
        'article_list': article_list,
    }
    return render(request, 'article_list.html', ctx)


def article_list_tag(request, tag_pk=None):
    if tag_pk is not None:
        article_list = Article.objects.filter(tag__pk=tag_pk)
        try:
            tag = get_object_or_404(Tag, pk=tag_pk)
        except tag.DoesNotExist:
            raise Http404('없는 tag입니다')
    else:
        article_list = Article.objects.all()
        tag = None

    ctx = {
        'article_list': article_list,
        'tag_list': Tag.objects.all(),
        'tag_selected': tag,
    }
    return render(request, 'article_list.html', ctx)


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.all()
    ctx = {
        'article': article,
        'comments': comments,
    }

    if request.method == 'POST':
        content = request.POST.get('content')
        author = request.POST.get('author')

        if content and author:
            comment = Comment.objects.create(
                article=article,
                content=content,
                author=author
            )
            url = reverse('core:article_detail', kwargs={
                'pk': article.pk
            })
            return redirect(url)

        error_msg = {}
        if not content:
            error_msg.update({'content': '제목을 입력해주세요.'})
        if not author:
            error_msg.update({'author': '내용을 입력해주세요.'})
        ctx.update({'error': error_msg, })

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