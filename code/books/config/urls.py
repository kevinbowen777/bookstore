from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('django.contrib.auth.urls')),

    # Local applications
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
]
