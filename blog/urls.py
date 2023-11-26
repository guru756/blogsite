from django.urls import path
from .views import *
urlpatterns = [
    path('home/', PostList.as_view(), name='home'),
    path('' , loginn, name="signin"),
    path('create_post/',newpost,name="create_post"),
    path('myblogs/',mypost,name="myblogs"),
    path('signup/' , signup , name="signup"),
    path('signout/' , signout , name="signout"),
    path('<slug:slug>/', PostDetail.as_view(), name="post_detail"),
]