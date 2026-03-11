from django.urls import path
from . import views

urlpatterns = [

    path('upload/', views.upload_document),
    path('list/', views.document_list),
    path('verify/<int:id>/', views.verify_document),

]