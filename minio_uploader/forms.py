from django import forms
from .models import Media


class MinioUploadForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = "__all__"
        widgets = {
            "bucket":forms.TextInput(attrs={"class":"form-control"}),
            "media_saved_name":forms.TextInput(attrs={"class":"form-control"}),
            "media":forms.FileInput(attrs={"class":"form-control"}),
        }
