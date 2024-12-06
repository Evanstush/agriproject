from django import forms

from agriapp.models import ImageModel,Contact


class CONTACTForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'