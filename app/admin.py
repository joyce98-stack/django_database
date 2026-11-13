from django.contrib import admin

from app.models import Book

# Register your models here.
admin.site.site_title="Bookshop"
admin.site.site_header="Bookshop Admin"
admin.site.index_title="Books Management System"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','year','cost','category')
    search_fields = ('title','cost','category','year')
    list_filter = ('category','year')
    ordering = ('-title','year')