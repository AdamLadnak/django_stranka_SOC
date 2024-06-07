from django.shortcuts import render, HttpResponse
from . models import *

def vypis_tem(request):
    temy = Tema.objects.all().order_by("nazov")
    return render(request, "soc/index.html", {"temy":temy})

def vypis_temy(request, tema):
    tema = Tema.objects.get(id=tema)
    return render(request, "soc/tema_detail.html", {"tema":tema})

def vypis_ucitela(request, ucitel):
    ucitel = Ucitel.objects.get(id=ucitel)
    temy = Tema.objects.filter(konzultant=ucitel)
    return render(request, "soc/ucitel_detail.html", {"ucitel":ucitel, "temy":temy})

def vypis_studenta(request, student):
    student = Student.objects.get(id=student)
    temy = Tema.objects.filter(student=student)
    return render(request, "soc/student_detail.html", {"student":student, "temy":temy})

def statistics(request):
    cakajuce = Tema.objects.filter(dostupnost="čakajúce").count()
    volne = Tema.objects.filter(dostupnost="voľné").count()
    schvalene = Tema.objects.filter(dostupnost="schválené").count()
    
    pocet_tem = Tema.objects.count()
    pocet_ucitelov = Ucitel.objects.count() 
    pocet_studentov = Student.objects.count()
    return render(request, "soc/statistics.html", {"cakajuce":cakajuce, "volne":volne, "schvalene":schvalene, "pocet_tem":pocet_tem, "pocet_ucitelov":pocet_ucitelov, "pocet_studentov":pocet_studentov})
