from django.contrib import admin
from django.urls import path, include

import todos_app
import todos_app.todos.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todos_app.todos.urls'))
]
