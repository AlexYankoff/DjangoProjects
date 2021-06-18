from django.shortcuts import render, redirect

from todos_app.todos.forms import CreateTodoForm, UpdateTodoForm, TodoForm
from todos_app.todos.models import Todo, Person


# def index(request):
#    context = {
#        'todos': Todo.objects.all(),
#        'form':CreateTodoForm()
#    }
#    return render(request, 'index.html', context)
#
#
# def create_todo(request):
#    form = CreateTodoForm(request.POST)
#
#    if form.is_valid():
#        #cleaned_data is available only after is_valid call
#        text = form.cleaned_data['text']
#        description = form.cleaned_data['description']
#        todo = Todo(
#            text=text,
#            description=description,
#            #owner=owner
#            )
#
#    todo.save()
#
#    return redirect('/')

def index(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'todo_app/index.html', context)


def create_todo(request):
    form = TodoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    # ako не е валидна формата, или не е POST заявка,  показваме я пак
    context = {
        'form': form,
    }
    return render(request, 'todo_app/create.html', context)


def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)

    #initial ще взме попълни формата с данните на текущото todo
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': TodoForm(initial=todo.__dict__),#показва формата с текущите данни
    }
    return render(request, 'todo_app/create.html', context)
    # ako не е валидна формата, или не е POST заявка,  показваме я пак
    context = {
        'form': form,
    }
    return render(request, 'todo_app/edit.html', context)