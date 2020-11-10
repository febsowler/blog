from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from bl import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.index, name='home'),
	path('login/', views.login_url),
	path('logout/', views.logout_url),
	path('reg/', views.reg_url),
	path('post/', include('bl.urls'))
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
						  document_root=settings.MEDIA_ROOT)