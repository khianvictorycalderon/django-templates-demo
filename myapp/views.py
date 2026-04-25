from django.shortcuts import render
from django.utils.timezone import now

# Create your views here.
def home(request):
    data = {
        "message": "Sample message from server!",
        "date": now()
    }
    return render(request, "home.html", data)