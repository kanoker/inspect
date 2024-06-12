# inspections/forms.py
from django import forms
from .models import Inspection, Vehicle, Photo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', 'Upload'))

# class PhotoSessionForm(forms.ModelForm):
#     class Meta:
#         model = PhotoSession
#         fields = ['inspection']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Start Session'))

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['vehicle', 'inspector', 'inspection_date', 'inspection_report', 'status']
        widgets = {
            'inspection_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=[('pending', 'Pending'), ('completed', 'Completed')]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Start Inspection'))

        


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['license_plate', 'make', 'model', 'year']

        