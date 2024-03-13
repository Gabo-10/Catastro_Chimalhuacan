from django.http import HttpResponse
import datetime
from django.template import Template, Context

def Inicio(request):
    
    doc_externo=open("C:/Users/gabri/Documents/9ISC21/SCM_Chimalhuacan/Proyecto_Chimalhuacan/Proyecto_Chimalhuacan/templates/index.html")
    
    plt=Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx=Context()
    
    documento = plt.render(ctx)
    
    return HttpResponse(documento)