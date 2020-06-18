from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Flight,Passengers
def index(request):
    context={"flights":Flight.objects.all()}
    return render(request,"flights/index.html",context)

def flight(request,flight_id):
    try:
        flight=Flight.objects.get(pk=flight_id)
    except:
        raise Http404("Flight does not exist")
    context={
    "flight":flight,
    "passsengers":flight.passengers.all(),
    "non_passengers":Passengers.objects.exclude(flights=flight).all()
    }
    return render(request,"flights/flight.html",context)
def book(request,flight_id):
    try:
        passenger_id=int(request.POST["passenger"])
        flight=Flight.objects.get(pk=flight_id)
        passenger=Passengers.objects.get(pk=passenger_id)
    except Passengers.DoesNotExist:
        raise Http404("Passenger Does Not Exist")
    except KeyError:
        return HttpResponse("wrind")
    except Flight.DoesNotExist:
        raise Http404("Flight Does Not Exist")
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight",args=(flight_id,)))
