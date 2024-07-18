from django.urls import path
from social_media.views import PostView, PostDetailView

urlpatterns = [
    path('post/', PostView.as_view()),
    path('post/<str:pk>/', PostDetailView.as_view()),
]