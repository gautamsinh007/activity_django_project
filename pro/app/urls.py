from django.urls import path , include
from .import views



urlpatterns = [
    
    path('api-auth/', include('rest_framework.urls')),
    path('quedata',views.quelist.as_view()),
    path('buddata',views.budgetlist.as_view()),
    path('plcdata',views.showplacelist.as_view()),
    path('place',views.filerplacedata.as_view()),
             
        
  
]


