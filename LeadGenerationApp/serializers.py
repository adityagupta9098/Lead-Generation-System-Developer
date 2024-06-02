from rest_framework import serializers 
from LeadGenerationApp.models import  Employee
from LeadGenerationApp.models import  Customer
from LeadGenerationApp.models import  Manager
from LeadGenerationApp.models import  States
from LeadGenerationApp.models import  Cities
from LeadGenerationApp.models import  Administrator
from LeadGenerationApp.models import  CallDetail

class EmployeeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Employee
        fields = ('id','firstname', 'lastname', 'dob', 'gender', 'emailid', 'mobileno', 'address', 'state', 'city', 'designation', 'managerid', 'photograph','password')
  
class StatesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = States
        fields = ('id','stateid','statename')
  
class CitiesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model =  Cities
        fields = ('id','stateid','cityid','cityname')
   
class ManagerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Manager
        fields = ('id','firstname', 'lastname', 'dob', 'gender', 'emailid', 'mobileno', 'address', 'state', 'city', 'photograph','password')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','firstname', 'lastname', 'dob', 'emailid', 'mobileno','alternateno', 'address', 'state', 'city', 'organisationname','photograph')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('id','mobileno','adminname','password')

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallDetail
        fields = ('id', 'customerid', 'customername', 'callerid', 'status', 'callername', 'currentdate', 'phonestatus', 'conversation', 'leadstatus', 'mobileno')
