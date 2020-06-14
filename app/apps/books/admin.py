from django.contrib import admin

from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price',)
    inlines = (ReviewInline,)
