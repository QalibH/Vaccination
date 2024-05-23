from django.db import models
from camp.models import Campaign, Slot
from django.contrib.auth.models import User

class Vaccination(models.Model):
    patient = models.ForeignKey(User, related_name='patient', on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, related_name='campaign', on_delete=models.CASCADE)
    slots = models.ManyToManyField(Slot, related_name='slots', blank=True)
    date = models.DateField(null=True, blank=True)
    is_vaccinated = models.BooleanField(default=False)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__ (self):
        return self.patient.get_full_name() + ' | ' + str(self.campaign.vaccine.name)
