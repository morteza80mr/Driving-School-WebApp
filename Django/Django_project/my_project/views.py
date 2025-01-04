from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Driving_school.models import *
from django.contrib.auth import login,authenticate,logout
# Create your views here.

@csrf_exempt
def landing_page(request):
    if request.method == 'POST':
        Workspace_Code = str(request.POST.get('Workspace_Code'))
        ID = str(request.POST.get('ID'))
        Password = str(request.POST.get('Password'))
        user = authenticate(request, username = ID , password = Password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if Workspace_Code == "R" :
                    return redirect('http://127.0.0.1:8000/Driving_school/registry_man/',)
                elif Workspace_Code == "S" :
                    return redirect('http://127.0.0.1:8000/Driving_school/student/',)
                elif Workspace_Code == "F" :
                    return redirect('http://127.0.0.1:8000/Driving_school/financial_man/',)
                elif Workspace_Code == "C" :
                    return redirect('http://127.0.0.1:8000/Driving_school/class_man/',)
                elif Workspace_Code == "T" :
                    return redirect('http://127.0.0.1:8000/Driving_school/classroom/',)
                elif Workspace_Code == "M" :
                    return redirect('http://127.0.0.1:8000/Driving_school/manager/',)
            else:
                return HttpResponse("not logged data not valid")
        else :
            return HttpResponse("not logged data none")
    else:
        return render(request,"Landing_page.html")

def log_out(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')