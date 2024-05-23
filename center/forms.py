from django.forms import ModelForm
from center.models import Center, Storage

class CenterForm(ModelForm):
    class Meta:
        model = Center
        fields = '__all__'

class StorageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        center_id = kwargs.pop('center_id')
        super(StorageForm, self).__init__(*args, **kwargs)
        self.fields['center'].queryset = Center.objects.filter(id=center_id)
        self.fields['center'].disabled = True
        self.fields['booked_quantity'].disabled = True



    class Meta:
        model = Storage
        fields = '__all__'