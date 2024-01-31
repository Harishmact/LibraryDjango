from django.shortcuts import render

# Create your views here.
from books.models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.serializers import bookserializer,userserializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins,generics,viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class userviewset(viewsets.ModelViewSet):     #both primarykey and non primary key based
    queryset = User.objects.all()
    serializer_class = userserializer


#viewset class both primarykey based and nonprimarykey based
class bookviewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Book.objects.all()
    serializer_class = bookserializer




#CLASS BASED VIEWS USING GENERICS
# class booklist(generics.ListCreateAPIView):        #non primary key based
#
#     queryset = Book.objects.all()
#     serializer_class=bookserializer
#
# class bookdetail(generics.RetrieveUpdateDestroyAPIView):     #primarykey based
#
#     queryset = Book.objects.all()
#     serializer_class=bookserializer
#


#MIXINS CLASS

# class booklist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#
#     queryset = Book.objects.all()  # retrieving all records (data-django object format)
#     serializer_class=bookserializer   #serialization(dof-->json format)
#
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
#
# class bookdetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#
#     queryset = Book.objects.all()
#     serializer_class=bookserializer
#
#     def get(self,request,pk):
#         return self.retrieve(request)
#     def put(self,request,pk):
#         return self.update(request)
#
#     def delete(self, request, pk):
#         return self.destroy(request)





#class based to view
#non primary key based
# class booklist(APIView):
#    def get(self,request):
#        book = Book.objects.all()  # retrieving all records (data-django object format)
#        s=bookserializer(book,many=True)    #serialization(dof-->json format)
#        return Response(s.data)
#    def post(self,request):
#        s=bookserializer(data=request.data)   #req+data<---      deserialzing the data
#        if s.is_valid():
#            s.save()         #saves to the table
#            return Response(s.data,status=status.HTTP_201_CREATED)
#        return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

#primarykey based
#
# class bookdetail(APIView):
#     def get_object(self,pk):
#        try:
#            return Book.objects.get(pk=pk)
#         except:
#            raise Http404
#    def get(self,request,pk):
#        book=self.get_object(pk)
#         s = bookserializer(book)  # serialization
#        return Response(s.data)
#    def put(self,request,pk):
#        book=self.get_object(pk)
#        s = bookserializer(book,data=request.data)
#        if s.is_valid():
#
#            s.save()         #saves to the table
#            return Response(s.data,status=status.HTTP_201_CREATED)
#        return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#    def delete(self,request,pk):
#        book=self.get_object(pk)
#        book.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
