from django.shortcuts import render
from django.views import generic


from .models import Teacher, Student, Class

# Create your views here


def index(request):
    """
    View function for home page of teacher.

    """
    # Generate counts of some of the main objects
    num_students = Student.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
            'num_students': num_students
        },
    )


class StudentListView(generic.ListView):
    model = Student
    # context_object_name = 'teacher_student_list'  # your own name for the list as a template variable
    # queryset = Student.objects.filter(title__icontains='war')[:5]  # Get 5 books containing the title war
    # template_name = 'classroom/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    #


class StudentDetailView(generic.DetailView):
    model = Student
