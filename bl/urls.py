from django.conf.urls import include, url
from .views import PostView

urlpatterns = [

	url(r'^(?P<pk>\d+)/$', PostView.as_view()), # а по URL http://имя_сайта/blog/число/ 
											  # будет выводиться пост с определенным номером
]