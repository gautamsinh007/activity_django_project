from django.db import models

# Create your models here.


class Questionslist(models.Model):
    addque =  models.CharField(max_length=100)

    def __str__(self):
        return  self.addque
    


class Budgetadd(models.Model):
    
    addbud  = models.CharField(max_length=100)
    quefk = models.ForeignKey(Questionslist,on_delete=models.CASCADE,related_name="lol")
    
    def __str__(self):
        return  self.addbud    

class Showplace(models.Model):
    
    placeadd = models.CharField(max_length=100)
    detail  = models.CharField(max_length=100)
    budgetfk = models.ForeignKey(Budgetadd,on_delete=models.CASCADE, related_name="budget")
    quefk = models.ForeignKey(Questionslist,on_delete=models.CASCADE, related_name='que')

    
    def __str__(self):
        return  self.placeadd 
    
    
    
    
    
    
    
    
    