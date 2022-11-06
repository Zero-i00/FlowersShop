from django.core.validators import FileExtensionValidator
from django.db import models

class Flower(models.Model):
    title = models.CharField('Название', max_length=15)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='flower/', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])
    price = models.PositiveIntegerField('Цена', default=0,)
    in_stock = models.BooleanField('В наличии', default=False)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'

class Bouquet(models.Model):
    title = models.CharField('Название', max_length=15)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='bouquet/', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])
    composition = models.ManyToManyField(to=Flower, verbose_name='Состав букета', related_name='bouquet_composition')
    price = models.PositiveIntegerField('Цена', default=0)
    quantity = models.PositiveSmallIntegerField(default=0)
    in_stock = models.BooleanField('В наличии', default=False)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'

class Wrapper(models.Model):
    title = models.CharField('Название', max_length=20)
    image = models.ImageField('Изображение', upload_to='wrapper/', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])
    price = models.PositiveIntegerField('Цена', default=0)
    in_stock = models.BooleanField('В наличии', default=False)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = 'Обёртка'
        verbose_name_plural = 'Обёртки'


class Ribbon(models.Model):
    title = models.CharField('Название', max_length=20)
    material = models.CharField('Материал', max_length=20)
    image = models.ImageField('Изображение', upload_to='wrapper/', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])
    price = models.PositiveIntegerField('Цена', default=0)
    in_stock = models.BooleanField('В наличии', default=False)

    def __str__(self):
        return f'{self.title}({self.material})'

    def __repr__(self):
        return f'{self.title}({self.material})'

    class Meta:
        verbose_name = 'Лента'
        verbose_name_plural = 'Ленты'

