from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.project_list, name='project_list'),
    url(r'^projects/([0-9])/$', views.issues_list, name='issues_list'),
    url(r'^projects/([0-9])/issues/([0-9])/$', views.issues_view, name='issues_view')
]