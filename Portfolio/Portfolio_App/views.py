from django.shortcuts import render
from Portfolio_App.models import Home,Skills,Language,WorkExp,Education

# Create your views here.

def portfolio(request):
    home = Home.objects.all()
    skills = Skills.objects.all()
    language = Language.objects.all()
    workexp = WorkExp.objects.all().order_by('-id')
    education = Education.objects.all().order_by('-id')
    
    for i in workexp:
        if i.date_leave == None:
            i.date_leave = 'Current'
        
    context = {
        'home' : home,
        'skills' : skills,
        'language' : language,
        'workexp' : workexp,
        'education': education,
    }
    return render(request,'portfolio.html',context)