from django.contrib import admin

from todos_app.todos.models import Todo, Person, Category


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']
    list_filter = ['owner']


admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
admin.site.register(Category)

# Register your models here.
