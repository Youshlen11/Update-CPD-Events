from urllib import request
from RestAPI.serializers import Jointableserializer
from RestAPI.models import Jointablesmodel
from rest_framework import viewsets

from rest_framework.decorators import api_view

api_view(['GET'])
class Jointableapi(viewsets.ModelViewSet):
    queryset=Jointablesmodel.objects.raw('select ApprovedEvents.id,ApprovedEvents.Credit,ApprovedEvents.CreatedAt,ApprovedEvents.UpdatedAt,ApprovedEvents.StartDate,ApprovedEvents.EndDate,ApprovedEvents.DateRange,ApprovedEvents.Landline,ApprovedEvents.CellPhone,ApprovedEvents.EventId,Events.EventType,Events.EventTitle,Events.EventVenue,Events.ValidationNumber,Events.OrganisationEvent,Events.EventCosts,Events.Applicants,Events.Email,Events.PhoneNumber,Events.MobileNumber from ApprovedEvents inner join Events on ApprovedEvents.id = Events.id')
    serializer_class=Jointableserializer

    
    