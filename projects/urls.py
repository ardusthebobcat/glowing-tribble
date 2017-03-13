from django.conf.urls import url
from . import views

#These are the project/:project_id/../../... routes only
urlpatterns = [
    url(r'^$', views.project_list, name='project_list'), #Empty route, to project list
    url(r'^projects/([0-9])/$', views.issues_list, name='issues_list'), #issues list of selected project
    url(r'^projects/([0-9])/issues/([0-9])/$', views.issues_view, name='issues_view') #specific issue view
]