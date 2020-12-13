from django.db import models
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
import datetime


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, type(datetime)):
            return str(obj)
        return super().default(obj)

class Specialization(models.Model):
    name = models.CharField(max_length=200,null=True)
    short_name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name+" - "+self.short_name

    def toJson(self):
        return '{"id":'+str(self.id)+',"name":"'+self.name+'","short":"'+self.short_name+'"}'

class Groups(models.Model):
    group = models.IntegerField()

    def __str__(self):
        return str(self.group)
    
    def toJson(self):
        return self

class FieldOfStudy(models.Model):
    SEMESTER = (
        (1,'1 year 1 semester'),
        (2,'1 year 2 semester'),
        (3,'2 year 1 semester'),
        (4,'2 year 2 semester'),
        (5,'3 year 1 semester'),
        (6,'3 year 2 semester'),
        (7,'4 year 1 semester',),
    )

    semester = models.IntegerField(blank=True, null=True,choices = SEMESTER)
    name = models.CharField(max_length=200,null=True,blank=True)
    year = models.CharField(max_length=200,null=True,blank=True)
    specializations = models.ManyToManyField(Specialization)
    groups = models.ManyToManyField(Groups,related_name="field1")
    laboratories = models.ManyToManyField(Groups,related_name="field2")

    def __str__(self):
        specsJson = []
        for spec in self.specializations.all():
            specsJson.append(spec.toJson())

        return self.name+" "+self.get_semester_display()+" "+json.dumps(specsJson)

    def toJson(self):

        specialization = '"specializations": ['
        for spec in self.specializations.all():
            specialization+=spec.toJson()
            specialization+=","
        specialization = specialization[:-1]
        specialization+="]"

        # print(self.groups.all())

        group = '"groups": ['
        for grou in self.groups.all():
            group+=str(grou.toJson())
            group+=","
        group = group[:-1]
        group+="]"

        laboratories = '"laboratories": ['
        for lab in self.laboratories.all():
            laboratories+=str(lab.toJson())
            laboratories+=","
        laboratories = laboratories[:-1]
        laboratories+="]"

        return '{"id":'+str(self.id)+',"name":"'+self.name+'","semester":'+str(self.semester)+',"year":"'+self.year+'",'+specialization+','+group+','+laboratories+'}'

class Building(models.Model):
    hall = models.IntegerField(blank=True, null=True)
    building = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return str(self.hall)+" "+self.building
    
    def toJSON(self):
        return '{"hall":'+str(self.hall)+',"building":"'+self.building+'"}'

class Lecturer(models.Model):
    ACADEMIC_TITLE = (
        ('dr','dr'),
        ('dr inż.','dr inż.'),
        ('dr hab.','dr hab.'),
        ('mgr inż.','mgr inż.')
    )

    name = models.CharField(max_length=200,null=True,blank=True)
    surname = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    academic_title = models.CharField(max_length=100,null=True,choices = ACADEMIC_TITLE)

    def __str__(self):
        if self.email is not None:
            return self.academic_title+" "+self.name+" "+self.surname+" "+self.email
        else:
            return self.academic_title+" "+self.name+" "+self.surname
    
    def toJSON(self):
        json = '{"name":"'
        if self.name is not None:
            json+=self.name
        json+='","surname":"'
        if self.surname is not None:
            json+=self.surname
        json+='","email":"'
        if self.email is not None:
            json+=self.email
        json+='","academic_title":"'
        if self.academic_title is not None:
            json+=self.academic_title
        json+='"}'

        return json

class Lecture(models.Model):
    WEEKS = (
        ('all','all'),
        ('1/3','1/3'),
        ('2/4','2/4')
    )
    WEEKDAY = (
        (0,'Monday'),
        (1,'Tuesday'),
        (2,'Wednesday'),
        (3,'Thursday'),
        (4,'Friday'),
        (5,'Saturday'),
        (6,'Sunday'),
    )

    weekday = models.IntegerField(blank=True, null=True,choices = WEEKDAY)
    weeks = models.CharField(max_length=100,null=True,choices = WEEKS)

    name = models.CharField(max_length=200,null=True,blank=True)

    start_time = models.TimeField(auto_now=False, auto_now_add=False)

    end_time = models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)



    building = models.ForeignKey(Building,null=True,blank=True, on_delete = models.SET_NULL)
    lecturer = models.ForeignKey(Lecturer,null=True, on_delete = models.SET_NULL)

    fielf_of_study = models.ForeignKey(FieldOfStudy,null=True,blank=True, on_delete = models.SET_NULL)

    group = models.ForeignKey(Groups,null=True,blank=True, on_delete = models.SET_NULL,related_name="lecture_group")
    laboratories = models.ForeignKey(Groups,null=True,blank=True, on_delete = models.SET_NULL,related_name="lecture_laboratories")

    specialization = models.ForeignKey(Specialization,null=True,blank=True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.get_weekday_display()+" | "+self.name+" | "+self.start_time.strftime("%H:%M")+" | "+self.end_time.strftime("%H:%M")+" | "+str(self.lecturer)

    def toJSON(self):
        

        group = ',"group":'
        if self.group is not None:
            group+=str(self.group)
        else:
            group=''

        laboratories = ',"laboratories":'
        if self.laboratories is not None:
            laboratories+=str(self.laboratories)
        else:
            laboratories=''

        specialization = ',"specialization":'
        if self.specialization is not None:
            specialization+=str(self.specialization.id)
        else:
            specialization=''

        place = ',"place":'
        if self.building is not None:
            place+=self.building.toJSON()+''
        else:
            place=''

        return '{"weekday":'+str(self.weekday)+',"weeks":"'+self.weeks+'","name":"'+self.name+'","start_time":"'+str(self.start_time)+'","end_time":"'+str(self.end_time)+'"'+group+laboratories+specialization+place+',"lecturer":'+self.lecturer.toJSON()+'}'

        # return str(model_to_dict(self)).replace("\'","\"")
        # return json.dumps(self, cls=DjangoJSONEncoder)
        # return jsonpickle.encode(self)
        # return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
