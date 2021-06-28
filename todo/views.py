from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.edit import DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy


# Create your views here.

class TodoList(ListView):
    template_name = 'List.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title','contens','priority','duedate')
    success_url = reverse_lazy('list')  #urlの第二引数で指定したnameがlistというところに繋がっている

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title','contens','priority','duedate')
    success_url = reverse_lazy('list')
