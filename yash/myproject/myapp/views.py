from django.shortcuts import render
from .models import Person

def person_list(request):
    people = Person.objects.all()
    return render(request, 'person_list.html', {'people': people})
