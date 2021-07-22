from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    
    context = {
        
    }

    return render(request, 'vic/home.html', context)