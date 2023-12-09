from django.shortcuts import render

def condition(request):
    d={'a':2,'b':1}
    return render(request,'condition.html',context=d)
