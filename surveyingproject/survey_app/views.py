from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .models import MarkedPosition


def index(request):
    lng, lat, note = "", "", ""
    locations = []
    
    if request.GET.get("Long"):
        lng = request.GET.get("Long")

    if request.GET.get("Lat"):
        lat = request.GET.get("Lat")

    if request.GET.get("Note"):
        note = request.GET.get("Note")

    if lng and lat and note:
        position = MarkedPosition()
        position.Longitude = lng
        position.Latitude = lat
        position.Notes = note
        position.save()

    markedLocations = MarkedPosition.objects.all()
    for loc in markedLocations:
        location={
            "Longitude":loc.Longitude,
            "Latitude":loc.Latitude,
            "Notes":loc.Notes
        }
        locations.append(location)
        
    context = {
      "locations":locations
    }

    return render(request,"survey_app/index.html", context) 
    
