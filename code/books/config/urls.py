from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')),

    # Local applications
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
]
