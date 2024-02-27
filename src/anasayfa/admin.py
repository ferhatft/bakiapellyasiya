from django.contrib import admin

from .models import ClientopinionModel
from .resources import BookResource


from .models import Book,Category
from import_export.admin import ImportExportModelAdmin

from advanced_filters.admin import AdminAdvancedFiltersMixin
# Register your models here.

# admin.site.register(ClientopinionModel)




class BookAdmin(AdminAdvancedFiltersMixin,ImportExportModelAdmin):
    
    # readonly_fields = ('rating','created_date')

    list_display = ('name', 'author', 'author_email','imported', 'published','price')

    list_filter = ('name', 'author', 'author_email','imported', 'published','price', 'categories',)

    ordering = ('-name',)
    
    advanced_filter_fields = (
        'name', ('categories__name', 'Kategori ismi'), ('author__username', 'Yazar ismi')
       
    )
    resource_class = BookResource

admin.site.register(Book, BookAdmin)


admin.site.register(Category)