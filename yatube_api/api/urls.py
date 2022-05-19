from rest_framework.authtoken import views
from rest_framework import routers
from django.urls import include, path

from api.views import PostsViewSet, CommentViewSet, GroupViewSet


router = routers.DefaultRouter()
router.register('posts', PostsViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
