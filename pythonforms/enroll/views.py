from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def ShowData(request):
    fm= StudentRegistration()
    return render(request, 'form.html', {'form':fm})