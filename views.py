from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, mixins
from . import models
from .serializers import BookSerializer

class MybookCreateViews(generics.ListAPIView, mixins.CreateModelMixin):
    lookup_field     = 'pk'
    serializer_class = BookSerializer

    # queryset     = models.Book.objects.all()

    def get_queryset(self):
        qs = models.Book.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)
                ).distinct()
        return qs       
    
    # def perform_create(self, serializer):
    #     serializer.save(name=self.request.name)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args,**kwargs)

    #  def put(self, request, *args, **kwargs):
    #     return self.create(request, *args,**kwargs)

    #  def patch(self, request, *args, **kwargs):
    #     return self.create(request, *args,**kwargs)
        
class MybookViews(generics.RetrieveUpdateDestroyAPIView):
    lookup_field     = 'pk'
    serializer_class = BookSerializer

    # queryset     = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.all()
    
    # def get_objects(self):
    #     pk = self.kwargs.get('pk')
    #     return models.Book.objects.get(pk=pk)