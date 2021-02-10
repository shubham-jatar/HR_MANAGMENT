from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from Homeadmin import views

urlpatterns = [
    path('admin/', TemplateView.as_view(template_name="admin/adminlogin.html"),name='Homeadmin'),
    path('checklogin/',views.checkLogin,name='login'),
    path('AddEmpyee',views.AddEmployee.as_view(),name="AddEmpyee"),
    path('viewEmployee/',views.ViewEmployee.as_view(),name='ViewEmployee'),
    path('showEmployee/',views.ShowEmployee.as_view(),name='showEmployee'),
    path('updateEmployee/',views.UpdateEmployee,name="update"),
    path('saveupdate/',views.saveupdate,name="saveupdate"),
    path('deleteEmployee/',views.DeleteEmployee.as_view(),name="deleteEmployee")

]
