from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length

def insert_topic(request):
    tn=input("Enter topic: ")
    TTO=Topic.objects.get_or_create(topic_name=tn)
    bl=TTO[1]
    if bl:
        TO=TTO[0]
        TO.save()
        #return HttpResponse("Topic is created.")
        d={"webpage":Topic.objects.all()}
        return render(request,"retrieve_webpage.html",d)
    else:
        return HttpResponse("Topic already exist.")
    
def insert_webpage(request):
    tn=input("Enter the Topic name: ")
    QLTO=Topic.objects.filter(topic_name=tn)
    if QLTO:
        name=input("Enter the name: ")
        url=input("Enter the url: ")
        email=input("Enter the email: ")

        WO=Webpage.objects.get_or_create(topic_name=QLTO[0],name=name,url=url,email=email)
        #return HttpResponse("Webpage is created.")
        d={"webpage":Webpage.objects.all()}
        return render(request,"retrieve_webpage.html",d)

    else:
        return HttpResponse("Topic is not there.")
    
def insert_accessrecord(request):
    
    for i in Webpage.objects.all():
        print(i.id,i.name)

    id=int(input("Enter the id: "))
    QLWO=Webpage.objects.filter(id=id)

    if QLWO:
        name=QLWO[0]
        author=input("Enter the author: ")
        date=input("Enter the date: ")
        AO=AccessRecord.objects.get_or_create(name=name,author=author,date=date)
        #return HttpResponse("AccessRecord is created")
        d={"accessrecord":AccessRecord.objects.all()}
        return render(request,"retrieve_accessrecord.html",d)
    else:
        return HttpResponse("Webpage is not there.")
    
def retrieve_topic(request):
    QLTO=Topic.objects.all()
    d={"topics":QLTO}
    return render(request, "retrieve_topic.html",d)

# def retrieve_webpage(request):
#     QLWO=Webpage.objects.all()
#     d={"webpage":QLWO}
#     return render(request,"retrieve_webpage.html",d)

def retrieve_webpage(request):
    QLWO=Webpage.objects.filter(topic_name="CRICKET")
    QLWO=Webpage.objects.exclude(topic_name="CRICKET")
    QLWO=Webpage.objects.all()[::-1]
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by("-topic_name")
    QLWO=Webpage.objects.filter(topic_name="CRICKET").order_by("-name")
    QLWO=Webpage.objects.all().order_by(Length("name"))
    QLWO=Webpage.objects.order_by(Length('name').desc())

    d={"webpage":QLWO}
    return render(request,"retrieve_webpage.html",d)

def retrieve_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={"accessrecord":QLAO}
    return render(request,"retrieve_accessrecord.html",d)