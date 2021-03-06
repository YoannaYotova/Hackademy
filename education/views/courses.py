from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse

from education.models import Course, Lecture


def list(request):
    return render(request, 'courses/list.html', {'courses': Course.objects.all()})


def detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lectures = Lecture.objects.filter(course=course)
    return render(request, 'courses/detail.html', {'course': course, 'lectures': lectures})


def delete_course(request, course_id):
    if request.method == 'POST':
        Course.objects.get(id=course_id).delete()
    return redirect(reverse('education:courses:list'))


class CourseCreateView(CreateView):
    model = Course
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'courses/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('education:courses:list')


class CourseEditView(UpdateView):
    model = Course
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'courses/edit.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('education:courses:detail', kwargs={'course_id': self.object.id})
