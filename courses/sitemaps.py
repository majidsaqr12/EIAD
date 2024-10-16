from django.contrib.sitemaps import Sitemap
from .models import Category, Course

class CategoryCourseSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return obj.get_absolute_url()


class CourseSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
        return Course.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return obj.get_absolute_url()
