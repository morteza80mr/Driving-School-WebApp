from asyncore import read
from email import header
from multiprocessing import context
from django import http
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from requests import request
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()

# Create your views here.

@csrf_exempt
@login_required(redirect_field_name='http://127.0.0.1:8000/')
def student(request):
    if request.user.User_role != 'S':
        return redirect('http://127.0.0.1:8000/logout/')
    else:
        data = classroom.objects.filter()
        context = {
            'data':data
        }
        return render(request,"student_page.html",context)

@csrf_exempt
@login_required(redirect_field_name='http://127.0.0.1:8000/')
def student_selecting_class(request):
    if request.user.User_role != 'S':
        return redirect('http://127.0.0.1:8000/logout/')
    else:
        if request.method == 'POST':
            user = request.user
            status_creation = status(student = User.objects.get(pk=(user.username)),classroom= classroom.objects.get(pk = request.POST.get('number_of_class')))
            status_creation.save()
            return render(request,"student_page_selecting_class.html")
        else:
            return render(request,"student_page_selecting_class.html")

@csrf_exempt
@login_required(redirect_field_name='http://127.0.0.1:8000/')
def registry_man(request):
    if request.user.User_role != 'R':
        return redirect('http://127.0.0.1:8000/logout/')
    else:
        if request.method == 'POST':
            user = User()
            user.family_name_user = str(request.POST.get('family_name'))
            user.set_password(str(request.POST.get('password')))
            user.first_name_user = str(request.POST.get('first_name'))
            user.National_ID_user = str(request.POST.get('National_ID'))
            user.username = str(request.POST.get('National_ID'))
            user.User_role = 'S'
            user.save()
            info = Student()
            info.father_name_Student = str(request.POST.get('father_name'))
            info.Address_Student = str(request.POST.get('Address'))
            info.Zip_code_Student = str(request.POST.get('zipcode'))
            info.Literate = str(request.POST.get('literate'))
            info.Birthday = (request.POST.get('birthday'))
            info.user = User(pk = str(request.POST.get('National_ID')))
            info.save()
            return render(request,"registry_man_page.html")
        else:
            return render(request,"registry_man_page.html")

@csrf_exempt
@login_required(redirect_field_name='http://127.0.0.1:8000/')
def registry_man_Documents(request):
    if request.user.User_role != 'R':
        return redirect('http://127.0.0.1:8000/logout/')
    else:
        if request.method == 'POST':
            user = request.user
            document = Document()
            document.Registry_man_ID = user
            document.Student_ID = User(pk = str(request.POST.get('Student_ID')))
            document.Catched = str(request.POST.get('recived'))
            document.save()
            return render(request,"registry_man_page_Document.html")
        else:
            return render(request,"registry_man_page_Document.html")

@csrf_exempt
@login_required(redirect_field_name='http://127.0.0.1:8000/')
def registry_man_delete(request):
    if request.user.User_role != 'R':
        return redirect('http://127.0.0.1:8000/logout/')
    else:
        if request.method == 'POST':
            user = User(pk = str(request.POST.get('National_ID')))
            user.delete()
            return render (request,'Registry_man_page_delete.html')
        else:
            return render (request,'Registry_man_page_delete.html')

@csrf_exempt
@login_required(redirect_field_name='http://127.0.0.1:8000/')
def financial_man(request):
    if request.user.User_role != 'F':
        return redirect('http://127.0.0.1:8000/logout/')
    else:
        if request.method == 'POST':
            user = request.user
            payment = Tuition()
            payment.Financial_man_ID = user
            payment.Student_ID = User(pk = str(request.POST.get('Student_ID')))
            payment.Price = (request.POST.get('Price'))
            payment.save()
            return render(request,"financial_man_page.html")
        else:
            return render(request,"financial_man_page.html")

@csrf_exempt
@login_required(redirect_field_name='http://127.0.0.1:8000/')
def class_man(request):
    if request.user.User_role != 'C':
        return redirect('http://127.0.0.1:8000/logout/')
    else:
        if request.method == 'POST':
            user = request.user
            class_obj = classroom()
            class_obj.creator_of_class_ID = user
            class_obj.ID_of_Trainer = User(pk = str(request.POST.get('ID_of_Trainer')))
            class_obj.type_of_class = str(request.POST.get('type_of_class'))
            class_obj.Capacity = (request.POST.get('Capacity'))
            class_obj.Date_class = (request.POST.get('Date_Exam'))
            class_obj.Time_class = str(request.POST.get('Time_Exam'))
            class_obj.name_of_Trainer = str(request.POST.get('name_of_Trainer'))
            class_obj.save()
            return render(request,"class_man_page.html")
        else:
            return render(request,"class_man_page.html")

@csrf_exempt
@login_required(redirect_field_name='http://127.0.0.1:8000/')
def manager(request):
    if request.user.User_role != 'M':
        return redirect('http://127.0.0.1:8000/logout/')
    else:
        if request.method == 'POST':
            user = User()
            user.family_name_user = str(request.POST.get('family_name'))
            user.set_password(str(request.POST.get('Password')))
            user.first_name_user = str(request.POST.get('first_name'))
            user.National_ID_user = str(request.POST.get('National_ID'))
            user.username = str(request.POST.get('National_ID'))
            user.User_role = str(request.POST.get('Workspace_Code'))
            user.save()
            return render (request,'Employee_page.html')
        else:
            return render (request,'Employee_page.html')

@csrf_exempt
@login_required(redirect_field_name='http://127.0.0.1:8000/')
def manager_delete(request):
    if request.user.User_role != 'M':
        return redirect('http://127.0.0.1:8000/logout/')
    else:
            if request.method == 'POST':
                user = User(pk = str(request.POST.get('National_ID')))
                user.delete()
                return render (request,'Employee_page_delete.html')
            else:
                return render (request,'Employee_page_delete.html')

@csrf_exempt
@login_required(redirect_field_name='http://127.0.0.1:8000/')
def classroom_institute(request):
    if request.user.User_role != 'T':
        return redirect('http://127.0.0.1:8000/logout/')
    else:
        if request.method == 'POST' :
            class_number = request.POST.get('class_number')
            data = status.objects.filter(classroom = classroom(pk = class_number))
            context = {
                'data':data
            }
            return render(request,"classroom_page.html",context)
        else:
            return render(request,"classroom_page_selecting.html")
