from django.db import models

# Create your models here.

class ActiveEmp(models.Manager):  # custom model manager
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class InactiveEmp(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)
    


class Employee(models.Model):   # table
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mob = models.IntegerField()
    salary = models.FloatField()
    address= models.CharField(max_length=100)
    email = models.EmailField(null=True)
    date_joined = models.DateTimeField(auto_now=True, null=True)
    date_updated = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    activee = ActiveEmp()
    in_active = InactiveEmp()
    objects = models.Manager()

    class Meta:
        db_table = "employee"

    def __str__(self):
        return f"{self.name}"

    def show_details(self):
        print(f"""---------------------------
Employee name:- {self.name}
Employee age:- {self.age}
Employee mob:- {self.mob}
Employee salary:- {self.salary}
Employee address:- {self.address}""")

    @classmethod
    def get_empdata_abv_age(cls):
        return cls.objects.filter(age__gt=25)

    @classmethod
    def get_avg_age_emp(cls):
        data = cls.objects.all().values("id", "name", "age")
        lst1 = list(map(lambda x: x['age'], list(data)))
        return sum(lst1)//len(lst1)
        
    @classmethod
    def get_act_data(cls):
        return cls.objects.filter(is_active=True)

    @classmethod
    def get_inact_data(cls):
        return cls.objects.filter(is_active=False)


class CommonClass(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class College(CommonClass):
    adr = models.CharField(max_length=200)
    est_date = models.DateField(auto_now=True)

    class Meta:
        db_table = "college"

class Principal(CommonClass):
    exp = models.FloatField()
    qual = models.CharField(max_length=100)
    college = models.OneToOneField(College, on_delete=models.CASCADE, related_name="principal")

    class Meta:
        db_table = "principal"

class Department(CommonClass):
    dept_str = models.IntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="dept")
    class Meta:
        db_table = "department"

class Student(CommonClass):
    marks = models.IntegerField()
    age = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="studs")
    class Meta:
        db_table = "student"

class Subject(CommonClass):
    is_practical = models.BooleanField(default=False)
    student = models.ManyToManyField(Student)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="subs")

    class Meta:
        db_table = "subject"



