# class IndexView(TemplateView):
#     template_name = "index.html"

# .............................................................................

# Function Based View

# from django.http import HttpResponse


# # Function Based View
# def index_entity(request):
#     return HttpResponse("Welcome to Entity")


# # request:  HttpRequest  -- http://127.0.0.1:8000/
# # response: HttpResponse -- Welcome to Entity


# # Function Based View
# def about_entity(request):
#     return HttpResponse("About Entity")


# # request:  HttpRequest  -- http://127.0.0.1:8000/about/
# # response: HttpResponse -- About Entity


# .............................................................................

# Class Based Generic View

# from django.http import HttpResponse
# from django.views import View


# class IndexView(View):
#     def get(self, request):
#         return HttpResponse("Welcome to Entity!")


# ........


# from django.shortcuts import render


# def index_entity(request):
#     return render(request, "index.html")

# ...


# Class Based Generic View
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"
