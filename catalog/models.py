from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name_product = models.CharField(max_length=20, verbose_name='имя')
    description = models.CharField(max_length=150, verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, **NULLABLE)
    price = models.IntegerField(verbose_name='цена', **NULLABLE)
    made = models.DateField(verbose_name='изготовлено', auto_now_add=True)
    change = models.DateField(verbose_name='изменено', auto_now=True)
    owner = models.ForeignKey(User, verbose_name='Владелец', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.pk} {self.name_product} {self.price} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ("can_edit_category", "Can edit category"),
            ("can_edit_description", "Can edit description"),
        ]


class Category(models.Model):
    name_category = models.CharField(max_length=20, verbose_name='имя')
    description = models.CharField(max_length=150, verbose_name='описание')

    def __str__(self):
        return f'{self.pk} {self.name_category}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'