# Generated by Django 3.2.2 on 2023-01-29 15:57

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_auto_20230129_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('adr', models.CharField(max_length=200)),
                ('est_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'college',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dept_str', models.IntegerField()),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.college')),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('marks', models.IntegerField()),
                ('age', models.IntegerField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.department')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.AlterModelManagers(
            name='employee',
            managers=[
                ('activee', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_practical', models.BooleanField(default=False)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.department')),
                ('student', models.ManyToManyField(to='app2.Student')),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('exp', models.FloatField()),
                ('qual', models.CharField(max_length=100)),
                ('college', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app2.college')),
            ],
            options={
                'db_table': 'principal',
            },
        ),
    ]