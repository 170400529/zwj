# Generated by Django 3.0.4 on 2020-03-30 09:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200322_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, null=True, verbose_name='科目名')),
                ('decs', models.CharField(default='', max_length=500, verbose_name='科目说明')),
            ],
            options={
                'verbose_name': '科目',
                'verbose_name_plural': '科目',
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('questionType', models.CharField(choices=[('single_choice', '单选'), ('judgment', '判断'), ('multiple_choice', '多选')], default='single_choice', max_length=20, verbose_name='题型')),
                ('content', models.TextField(verbose_name='题目内容')),
                ('answer', models.TextField(verbose_name='正确答案')),
                ('choice_a', models.TextField(default='A.', null=True, verbose_name='A选项')),
                ('choice_b', models.TextField(default='B.', null=True, verbose_name='B选项')),
                ('choice_c', models.TextField(default='C.', null=True, verbose_name='C选项')),
                ('choice_d', models.TextField(default='D.', null=True, verbose_name='D选项')),
                ('choice_e', models.TextField(default='E.', null=True, verbose_name='E选项')),
                ('choice_f', models.TextField(default='F.', null=True, verbose_name='F选项')),
                ('boolt', models.TextField(default='对', null=True, verbose_name='判断正确')),
                ('boolf', models.TextField(default='错', null=True, verbose_name='判断错误')),
                ('choice_num', models.IntegerField(default=4, verbose_name='选项数')),
                ('level', models.CharField(choices=[('1', 'easy'), ('3', 'difficult'), ('2', 'general')], max_length=10, null=True, verbose_name='等级')),
                ('score', models.IntegerField(default=1, verbose_name='分数')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Course', verbose_name='科目')),
            ],
            options={
                'verbose_name': '题目',
                'verbose_name_plural': '题目',
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='试卷名称')),
                ('start_time', models.DateField(default=datetime.datetime.now, verbose_name='开始时间')),
                ('single_choice_num', models.IntegerField(default=0, verbose_name='单选题数')),
                ('single_choice_score', models.IntegerField(default=0, verbose_name='单选分值')),
                ('judgment', models.IntegerField(default=0, verbose_name='判断题数')),
                ('judgment_score', models.IntegerField(default=0, verbose_name='判断分值')),
                ('multiple_choice_num', models.IntegerField(default=0, verbose_name='多选题数')),
                ('multiple_choice_score', models.IntegerField(default=0, verbose_name='多选分值')),
                ('total_num', models.IntegerField(default=0, verbose_name='总题数')),
                ('total_score', models.IntegerField(default=100, verbose_name='总分')),
                ('exam_time', models.IntegerField(default=120, verbose_name='考试时间（min）')),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Course', verbose_name='科目')),
                ('pid', models.ManyToManyField(to='users.Question')),
            ],
            options={
                'verbose_name': '试卷',
                'verbose_name_plural': '试卷',
                'db_table': 'paper',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(default='', max_length=100, verbose_name='试卷名称')),
                ('grade', models.IntegerField(default=0, verbose_name='考试成绩')),
                ('stu', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='学生')),
            ],
            options={
                'verbose_name': '成绩',
                'verbose_name_plural': '成绩',
                'db_table': 'grade',
            },
        ),
    ]
