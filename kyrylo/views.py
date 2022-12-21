from django.shortcuts import render
from practicalapp.models import ProgrammingLanguage

# Create your views here.
def show_kyrylo(request):
    ratings_language = ProgrammingLanguage.objects.all()
    return render(request, 'kyrylo.html', context = {'ratings_language': ratings_language})