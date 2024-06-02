from django.db import connection

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from LeadGenerationApp.models import Customer
from LeadGenerationApp.models import States
from LeadGenerationApp.models import Cities

from LeadGenerationApp.serializers import CustomerSerializer
from LeadGenerationApp.serializers import StatesSerializer
from LeadGenerationApp.serializers import CitiesSerializer
from django.http.response import JsonResponse
from .import tuple_to_dict
from django.shortcuts import redirect
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def CustomerInterface(request):
    return render(request, "Customer.html", {})


@xframe_options_exempt
def DisplayAllCustomer(request):
    return render(request, "DisplayAllCustomer.html", {})


@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def CustomerSubmit(request):
    if request.method == 'POST':

        customer_serializer = CustomerSerializer(data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return render(request, "Customer.html", {"message": "Record Submitted Successfully"})

        return render(request, "Customer.html", {"message": "Fail to Submit Record"})


'''
@api_view(['GET','POST','DELETE'])
def Customer_List(request):
  if request.method=='GET':
    customer_list=Customer.objects.all()
    customer_serializer=CustomerSerializer(customer_list,many=True)
    #print("Employee",customer_serializer.data)
    return JsonResponse(customer_serializer.data,safe=False)
  return JsonResponse({},safe=False)
'''


@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Customer_List(request):
    if request.method == 'GET':
        cursor = connection.cursor()
        q = "select E.*,(select S.statename from leadgenerationapp_states S where S.stateid=E.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=E.city) as cityname from leadgenerationapp_Customer E"
        cursor.execute(q)

        data = tuple_to_dict.ParseToDictAll(cursor)
        return JsonResponse(data, safe=False)
    return JsonResponse({}, safe=False)


@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Customer_Update_Delete(request):
    if request.method == 'GET':
        btn = request.GET['btn']
        if (btn == 'Edit'):
            customer = Customer.objects.get(pk=request.GET['id'])

            customer.firstname = request.GET['firstname']
            customer.lastname = request.GET['lastname']
            customer.dob = request.GET['dob']
            customer.emailid = request.GET['emailid']
            customer.mobileno = request.GET['mobileno']
            customer.alternateno = request.GET['alternateno']
            customer.organisationname = request.GET['organisationname']
            customer.address = request.GET['address']
            customer.state = request.GET['state']
            customer.city = request.GET['city']

            customer.save()

        else:
            customer = Customer.objects.get(pk=request.GET['id'])
            customer.delete()
    return redirect('/api/displayallcustomer')


@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Customer_List_By_Id(request):
    if request.method == 'GET':
        customerid = request.GET['customerid']
        cursor = connection.cursor()
        q = "select E.*,(select S.statename from leadgenerationapp_states S where S.stateid=E.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=E.city) as cityname from leadgenerationapp_customer E where E.id={0}".format(
            customerid)
        # print(q)
        cursor.execute(q)
        data = tuple_to_dict.ParseToDictOne(cursor)
        data['dob'] = str(data['dob'])

        return render(request, "CustomerById.html", {'record': data})

    return JsonResponse({}, safe=False)


@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Customer_Display_Picture(request):
    if request.method == 'GET':
        return render(request, "CustomerPicture.html", {"id": request.GET['customerid'], "customername": request.GET['customername'], 'picture': request.GET['picture']})


@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def UpdateCustomerImage(request):

    if request.method == 'POST':
        customer = Customer.objects.get(pk=request.POST['id'])
        customer.photograph = request.FILES['photograph']
        customer.save()
        return redirect('/api/displayallcustomer')
