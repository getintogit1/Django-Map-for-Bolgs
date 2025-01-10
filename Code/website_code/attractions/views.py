# attractions/views.py

from django.shortcuts   import render, redirect, get_object_or_404
from django.db.models   import Q
from django.http        import HttpResponse

from django.shortcuts   import render
from attractions.models import Attraction

def attraction_index(request):
    attractions = Attraction.objects.all()
    context = {
        "attractions": attractions
    }
    return render(request, "attractions/attraction_index.html", context)

# def attraction_detail(request, pk):
#     attraction = attraction.objects.get(pk=pk)
#     context = {
#         "attraction": attraction
#     }
#     return render(request, "attractions/attraction_detail.html", context)

def attraction_detail(request, slug):
    attraction = get_object_or_404(Attraction, slug=slug)
    context = {
        "attraction": attraction
    }
    return render(request, "attractions/attraction_detail.html", context)

def get_attractions_query_set(query=None):
    queryset= []
    queries = query.split(" ")                                                  # python install 2023 = [python, install, 2023]
    for q in queries:
        attractions = Attraction.objects.filter(
            Q(title__icontains = q) |
            Q(description__icontains = q) 
        ).distinct()                                                            # all posts in the list retrive are uniuque

        for attraction in attractions:
            queryset.append(attraction)
    return list(set(queryset))