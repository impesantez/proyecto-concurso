from django.http import HttpResponse
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from .models import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddUsageForm
from django.http import JsonResponse

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index_loggedin.html')
    else:
        return render(request, 'index.html')

@login_required
def add_usage(request):
    if request.method == "POST":
        form = AddUsageForm(request.POST)
        if form.is_valid():
            carbon_footprint = form.save(commit=False)
            carbon_footprint.user = request.user
            carbon_footprint.save()
            return redirect('electricity:dashboard')
    else:
        form = AddUsageForm()

    return render(request, 'add_usage.html', {'form': form})

def usage_info(request, usage_id):
    usage = Usage.objects.get(id=usage_id)
    return JsonResponse({
        'usage_hour': usage.usage_hour,
        'usage_per_time': usage.usage_per_time
    })

@login_required
def dashboard(request):
    user = request.user
    footprints = Carbon_footprint.objects.filter(user=user)
    total_kwh = sum(footprint.kwh for footprint in footprints)
    total_carbon = sum(footprint.carbon for footprint in footprints)
    
    context = {
        'footprints': footprints,
        'total_kwh': total_kwh,
        'total_carbon': total_carbon,
    }
    return render(request, 'index_loggedin.html', context)


