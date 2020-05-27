from django.test import TestCase
from .models import Solution, Lecture, Course, Task


class TestSolutionUrl(TestCase):
    def test_to_create_solution_with_wrong_url(self):
        exc = None
        c = Course(name='Python 101', description='super cool')
        l = Lecture(name='Decorators', week=5, course=c, url='https://slides.com/hackbulgaria/python101-9th-decorators')
        t = Task(name='first_decoartor', description='wrap a func', course=c, lecture=l)
        try:
            s = Solution(task=t, url='https://github.com/asd/Python101/blob/master/week02/cat.py')
            s.save()
        except Exception as e:
            exc = e

        print(s)
        self.assertIsNotNone(str(exc))
        self.assertIs(s.is_valid(), False)
