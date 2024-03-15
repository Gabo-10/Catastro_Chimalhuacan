from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template

def Inicio(request):
    
    #doc_externo=open("C:/Users/gabri/Documents/9ISC21/SCM_Chimalhuacan/Proyecto_Chimalhuacan/Proyecto_Chimalhuacan/templates/index.html")
    
    #plt=Template(doc_externo.read())
    
    #doc_externo.close()
    
    doc_externo = get_template('index.html')
    
    #ctx=Context()
    
    documento = doc_externo.render()
    
    return HttpResponse(documento)