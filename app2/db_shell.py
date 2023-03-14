from app2.models import *
from django.contrib.auth.models import User

# exec(open(r"F:\code_files_python\B8_Django\second_project\app2\db_shell.py").read())
# print(Employee.objects.get(id=1))

# e1 = Employee(name="bdvhds", age=25, mob=2456153145, salary=15315, address= "hscgh")
# e1.save()
# Employee.objects.create(name="bdds", age=27, mob=24561535, salary=1535, address= "hsch")
# print(dir(Employee.objects))

# print(Employee.objects.filter(age=25))

# obj = Employee.objects.all()
# for emp in obj:
#     emp.show_details()

# print(Employee.get_empdata_abv_age())
# 
# print(Employee.objects.filter(name__startswith="v")) 
# print(Employee.objects.filter(name__endswith="k")) 
# print(Employee.objects.exclude(name__startswith="v"))
# print(dir(Employee.objects))
# data = Employee.objects.all().values()
# print(data)
# print(Employee.objects.all().order_by("-id"))

# print(Employee.objects.filter(name__contains="h"))

# data = Employee.objects.all().values()
# # print(data)
# for emp in data:
#     print(emp, type(emp))

# data = Employee.objects.all().values("id", "name", "age")  # list of dictionaries
# # print(data)
# for emp in data:
#     print(emp)

# lst1 = list(map(lambda x: x['age'], list(data)))

# avg = sum(lst1)//len(lst1)
# print(avg)

# print(Employee.get_avg_age_emp())

# data = Employee.objects.all().values_list()   # list of tuples
# print(data)


# database changed from here
# exec(open(r"F:\code_files_python\B8_Django\second_project\app2\db_shell.py").read())

# User.objects.create_user(username="Hemant", password="Hemant@123")

# data = Employee.objects.filter(id__in=[3, 5]).update(is_active=False)

# print(Employee.objects.all())

# print(Employee.objects.filter(is_active=False))
# print(Employee.get_act_data())

# print(Employee.get_inact_data())
# print(Employee.activee.all())
# print(Employee.in_active.all())
# print(Employee.objects.all())


# exec(open(r"F:\code_files_python\B8_Django\second_project\app2\db_shell.py").read())

# clgs = College.objects.all()
# prnc = Principal.objects.all()
# depts = Department.objects.all()
# subs = Subject.objects.all()
# studs = Student.objects.all()

# print(clgs, prnc, depts, subs, studs, sep="\n")
# for dept in depts:
#     print(dept.__dict__)

# for clg in clgs:
#     print(clg.__dict__)

# for pr in prnc:
#     print(pr.__dict__)

# for sub in subs:
#     print(sub.__dict__)

# for stud in studs:
#     print(stud.__dict__)


# clgs = College.objects.all()

# clg = clgs[0]
# print(clg.principal)

#  clgs = College.objects.all()
# prnc = Principal.objects.all()
# depts = Department.objects.all()
# subs = Subject.objects.all()
# studs = Student.objects.all()

# prn_name = Principal.objects.get(id=1)

# print(prn_name.college)


# one to many relationship data fetching

# clgs = College.objects.all()
# clg = clgs[0]

# print(clg.department_set.all())



# depts = Department.objects.first()
# print(depts.college)
# dept = depts[0]
# print(depts.student_set.all())

# all_depts = Department.objects.all()
# for dept in all_depts:
#     print(f"Department name:- {dept}, students are:- {list(dept.student_set.all())}")


# s1 = Student.objects.first()
# print(s1.dept)

# studs = Student.objects.all()

# stud_dept_dict = {}
# for stud in studs:
#     stud_dept_dict[stud.name] = stud.dept.name

# print(stud_dept_dict) 
# exec(open(r"F:\code_files_python\B8_Django\second_project\app2\db_shell.py").read())


# dept = Department.objects.get(id=1)
# print(dept.studs.all())


# depts = Department.objects.all()

# for dept in depts:
#     print(dept.subs.all())

#     pass

# print([list(dept.subs.all()) for dept in depts])

# s1 = Student.objects.get(id=5)
# print(s1.dept)



# exec(open(r"F:\code_files_python\B8_Django\second_project\app2\db_shell.py").read())

# College.objects.create(name="MIT", adr="Kothrud")


# p1 =Principal(name="ABC", exp=10.5, qual="PHD in Sc.", college=College.objects.get(id=2))
# p1.save()

# p1 = Principal(name="XYZ", exp=9, qual="PHD in Maths", college_id=3)
# p1.save()



# studs = Student.objects.select_related("dept")

# for stud in studs:
#     print(stud.dept)



# first way by raw sql


# exec(open(r"F:\code_files_python\B8_Django\second_project\app2\db_shell.py").read())

# from django.db import connection

# cursor = connection.cursor()
# cursor.execute("SELECT * FROM b8_db.student;")  # raw sql
# data = cursor.fetchall()
# print(data)

# cursor = connection.cursor()
# cursor.execute("SELECT * FROM student")  # raw sql
# data = cursor.fetchmany(12)
# print(data)


# second way

# data = Student.objects.raw("SELECT * FROM student")
# for i in data:
#     print(i.name, i.age, i.marks)



# exec(open(r"F:\code_files_python\B8_Django\second_project\app2\db_shell.py").read())


# SECOND_DB = "second_db"

# data = Student.objects.using(SECOND_DB).all()
# print(data)

# c1 = College.objects.using(SECOND_DB).get(id=1)
# p1 = Principal.objects.using(SECOND_DB).create(name="Jadhav", exp= 10.5, qual="Phd", college=c1)
# d1 = Department.objects.using(SECOND_DB).create(name="IT", dept_str=120, college=c1)
# s1 = Student.objects.using(SECOND_DB).create(name="XYZ", marks=95, age=22, dept=d1)
# subj1 = Subject.objects.using(SECOND_DB).create(name="Python", is_practical=True, THIRD_DB
# THIRD_DB = "third_db"

# c1 = College.objects.using(THIRD_DB).create(name="COEP", adr="Pune")
# p1 = Principal.objects.using(THIRD_DB).create(name="Jadhav", exp= 10.5, qual="Phd", college=c1)
# d1 = Department.objects.using(THIRD_DB).create(name="IT", dept_str=120, college=c1)
# s1 = Student.objects.using(THIRD_DB).create(name="XYZ", marks=95, age=22, dept=d1)
# subj1 = Subject.objects.using(THIRD_DB).create(name="Python", is_practical=True, dept=d1)

