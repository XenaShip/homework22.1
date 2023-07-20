from django.urls import path
from django.views.generic import TemplateView

from .views import ProductListView, ProductDetailView, ProductCreateView, NoteListView, NoteUpdateView, \
    NoteDetailView, NoteCreateView, NoteDeleteView, ContactsTemplateView, ProductUpdateView, ProductDeleteView

app_name = 'homework'

urlpatterns = [
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('', ProductListView.as_view(), name='index'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('blog/', NoteListView.as_view(), name='blog'),
    path('update_note/<slug:slug>/', NoteUpdateView.as_view(), name='update_note'),
    path('create_note/', NoteCreateView.as_view(), name='create_note'),
    path('note_delete/<slug:slug>/', NoteDeleteView.as_view(), name='note_delete'),
    path('note_detail/<slug:slug>/', NoteDetailView.as_view(), name='note_detail'),
]