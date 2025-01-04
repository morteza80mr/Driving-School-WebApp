"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from . import views

urlpatterns = [
    path('student/',views.student),
    path('student/selecting_class/',views.student_selecting_class),
    path('registry_man/',views.registry_man),
    path('registry_man/Documents/',views.registry_man_Documents),
    path('registry_man/Delete/',views.registry_man_delete),
    path('financial_man/',views.financial_man),
    path('class_man/',views.class_man),
    path('manager/',views.manager),
    path('manager/delete/',views.manager_delete),
    path('classroom/',views.classroom_institute),
]