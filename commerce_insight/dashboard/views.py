from django.shortcuts import render
from .forms import UploadFileForm
from .analytics import process_csv

def home(request):
    result = None

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            result = process_csv(file)
    else:
        form = UploadFileForm()

    return render(request, "dashboard/home.html", {
        "form": form,
        "result": result
    })