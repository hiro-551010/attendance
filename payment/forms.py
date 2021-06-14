from payment.models import AttendanceEmployee
from django import forms


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = AttendanceEmployee
        fields = ('place', 'in_out')

