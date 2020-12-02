from django.urls import path

from paintings.views import list_painting, details_or_comment_painting, like_painting, edit_painting, delete_painting, create_painting

urlpatterns = [
    path('', list_painting, name='list paintings'),
    path('detail/<int:pk>/', details_or_comment_painting, name='painting details or comment'),
    # path('like/<int:pk>/', like_painting, name='like painting'),
    path('edit/<int:pk>/', edit_painting, name='edit painting'),
    path('delete/<int:pk>/', delete_painting, name='delete painting'),
    path('create/', create_painting, name='create painting'),
]