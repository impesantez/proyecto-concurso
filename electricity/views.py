from django.shortcuts import render

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index_loggedin.html')  # Template for logged-in users
    else:
        return render(request, 'index.html')  # Template for guests
