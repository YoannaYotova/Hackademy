from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from education.models import Lecture
from django.urls import reverse_lazy, reverse


def list(request):
    return render(request, 'lectures/list.html', {'lectures': Lecture.objects.all()})


def detail(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    return render(request, 'lectures/detail.html', {'lecture': lecture})


def delete_course(request, course_id):
    if request.method == 'POST':
        Lecture.objects.get(id=course_id).delete()
    return redirect(reverse('education:courses:list'))


class LectureCreateView(CreateView):
    model = Lecture
    fields = ['name', 'week', 'course', 'url']
    template_name = 'lectures/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('education:lectures:detail', kwargs={'lecture_id': self.object.id})


class LectureEditView(UpdateView):
    model = Lecture
    fields = ['name', 'week', 'course', 'url']
    template_name = 'lectures/edit.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('education:lectures:detail', kwargs={'lecture_id': self.object.id})
