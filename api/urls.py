from django.urls import path, include
from .views import signup, login_view, mainpage, logout_view, create_post, delete_post, profile_view, like_post, add_comment,notifications,menu_view
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('mainpage/', mainpage, name='mainpage'),
    path('create_post/', create_post, name='create_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('like_post/<int:post_id>/', like_post, name='like_post'),
    path('add_comment/<int:post_id>/', add_comment, name='add_comment'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('notifications/', notifications, name='notifications'),
    path('menu/', menu_view, name='menu'),
    
    path('', include(router.urls)),
]

