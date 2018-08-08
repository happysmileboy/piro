from django.db import models
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name='태그')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    author = models.CharField(max_length=10, verbose_name='저자')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name='코맨트')
    author = models.CharField(max_length=10, verbose_name='글쓴이')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


