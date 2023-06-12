from django import forms
from .models import Media


class MinioUploadForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = "__all__"
