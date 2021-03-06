from django import forms
from django.core.exceptions import ValidationError
from . import models


class RegionalLeadForm(forms.ModelForm):

    class Meta:
        model = models.RegionalLead
        exclude = ()

    def clean(self):
        location = self.cleaned_data['location']
        error_message = []
        for u in self.cleaned_data['leads']:
            if not u.profile:
                error_message.append('Profile for user %s not found' % (u))
            elif u.profile.location != location:
                error_message.append(
                    "User %s doesn't belong to region %s" % (u, location))
        if error_message:
            raise ValidationError(error_message)


class LocationForm(forms.ModelForm):

    class Meta:
        model = models.Location
        exclude = ()


class StateForm(forms.ModelForm):

    class Meta:
        model = models.State
        exclude = ()
