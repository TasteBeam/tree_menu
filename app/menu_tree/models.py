from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField('Название' ,max_length=255)
    description = models.TextField('Описание', max_length=255, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

class MenuItem(models.Model):
    name = models.CharField('Название пункта', max_length=60, unique=True)
    description = models.TextField('Описание', max_length=255, blank=True)
    url = models.CharField("Ссылка", max_length=50, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'