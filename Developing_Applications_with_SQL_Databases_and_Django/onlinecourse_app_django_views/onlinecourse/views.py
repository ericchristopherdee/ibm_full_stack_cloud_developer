from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic
from django.http import Http404

# Create your views here.

def popular_course_list(request):
    context = {}
    if request.method == 'GET':
        course_list = Course.objects.order_by('-total_enrollment')[:10]
        # Creates a key value, and its pairing.
        context['course_list'] = course_list
        # Uses the Django template language markup to provide a supplementary html based on the tagged element layout
        return render(request, 'onlinecourse/course_list.html', context)

def enroll(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=course_id)
        course.total_enrollment += 1
        course.save()
        return HttpResponseRedirect(reverse(viewname='onlinecourse:popular_course_list'))
        # It is considered best practice to return an http/response redirect upon success of a post.