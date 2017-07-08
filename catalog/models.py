# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.urls import reverse 
import uuid
# Create your models here.

class Genre(models.Model):
    name=models.CharField(max_length=200, help_text="Enter a book genre.")


    def __str__(self):
        return self.name;
class Book(models.Model):
    title=models.CharField(max_length=200)

    author=models.ForeignKey('Author' ,on_delete=models.SET_NULL, null=True)

    isbn = models.CharField('ISBN', max_length=13, help_text='13 character <a href="www.facebook.com">Facebook Link</a>')

    genre=models.ManyToManyField(Genre, help_text='Select Genre')

    def genre_display(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
    
    genre_display.short_description= 'Genre'

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        #id is the default column for primary key if not specified
        return reverse('book-detail', args=[str(self.id)])
    

class BookInstance(models.Model):

    id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Universally unique ID")
    book=models.ForeignKey('Book', on_delete=models.SET_NULL,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
            ('d', 'Maintenance'),
            ('o', 'On Loan'),
            ('a', 'Available'),
            ('r', 'Reserved'),
        )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Book Availability')
        
    class Meta:
        ordering = ["due_back"]

    def __str__(self):

        return '%s (%s)' % (self.id, self.book.title)

class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
        
class SamplesSinger(models.Model):
    first_name=models.CharField('XYZ', max_length=20)

    def __str__(self):
        return self.first_name;        
    
    
