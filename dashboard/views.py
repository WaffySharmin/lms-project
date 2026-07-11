from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# from courses.models import Course
# from enrollments.models import Enrollment


@login_required
def home(request):
    user = request.user
    if user.is_teacher():
        courses = Course.objects.filter(teacher=user)
        return render(request, 'dashboard/teacher_dashboard.html', {'courses': courses})
    elif user.is_student():
        enrollments = Enrollment.objects.filter(student=user).select_related('course')
        return render(request, 'dashboard/student_dashboard.html', {'enrollments': enrollments})
    else:
        return render(request, 'dashboard/admin_dashboard.html')
