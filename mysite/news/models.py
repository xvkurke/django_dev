from django.db import models
from django.urls import reverse

# Create your models here.

class News(models.Model):
    
    title = models.CharField( max_length = 150 , verbose_name = 'Title' )
    content = models.TextField( blank = True, verbose_name = 'Content' )
    created_at = models.DateTimeField( auto_now_add = True, verbose_name = 'Created At' )
    updated_at = models.DateTimeField( auto_now = True, verbose_name = 'Updated At' )
    photo = models.ImageField( upload_to = 'photos/%Y/%m/%d/', blank = True, verbose_name = 'Photo')
    is_published = models.BooleanField( default = True, verbose_name = 'Is Published' )
    category = models.ForeignKey('Category', on_delete = models.PROTECT, null = True, blank = True)

    def get_absolute_url(self):
        return reverse('view_news', kwargs = {'news_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News list'
        verbose_name_plural = 'News lists'
        ordering = ['-created_at']


class Category(models.Model):

    title = models.CharField( max_length = 150, verbose_name = 'Category Title', db_index = True )

    def get_absolute_url(self):
        return reverse('category', kwargs = {'category_id': self.pk})
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']