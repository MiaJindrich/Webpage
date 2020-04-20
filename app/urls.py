from django.conf.urls import url
from app import views

app_name = 'app'
urlpatterns = [
    url(r'^registration/$', views.register, name='registration'),
    url(r'^login/$', views.user_login, name='user_login'),
]
