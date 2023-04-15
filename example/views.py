from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer


class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request,*args,**kwargs)
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class BookAPIMixins(mixins.RetrieveModelMixin, generics.GenericAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  lookup_field = 'bid'

  def get(self, request, *args, **kwargs):
   return self.retrieve(request, *args, **kwargs)
  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)
  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)
