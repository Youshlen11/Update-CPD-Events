from django.db import models

class Jointablesmodel(models.Model):
    id = models.IntegerField(primary_key=True)

    Credit = models.IntegerField()
    CreatedAt = models.DateTimeField()
    UpdatedAt = models.DateTimeField()
    StartDate = models.DateField()
    EndDate = models.DateField()
    DateRange = models.CharField(max_length=50)
    Landline = models.CharField(max_length=20)
    CellPhone = models.CharField(max_length=20)
    EventId = models.IntegerField()
    
    EventType = models.CharField(max_length=50)
    EventTitle = models.CharField(max_length=200)
    EventVenue = models.CharField(max_length=200)
    ValidationNumber = models.CharField(max_length=50)
    OrganisationEvent = models.CharField(max_length=200)
    EventCosts = models.IntegerField()
    Applicants = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=50)
    MobileNumber = models.CharField(max_length=50)