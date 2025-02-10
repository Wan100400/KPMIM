from django.shortcuts import render
from Registration.models import Course, Mentor
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    context = {
        'fathername': 'Nasron',
        'greeting': 1,
    }
    return render(request, "index.html", context)

def course(request):
    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        data = Course(code=c_code, description=c_desc)
        data.save()
        allcourse = Course.objects.all().values()
        dict = {
            'message': 'Data Saved',
            'allcourse': allcourse,
        }
    else:
        allcourse = Course.objects.all().values()
        dict = {
            'message': 'Unsuccessful',
            'allcourse': allcourse,
        }
    return render(request, "Course.html", dict)

def mentor(request):
    allmentor = Mentor.objects.all().values()

    if request.method == 'POST':
        m_code = request.POST['mentorCd']
        m_name = request.POST['mentorName']
        m_email = request.POST['mentorEmail']
        data = Mentor(mentorCd=m_code, mentorName=m_name, mentorEmail=m_email)
        data.save()

        dict = {
            'message': 'Data Saved',
            'allmentor': allmentor,
        }
    else:
        dict = {
            'message': 'Unsuccessful',
            'allmentor': allmentor,
        }

    return render(request, 'mentor.html', dict)

def search_course(request):
    if request.method == 'GET':
        c_code = request.GET.get('c_code')
        
        if c_code:
            data = Course.objects.filter(code=c_code.upper())
        else:
            data = None
        
        context = {
            'data': data
        }
        
        return render(request, "search_course.html", context)
    
    return render(request, "search_course.html")

def search_mentor(request):
    if request.method == 'GET':
        mentor_code = request.GET.get('mentor_code')
        
        if mentor_code:
            data = Mentor.objects.filter(mentorCd=mentor_code.upper())
        else:
            data = None

        context = {
            'data': data,
        }
        return render(request, "search_mentor.html", context)

    return render(request, "search_mentor.html")

def update_course (request,code):
    data = Course.objects.get (code = code)
    dict = {
        'data' : data
    }

    return render (request, "update_course.html", dict)

def save_update_course (request, code):
    c_desc = request.POST['desc']
    data = Course.objects.get (code = code)
    data.description = c_desc
    data.save()

    return HttpResponseRedirect (reverse('course'))

def delete_course (request, code):
    data = Course.objects.get (code = code)
    data.delete()

    return HttpResponseRedirect (reverse ('course'))

