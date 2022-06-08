from django.db import models

# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/#model-field-types


#1步、运行创建迁移python manage.py makemigrations
#2步、运行以将那些更改应用到数据库。python manage.py migrate
#3、在Terminal中运行上面命令

class user(models.Model):
    u_Name = models.CharField(max_length=10)
    u_PassWord = models.CharField(max_length=20)
class user(models.Model):
    u_Name = models.CharField(max_length=10)
    u_PassWord = models.CharField(max_length=20)

#models  :实体类    ORM :数据库关系形映射        1\mvc  2、mtv