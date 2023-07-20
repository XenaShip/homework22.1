from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from homework.models import Product, Note
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .forms import ProductForm, VersionForm
from homework.models import Product, Version
from django.forms import inlineformset_factory


class ProductListView(generic.ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Список товаров'
        return context_data
# Create your views here.


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('homework:index')
    extra_context = {
        'title': 'Создание продукта'
    }


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('homework:index')


class ContactsTemplateView(generic.TemplateView):
    template_name = 'homework/contacts2.html'


#class NoteCreateView(generic.CreateView):
#    model = Note
#    fields = ('name', 'the_text', 'image', 'published')
#    success_url = reverse_lazy('homework:blog')


class NoteDetailView(generic.DetailView):
    model = Note

    def get_object(self, queryset=None):
        note = super().get_object()
        note.views_up()
        return note

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Просмотр статьи'
        return context_data


class NoteListView(generic.ListView):
    model = Note


class NoteUpdateView(generic.UpdateView):
    model = Note
    fields = ('name', 'the_text', 'image', 'published')
    extra_context = {
        'title': 'изменить статью'
    }

    def get_success_url(self):
        return reverse('homework:note_detail', args=[*self.kwargs.values()])


class NoteCreateView(generic.CreateView):
    model = Note
    fields = ('name', 'the_text', 'image', 'published')
    success_url = reverse_lazy('homework:blog')
    extra_context = {
        'title': 'Создание статьи'
    }


class NoteDeleteView(generic.DeleteView):
    model = Note
    success_url = reverse_lazy('homework:blog')


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    extra_context = {
        'title': 'Изменение продукта'
    }
    success_url = reverse_lazy("homework:index")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_formset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        context_data['formset'] = version_formset()

        if self.request.method == 'POST':
            context_data['formset'] = version_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = version_formset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)