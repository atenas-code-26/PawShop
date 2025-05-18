from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from products.views import home_view
from accounts.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('login/', LoginView.as_view(template_name='products/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    