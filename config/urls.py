from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Local applications
    path("accounts/", include("accounts.urls")),
    path("", include("pages.urls")),
    path("books/", include("books.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
if settings.DEBUG:
    import debug_toolbar  # isort:skip # pragma: no cover

    urlpatterns = [  # pragma: no cover
        path("__debug__/", include(debug_toolbar.urls))
    ] + urlpatterns
"""
