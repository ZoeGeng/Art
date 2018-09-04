from django.conf.urls import url
from user import views

app_name = 'user'
urlpatterns = [
    url('login/', views.login),
    url('regist/', views.regist),
    url('upload/', views.upload),
    url('logout/', views.logout),

]