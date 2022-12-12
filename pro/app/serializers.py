from  .models import *
from rest_framework import serializers





class  queserializers(serializers.ModelSerializer):
    class Meta:
        model = Questionslist
        fields = "__all__"


class  budgetserializers(serializers.ModelSerializer):
    budget = serializers.StringRelatedField(many=True,read_only=True)
    class Meta: 
        model = Budgetadd
        fields = ['id','addbud','quefk',"budget"]
        

class  placeserializers(serializers.ModelSerializer):
    
    # budget = serializers.StringRelatedField(many=True,read_only=True)
    
    class Meta:
        model = Showplace
        fields = ['id','placeadd','detail','budgetfk','quefk']