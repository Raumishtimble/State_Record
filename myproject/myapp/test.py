from django.test import TestCase
from myapp.models import *

class AppTestCase(TestCase):
    def setUp(self):
       state_marks=0
       all_marks=0
       f=0
       count=0
       count1=0
       state_data=state.objects.all()
       student_data=student.objects.all()
       print(state_data)
       print(student_data)
       print("State Name:-")
       for stat_name in state_data:
           print(stat_name.name)
       state_name=input("Enter the state name:-")
       for i in student_data:
           if i.state==state_name:
               print(i.subject)
               f=1
       if f==1:
               subject_name=input("Enter the subject name:-")
               for record in student_data:
                   if record.subject==subject_name:
                      count=count+1
                      all_marks+=record.Marks
                   if record.subject==subject_name and record.state==state_name:
                       count1=count1+1
                       state_marks+=record.Marks
               print("Average Marks of Student")
               print(state_name,"=",state_marks/count1)
               print("All state= ",all_marks/count)
       else:
           print("Enter valid state name")

obj =AppTestCase()
obj.setUp()