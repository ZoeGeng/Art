from django.conf.urls import url
from art import views
app_name = 'art'

urlpatterns = [
    url(r'^show/(\d+?)/$', views.show),
    url(r'^advance/(\d+?)/$', views.advance),
    url(r'^qAdvance/(\d+?)/$',views.queryAdvance)

]

