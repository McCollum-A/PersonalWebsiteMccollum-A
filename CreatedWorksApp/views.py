from django.shortcuts import render, get_object_or_404
from .models import Works


# Create your views here.
def home(request):
    AllWorks = Works.objects.all()
    return render(request, 'CreatedWorksApp/home.html', {'AllWorks': AllWorks})


def projectabstract(request, Works_id):
    ProjectAbstract = get_object_or_404(Works, pk=Works_id)
    return render(request, 'CreatedWorksApp/Abstract.html', {'ProjectAbstract': ProjectAbstract})
