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
      
    sum_value = Values.objects.values('site_id').filter(site__in = site_list).annotate(sum_a = Sum('valueA')).annotate(sum_b = Sum('valueB'))
    
    list_values = zip(site_list, sum_value)
        
    context =  ({'site_list': site_list, 'list_values':list_values})
    return render(request, 'summary/index.html', context)   
    

def average(request):
	
    site_list = Sites.objects.order_by('id')
          
    avg_value = Values.objects.values('site_id').filter(site__in = site_list).annotate(sum_a = Avg('valueA')).annotate(sum_b = Avg('valueB'))
        
    list_values = zip(site_list, avg_value)
            
    context =  ({'site_list': site_list, 'list_values':list_values})
    return render(request, 'summary/index.html', context)   
     
