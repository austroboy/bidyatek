from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/', include('core.urls')),
    path('api/', include('schools.urls')),
    path('api/', include('products.urls')),
    path('api/', include('demo.urls')),
    path('api/', include('contact.urls')),
    path('api/', include('blog.urls')),
    path('api/', include('gallery.urls')),
    path('api/', include('testimonials.urls')),
    path('api/', include('faq.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)