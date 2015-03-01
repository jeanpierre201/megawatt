from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.db.models import Count, Min, Sum, Avg
from django.db import connection

from django.http import *
from django.shortcuts import render_to_response
import socket

from sites.models import Sites
from sites.models import Values

def index(request):

    site_list = Sites.objects.order_by('id')
    
    cursor = connection.cursor()
    #cursor.execute("SELECT * FROM Values WHERE site = %s", 'XYZ Site')
    cursor.fetchone()
      
      
      
    sum_value_a =  Values.objects.filter(site = site_list[0]).aggregate(Sum('valueA')).values()
    sum_value_a2 = Values.objects.filter(site = site_list[1]).aggregate(Sum('valueA')).values()
    sum_value_a3 = Values.objects.filter(site = site_list[2]).aggregate(Sum('valueA')).values()
    sum_value_b =  Values.objects.filter(site = site_list[0]).aggregate(Sum('valueB')).values()
    sum_value_b2 = Values.objects.filter(site = site_list[1]).aggregate(Sum('valueB')).values()
    sum_value_b3 = Values.objects.filter(site = site_list[2]).aggregate(Sum('valueB')).values()
        
    a_list = [sum_value_a , sum_value_a2, sum_value_a3]
    b_list = [sum_value_b , sum_value_b2, sum_value_b3]
    
    table = zip(site_list, a_list, b_list)
    str(table)
        
    context =  ({'table': table})
    return render(request, 'summary/index.html', context)   
    

def average(context):
	
    site_list = Sites.objects.order_by('id')
          
    avg_value_a =  Values.objects.filter(site = site_list[0]).aggregate(Avg('valueA')).values()
    avg_value_a2 = Values.objects.filter(site = site_list[1]).aggregate(Avg('valueA')).values()
    avg_value_a3 = Values.objects.filter(site = site_list[2]).aggregate(Avg('valueA')).values() 
    avg_value_b =  Values.objects.filter(site = site_list[0]).aggregate(Avg('valueB')).values()
    avg_value_b2 = Values.objects.filter(site = site_list[1]).aggregate(Avg('valueB')).values()
    avg_value_b3 = Values.objects.filter(site = site_list[2]).aggregate(Avg('valueB')).values()
        
    a_list = (avg_value_a , avg_value_a2, avg_value_a3)
    b_list = [avg_value_b , avg_value_b2, avg_value_b3]
    
    table = zip(site_list, a_list, b_list)
            
    context = RequestContext(context, {'table': table})
    template = loader.get_template('summary/average.html')
    return HttpResponse(template.render(context))    