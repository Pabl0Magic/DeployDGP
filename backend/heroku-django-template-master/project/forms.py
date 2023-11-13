""" Forms to work with in the project """

from django import forms
from .models import Room, UploadedFile


class RoomForm(forms.ModelForm):
    """Formulary for room"""

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta class for the form"""

        model = Room
        fields = ["name", "size"]


class FileUploadForm(forms.ModelForm):
    """Formulary for uploading a file"""

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta class for the form"""

        model = UploadedFile
        fields = ["file"]
