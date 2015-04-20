from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from models import Table
# Create your views here.


def form(request):
   
    if request.method == "POST":
        
        try:
            num = Table.objects.get(url=request.POST["nombre"]).id
            return HttpResponse("La url cortada es :"+str(num))
        except Table.DoesNotExist:
            record = Table(url= request.POST["nombre"].replace('%3A',':').replace('%2F','/'))  
            record.save()
            return HttpResponse("La url cortada es :" +"<a href="+Table.objects.get(url=request.POST["nombre"]).url +">"+str(Table.objects.get(url=request.POST["nombre"]).id)+"</a>")
    form=""
    form+="<body><h1>Url Shortener </h1><form method=post>Escribe la url:<input type=text name= nombre value=http:// /> <br/><input type=submit value=Enviar /></form></body></html>"   
    
    return HttpResponse(form)
    

def show_url (request,num):
    try:
        url=(Table.objects.get(id=num).url)
    except Table.DoesNotExist:
        return HttpResponseNotFound(" 404 Not Found")
    return HttpResponseRedirect(url)
