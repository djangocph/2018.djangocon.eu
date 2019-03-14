from django import forms

from . import models


class BicycleBookingForm(forms.ModelForm):

    class Meta:
        model = models.BicycleBooking
        widgets = {
            'size': forms.widgets.RadioSelect
        }
        fields = ('bicycle_type', 'size', 'frame_type', 'from_date', 'days', 'confirmed')


class TShirtForm(forms.ModelForm):

    class Meta:
        model = models.TShirtPreference
        widgets = {
            'size': forms.widgets.RadioSelect,
            'fit': forms.widgets.RadioSelect,
        }
        fields = ('size', 'fit', 'confirmed')
