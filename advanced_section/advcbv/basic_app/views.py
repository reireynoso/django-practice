from django import http
from django.http.response import HttpResponse
from django.shortcuts import render
# from django.views.generic import View
from django.views.generic import (View, 
                                TemplateView, 
                                ListView, 
                                DetailView, 
                                CreateView, 
                                UpdateView, 
                                DeleteView)
from basic_app import models
from django.urls import reverse_lazy
# from django.http import HttpResponse
# Create your views here.
# def index(request):
#     return render(request,'index.html')

# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Class BAsed Views are cool")

class IndexView(TemplateView):
    # provide path to where the file is. If it's `basic_app/index.html`
    template_name = 'index.html'

    # injecting data
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'Basic Injection!'
        return context

class SchoolListView(ListView):
    context_object_name = "schools"
    # list out all schools in school model
    model = models.School
    # under the hood, ListView is creating the school_list

class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    # show all the details of a specific entry in that school
    # includes showing all students for a particular school
    model = models.School
    template_name = 'basic_app/school_detail.html'
    # under the hood, DetailView is creating the school variable

class SchoolCreateView(CreateView):
    # provide fields for the form
    fields = ('name','principal', 'location')
    model = models.School 

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School 
    # once successfully deleted, redirect to the list page of the basic app and show all the schools
    success_url = reverse_lazy("basic_app:list")