from django.shortcuts import render

from polls.models import *
# Create your views here.


def my(request):




    key = request.POST.get("key")
    if key:
        p = Person(first_name=key)
        p.save()

    data = Person.objects.all()

    Person.objects.filter(first_name=request.GET.get("n")).delete()

    keyno = request.GET.get("no")
    keyyes = request.GET.get("yes")
    if(keyno=="забито"):
        o=no(n=keyno)
        o.save()
    elif(keyyes=="сделано"):
        o=yes(n=keyyes)
        o.save()
    non=no.objects.count()
    yesy=yes.objects.count()


#

    return render(request,"index.html",context={"data":data,"no":non,"yes":yesy,})

