from django.urls import path
from . import views
from .views import User_Auth

urlpatterns = [
    path("add_user/", views.add_user, name='add_user'),
    path("profile/", User_Auth.as_view(), name='home'),
    path("forgot_password/", views.user_change_pwd, name='changepwd'),
    path("contact/", views.contact, name='contact'),
    path("filters/", views.filter_user, name='filter'),
    path("logout/", views.log_out, name='logout'),
    path("userpage/", views.userpage, name='userpage'),
    path("userpage_filter/", views.userpage_filter, name='userpagefilter'),
    path("userpage_love/", views.userpage_love, name='userpagelove'),
    path("userpage_horror/", views.userpage_horror, name='userpagehorror'),
    path("userpage_comedy/", views.userpage_comedy, name='userpagecomedy'),
    path("userpage_action/", views.userpage_action, name='userpageaction'),
    path("userpage_music/", views.userpage_music, name='userpagemusic'),
    path("", views.home, name='home2'),
    path("add_video/", views.add_video, name='add_video')
]