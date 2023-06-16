import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import MinioUploadForm
from .models import Media
from .upload_func import uploader


class MinioUplaodView(View):
    def get(self, request):
        form = MinioUploadForm()
        return render(
            request,
            "minio_uploader/index.html",
            {
                "form": form,
            },
        )

    def post(self, request):
        form = MinioUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # getting new object
            media = Media.objects.last()

            # upload object to minio
            bucket = media.bucket
            object_extention = os.path.splitext(media.media.path)[1]
            object_name = f"{media.media_saved_name}{object_extention}"
            object_path = media.media.path
            uploader(bucket=bucket, object_name=object_name, object_path=object_path)

            return render(
                request,
                "minio_uploader/index.html",
                {
                    "form": form,
                },
            )
        return render(
            request,
            "minio_uploader/index.html",
            {
                "form": form,
            },
        )
