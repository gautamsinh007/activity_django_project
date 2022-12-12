from django.shortcuts import render 
from .models import *
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
from  .serializers import *
# def home(request):
#     quedata = Questionslist.objects.all()
    
#     return quedata
    
class  quelist(APIView):
    
    def get(self, request):
        data = Questionslist.objects.all()
        serilizer =  queserializers(data,many=True)
        return Response(serilizer.data)
    
    
class  budgetlist(APIView):
    
    def get(self, request):
        bddata = Budgetadd.objects.all()
        serilizer =  budgetserializers(bddata,many=True)
        return Response(serilizer.data)    
       
       
class  showplacelist(APIView):
    
    def get(self, request):
        pldata = Showplace.objects.all()
        serilizer =  placeserializers(pldata,many=True)
        return Response(serilizer.data)    
       
       
       
class filerplacedata(APIView):
    
    
    def get(self,request):
        
        quefk = 3
        # id_ = Questionslist.objects.get(username=request.data['username']).id
        datas =  Showplace.objects.filter(quefk=quefk)
        serializers = placeserializers(datas, many=True)
        
        print(serializers.data)
        # for i in serializers:
        #     print(i)
        
        
        
        return  Response(serializers.data)
        
        
        
        

        