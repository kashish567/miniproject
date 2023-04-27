from django.contrib import admin
from . import Author

class AuthorAdmin(admin.ModelAdmin):
    
admin.site.register(Author, AuthorAdmin)

