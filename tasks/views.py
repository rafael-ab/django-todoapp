from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.base import View
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Task
from .forms import TaskForm

# Create your views here.
class Todo(View):
    def get(self, request, *args, **kwargs):
        tasks_active = list(reversed(Task.objects.filter(active=True)))
        tasks_done = list(reversed(Task.objects.filter(active=False)))
        context = {
            'form': TaskForm(),
            'tasks_active': tasks_active,
            'tasks_done': tasks_done,
        }
        return render(request, 'tasks/todo.html', context)
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if not request.POST['name']:
            messages.error(request, 'You need to add a task')
            redirect('todo')
        elif form.is_valid():
            form.save()
            form = TaskForm()
            messages.success(request, 'New task created successfully!')
        tasks_active = reversed(Task.objects.filter(active=True))
        tasks_done = reversed(Task.objects.filter(active=False))
        context = {
            'form': form,
            'tasks_active': tasks_active,
            'tasks_done': tasks_done,
        }
        return render(request, 'tasks/todo.html', context)

class TaskUpdate(SuccessMessageMixin, UpdateView):
    model = Task
    fields = ['name']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('todo')
    success_message = 'Task updated successfully!'
    
    def get_object(self, queryset=None):
        return Task.objects.get(pk=self.kwargs['pk'])

class TaskDelete(DeleteView):
    model = Task
    template_name_suffix = '_delete'
    success_url = reverse_lazy('todo')
    success_message = 'Task deleted successfully!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TaskDelete, self).delete(request, *args, **kwargs)

def task_update_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.active = not task.active
    task.save()
    return redirect('todo')