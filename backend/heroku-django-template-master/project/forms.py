from django import forms
from .models import Room, UploadedFile

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'size']

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
