from django.shortcuts import render, redirect


def instructorhomepage(request):
    return render(request,'instructorapp/instructorhomepage.html')

def sharegardeningtips(request):
    return render(request,'instructorapp/sharegardeningtips.html')

def contactsupport(request):
    return render(request,'instructorapp/contactsupport.html')