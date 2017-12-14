from django.test import TestCase

from django.contrib.auth.models import User

from classroom.models import Class, Teacher, Student


class _BootstrapTest(object):

    def setUpUser(self):
        self.u1 = User.objects.create_user(username='superman', password='ClarkKent1938')
        self.u2 = User.objects.create_user(username='lex', password='LutherCorp')
        self.u3 = User.objects.create_user(username='trump', password='CrookedHillary')
        self.u4 = User.objects.create_user(username='clinton', password='monicaMyGal')
        self.u5 = User.objects.create_user(username='pence', password='JesusFreak')
        self.u6 = User.objects.create_user(username='kaine', password='Jesuit2016')

    def setUpTeachers(self):
        self.t3 = Teacher.objects.create(user=self.u3)
        self.t4 = Teacher.objects.create(user=self.u4)

    def setupStudents(self):
        self.s4 = Student.objects.create(user=self.u4)
        self.s5 = Student.objects.create(user=self.u5)
        self.s6 = Student.objects.create(user=self.u6)


class TestClass(TestCase, _BootstrapTest):

    def setUp(self):
        self.setUpUser()
        self.setUpTeachers()
        self.setupStudents()
        self.setUpClassroom()

    def setUpClassroom(self):
        self.cls = Class()

        self.cls.name = 'Test Classroom'
        self.cls.teacher = self.t3
        self.cls.save()

        self.cls.students.add(self.s4)
        self.cls.students.add(self.s6)

    def test_num_of_students(self):
        self.assertEqual(self.cls.students.count(), 2)

    def test_teacher(self):
        self.assertEqual(self.cls.teacher.user.username, 'trump')

