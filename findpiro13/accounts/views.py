from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    request.user
    return render(request, 'accounts/profile.html')
    pass
# Create your views here.
