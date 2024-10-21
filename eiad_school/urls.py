from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from pages.views import custom_404
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from blogs.sitemaps import PostSitemap, CategorySitemap
from courses.sitemaps import CourseSitemap, CategoryCourseSitemap
handler404 = custom_404

sitemaps = {
    'posts': PostSitemap,
    'categories': CategorySitemap,
    'courses': CourseSitemap,
    'courses_categories': CategoryCourseSitemap,
}

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('courses/', include('courses.urls')),
    path('programs/', include('programs.urls')),
    path('blogs/', include('blogs.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

