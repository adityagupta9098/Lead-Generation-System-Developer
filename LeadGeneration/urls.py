"""LeadGeneration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from LeadGenerationApp import views
from LeadGenerationApp import managerview
from LeadGenerationApp import customerview
from LeadGenerationApp import login
from LeadGenerationApp import callview
from LeadGenerationApp import dashboardview



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/employeeinterface',views.EmployeeInterface), 
    url(r'^api/displayallemployee',views.DisplayAllEmployee), 
    url(r'^api/employeesubmit',views.EmployeeSubmit), 
    url(r'^api/employeelist',views.Employee_List), 
    url(r'^api/employeebyid',views.Employee_List_By_Id), 
    url(r'^api/employeeupdatedelete',views.Employee_Update_Delete), 
    url(r'^api/displayemployeepicture',views.Employee_Display_Picture), 
    url(r'^api/updateemployeeimage',views.UpdateEmployeeImage), 

    url(r'^api/statelist',views.State_List), 
    url(r'^api/citylist',views.City_List), 

    url(r'^api/managerinterface',managerview.ManagerInterface), 
    url(r'^api/displayallmanager',managerview.DisplayAllManager), 
    url(r'^api/managersubmit',managerview.ManagerSubmit), 
    url(r'^api/managerlist',managerview.Manager_List), 
    url(r'^api/managerbyid',managerview.Manager_List_By_Id), 
    url(r'^api/managerupdatedelete',managerview.Manager_Update_Delete),
    url(r'^api/displaymanagerpicture',managerview.Manager_Display_Picture), 
    url(r'^api/updatemanagerimage',managerview.UpdateManagerImage), 

    url(r'^api/customerinterface',customerview.CustomerInterface), 
    url(r'^api/displayallcustomer',customerview.DisplayAllCustomer), 
    url(r'^api/customersubmit',customerview.CustomerSubmit), 
    url(r'^api/customerlist',customerview.Customer_List), 
    url(r'^api/customerupdatedelete',customerview.Customer_Update_Delete), 
    url(r'^api/customerbyid',customerview.Customer_List_By_Id), 
    url(r'^api/updatecustomerimage',customerview.UpdateCustomerImage), 
    url(r'^api/display_customer_picture',customerview.Customer_Display_Picture), 
    

    url(r'^api/login',login.Login), 
    url(r'^api/admindashboard',login.AdminDashboard), 
    url(r'^api/managerdashboard',login.ManagerDashboard), 
    url(r'^api/employeedashboard',login.EmployeeDashboard), 
    url(r'^api/checkadminlogin',login.Check_Admin_Login), 
    url(r'^api/checkmanagerlogin',login.Check_Manager_Login), 
    url(r'^api/checkemployeelogin',login.Check_Employee_Login), 
    url(r'^api/logoutadmin',login.LogoutAdmin), 
    url(r'^api/logoutmanager',login.LogoutManager), 
    url(r'^api/logoutemployee',login.LogoutEmployee), 
     



   
    url(r'^api/calldetailsubmit',callview.CallDetailSubmit), 
    url(r'^api/callcustomerbyid',callview.Customer_List_By_Id), 
    url(r'^api/displaycalldetails',callview.DisplayCallDetails), 
    url(r'^api/calldetailslist',callview.CallDetails_List),
    url(r'^api/calldetails_list_by_date',callview.CallDetails_List_By_Date),
    url(r'^api/calldetails_list_by_LeadStatus',callview.CallDetails_List_By_LeadStatus),
    url(r'^api/calldetails_list_by_PhoneStatus',callview.CallDetails_List_By_PhoneStatus),




    url(r'^api/dashboard',dashboardview.Dashboard),

    url(r'^api/hotcall',dashboardview.HotCall),
    url(r'^api/displayhotcalls',dashboardview.DisplayHotCalls),
    
    url(r'^api/warmcall',dashboardview.WarmCall),
    url(r'^api/displaywarmcalls',dashboardview.DisplayWarmCall),
    
    url(r'^api/coldcall',dashboardview.ColdCall),
    url(r'^api/displaycoldcalls',dashboardview.DisplayColdCall),

    url(r'^api/freezecall',dashboardview.FreezeCall),
    url(r'^api/displayfreezecalls',dashboardview.DisplayFreezeCall),
    
    url(r'^api/connectedcall',dashboardview.ConnectedCall),
    url(r'^api/displayconnectedcalls',dashboardview.DisplayConnectedCall),
    
    url(r'^api/disconnectedcall',dashboardview.DisconnectedCall),
    url(r'^api/displaydisconnectedcalls',dashboardview.DisplayDisconnectedCall),


    url(r'^api/callsearch',callview.SearchByName),
    
    
    
   
]
