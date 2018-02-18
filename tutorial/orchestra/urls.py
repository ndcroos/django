from django.conf.urls import url
from orchestra import views

urlpatterns = [
    url(r'^$/', views.index, name='index'),
]