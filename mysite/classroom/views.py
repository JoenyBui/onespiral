from django.shortcuts import render


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