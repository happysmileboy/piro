from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path('article_list', views.article_list, name="article_list"),
    path('article/<int:pk>', views.article_detail, name="article_detail"),
    path('article_create', views.article_create, name="article_create"),
    path('article_list_tag', views.article_list_tag, name="article_list_tag"),
    path('article_list_tag/<int:tag_pk>', views.article_list_tag, name='article_list_by_tag'),
    path('article_update/<int:pk>',views.article_update, name="article_update")
]