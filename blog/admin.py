from django.contrib import admin

from .models import Artikel, Category

# Register your models here.


class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('judul', 'slug', 'author', 'published',
                    'status', 'kategori')
    list_filter = ('status', 'created', 'published', 'author', 'kategori')
    search_fields = ('judul', 'isi')
    date_hierarchy = 'published'
    ordering = ('status', 'published')


class CategoryAdmin(admin.ModelAdmin):
    ordering = ('id',)


admin.site.register(Artikel, ArtikelAdmin)
admin.site.register(Category, CategoryAdmin)
