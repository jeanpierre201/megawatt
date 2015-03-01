from django.shortcuts import get_object_or_404, render

from sites.models import Sites
    
def index(request):
    site_list = Sites.objects.order_by('id')[:5]
    context = {'site_list': site_list}
    return render(request, 'sites/index.html', context)
    
def detail(request, site_id):
    site = get_object_or_404(Sites, pk=site_id)
    return render(request, 'sites/detail.html', {'site': site})
    
