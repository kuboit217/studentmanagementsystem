from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from studentmanagementapp.models import *
import datetime
from django.utils.dateparse import parse_date


def admin_home(request):
    return render(request, 'hod_template/home_content.html')


def add_staff(request):
    return render(request, 'hod_template/add_staff_template.html')


def add_staff_save(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        try:
            user = CustomUser.objects.create_user(
                username=username, email=email, password=password, first_name=first_name, last_name=last_name, user_type=2)
            user.staffs.address = address
            user.save()
            messages.success(request, 'Successfully Add Staff')
            return HttpResponseRedirect('/add_staff')
        except:
            messages.error(request, 'Failed To Add Staff')
            return HttpResponseRedirect('/add_staff')

# views add courses


def add_courses(request):
    return render(request, 'hod_template/add_course_template.html')


def add_courses_save(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        courses = request.POST.get('course')
        try:
            course_model = Courses(course_name=courses)
            course_model.save()
            messages.success(request, 'Successfully Add Courses')
            return HttpResponseRedirect('/add_courses')
        except:
            messages.error(request, 'Failed To Add Courses')
            return HttpResponseRedirect('/add_courses')

# view add students


def add_student(request):
    courses = Courses.objects.all()
    context = {'courses': courses}
    return render(request, 'hod_template/add_student_template.html', context)


def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        start_year_str = request.POST.get('session_start')
        end_year_str = request.POST.get('session_end')
        course_id = request.POST.get('course')
        sex = request.POST.get('sex')
        start_year = parse_date(start_year_str)
        end_year = parse_date(end_year_str)
        try:
            user = CustomUser.objects.create_user(
                username=username, email=email, password=password, first_name=first_name, last_name=last_name, user_type=3)
            user.students.address = address
            user.students.session_start_year = start_year
            user.students.session_end_year = end_year
            course_obj = Courses.objects.get(id=course_id)
            user.students.course_id = course_obj
            user.students.gender = sex
            user.students.profile_pic = " "
            print(end_year)
            user.save()
            messages.success(request, 'Successfully Add Student')
            return HttpResponseRedirect('/add_student')
        except:
            messages.error(request, 'Failed To Add Student')
            return HttpResponseRedirect('/add_student') 

def add_subject(request):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type = 2)
    context = {'courses': courses , 'staffs':staffs}
    return render(request, 'hod_template/add_subject_template.html', context)
def add_subject_save(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        subject_name = request.POST.get('subject')
        course_id = request.POST.get('course')
        course_obj = Courses.objects.get(id=course_id)
        staff_id = request.POST.get('staff')
        staff_obj = CustomUser.objects.get(id=staff_id)
        try:
            subject = Subjects(subject_name=subject_name, course_id=course_obj, staff_id=staff_obj)
            #print(subject)
            subject.save()
            messages.success(request, 'Successfully Add Subject')
            return HttpResponseRedirect('/add_subject')
        except:
            messages.error(request, 'Failed To Add Subject')
            return HttpResponseRedirect('/add_subject') 

def manage_staff(request):
    staffs = Staffs.objects.all()
    context = {'staffs':staffs}
    return render(request, 'hod_template/manage_staff_template.html',context)

def manage_student(request):
    students = Students.objects.all()
    context = {'students':students}
    return render(request, 'hod_template/manage_student_template.html', context)

def manage_course(request):
    courses = Courses.objects.all()
    context = {'courses':courses}
    return render(request, 'hod_template/manage_course_template.html', context)

def manage_subject(request):
    subjects = Subjects.objects.all()
    context = {'subjects':subjects}
    return render(request, 'hod_template/manage_subject_template.html',context)