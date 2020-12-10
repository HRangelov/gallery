from django.shortcuts import render
from django.views.generic import TemplateView


# def landing_page(request):
#     return render(request, 'landing_page.html')

class LandingPageView(TemplateView):
    template_name = 'landing_page.html'