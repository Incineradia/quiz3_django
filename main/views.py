from django.shortcuts import render
from .models import Students
from django.views import View
# Create your views here.
class SomethingClass(View):
    def get(self, request):
        students=Students.objects.all()
        return render(request, 'main\home.html', {'all_students': students})