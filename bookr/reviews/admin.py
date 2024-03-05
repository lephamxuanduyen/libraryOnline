
from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13', 'has_isbn')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn')
    @admin.display(boolean=True, description='Has ISBN')
    def has_isbn(self, obj):
        return bool(obj.isbn)
    @admin.display(ordering='isbn', description='ISBN-13', empty_value='-/-')
    def isbn13(self, obj):
        return '{}-{}-{}-{}-{}'.format(obj.isbn[0:3],obj.isbn[3:4],obj.isbn[4:6],obj.isbn[6:12],obj.isbn[12:13])
    
class ReviewAdmin(admin.ModelAdmin):
    # exclude = ('date_edited',)
    # fields = ('content', 'rating', 'creator', 'book')
    fieldsets = (
        (None, {"fields": ('creator', 'book')}),
        ('Review content', {"fields": ('content', 'rating')})
    )
    
class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    search_fields = ('last_names', 'first_names')
    list_filter = ('last_names',)
# Register your models here.

admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)