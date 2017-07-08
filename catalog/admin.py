# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, SamplesSinger

# Register your models here.0
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(SamplesSinger)

class BookInline(admin.TabularInline):
	model = Book

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'date_of_birth')
	fieldsets = (
			('Name' , {
					'fields': ('first_name', 'last_name')
				}),
			('Second Name', {
					'fields': ('last_name', 'date_of_birth')
				}),
		)
	inlines = [BookInline]
admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
	model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display=('title', 'author', 'genre_display')
	inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('id', 'book' ,'due_back', 'status')
	list_filter  = ('status', 'due_back')