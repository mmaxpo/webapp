from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from django.conf import settings

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("blog/", include('blog.urls')),
                  path("basket/", include('basket.urls')),
                  path('shipping/', include('shipping.urls')),
                  path('school/', include('school.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
