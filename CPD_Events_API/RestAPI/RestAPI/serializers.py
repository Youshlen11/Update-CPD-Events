from dataclasses import field
from rest_framework import serializers
from RestAPI.models import Jointablesmodel

class Jointableserializer(serializers.ModelSerializer):
    class Meta:
        model=Jointablesmodel
        fields='__all__'
        #['id','Credit','CreatedAt','UpdatedAt','StartDate','EndDate','DateRange','Landline','CellPhone','EventId','EventType','EventTitle','EventVenue','ValidationNumber','OrganisationEvent','EventCosts','Applicants','Email','PhoneNumber','MobileNumber']

    

    