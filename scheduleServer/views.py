from django.shortcuts import render
from .models import Lecture, Lecturer, FieldOfStudy
from django.core import serializers
from django.db.models import Prefetch

from django.http import JsonResponse

import json


def lectures(request, fieldId):
    print("id:" + str(fieldId))

    field = FieldOfStudy.objects.filter(id=fieldId).exists()

    if field:
        field = FieldOfStudy.objects.filter(id=fieldId).get()

        print("json field:"+field.toJson())
        x = json.loads(field.toJson())

        response = {'fieldOfStudy': json.loads(field.toJson())}


# ,'specializations':field.specializations

        Lecture.objects.all().filter(fielf_of_study=fieldId).order_by('start_time')
        # lectures = Lecture.objects.all()
        lectures = Lecture.objects.all().filter(
            fielf_of_study=fieldId).order_by('start_time')

        lectures2 = "["
        i = 0
        for y in lectures:
            lectures2 += y.toJSON()+","
            # print(str(i)+" : "+y.toJSON())

        lectures2 = lectures2[:-1]

        lectures2 += "]"

        if not lectures:
            return JsonResponse({'error': 'There is no Field of Study with that id.'}, status=422)

        x = json.loads(lectures2)

        monday = []
        tuesday = []
        wednesday = []
        thursday = []
        friday = []
        saturday = []
        sunday = []

        # for lecture in x:
        #     print("Xd: "+str(lecture['weekday']))

        for lecture in x:
            if lecture['weekday'] == 0:
                if 'weekday' in lecture:
                    del lecture['weekday']
                monday.append(lecture)

            elif lecture['weekday'] == 1:
                if 'weekday' in lecture:
                    del lecture['weekday']
                tuesday.append(lecture)

            elif lecture['weekday'] == 2:
                if 'weekday' in lecture:
                    del lecture['weekday']
                wednesday.append(lecture)

            elif lecture['weekday'] == 3:
                if 'weekday' in lecture:
                    del lecture['weekday']
                thursday.append(lecture)

            elif lecture['weekday'] == 4:
                if 'weekday' in lecture:
                    del lecture['weekday']
                friday.append(lecture)

            elif lecture['weekday'] == 5:
                if 'weekday' in lecture:
                    del lecture['weekday']
                saturday.append(lecture)

            elif lecture['weekday'] == 6:
                if 'weekday' in lecture:
                    del lecture['weekday']
                sunday.append(lecture)

        week = []
        week.append(monday)
        week.append(tuesday)
        week.append(wednesday)
        week.append(thursday)
        week.append(friday)
        week.append(saturday)
        week.append(sunday)

        week1_3 = ["1-10-2020", "12-10-2020", "26-10-2020", "9-11-2020", "23-11-2020",
                   "7-12-2020", "21-12-2020", "4-1-2021", "18-1-2021", "22-2-2021"]
        week2_4 = ["5-10-2020", "19-10-2020", "2-11-2020",
                   "16-11-2020", "30-11-2020", "14-12-2020", "11-1-2021"]
        free = [["23-12-2020", "3-1-2021"], ["8-2-2021", "14-2-2021"]]

        # week = {'monday':monday}

        # week['tuesday']=tuesday
        # week['wednesday']=wednesday
        # week['thursday']=thursday
        # week['friday']=friday
        # week['saturday']=saturday
        # week['sunday']=sunday

        # for lecture in x:
        # print(lecture)

        y = json.dumps(week)

        response['weekSchedule'] = week
        response['week1/3'] = week1_3
        response['week2/4'] = week2_4
        response['free'] = free

        return JsonResponse(response, safe=False)

    return JsonResponse({'error': 'Ther is no Field of Study with that id.'}, status=401)


def schedules(request):
    fields = FieldOfStudy.objects.all()

    jsonobject = '['
    for field in fields:
        jsonobject += field.toJson()+","

    jsonobject = jsonobject[:-1]
    jsonobject += ']'

    x = json.loads(jsonobject)
    listOfFields = []
    for y in x:
        listOfFields.append(y)

    print("xd : "+jsonobject)
    # x = list(FieldOfStudy.objects.values())

    # return render(request, 'scheduleServer/Views/schedule.html', context)

    return JsonResponse(json.loads(jsonobject), safe=False)
