from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}: {self.name}'

    class Meta:
        verbose_name_plural = 'categories'


class Todo(models.Model):
    text = models.CharField(max_length=30)
    state = models.BooleanField(default=False)

    description = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True,

    )

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.text}'
