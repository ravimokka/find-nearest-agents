from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import datetime
from django.views import View
from .models import *
import json
from django.core import serializers
from random import randrange

from .all_places import all_places_Info

import csv
from csv import DictReader
from collections import OrderedDict
from math import cos, sqrt
import random
import sys
import math

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'agents.tsv')

class LoadHomePage(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        orm_data = AllPlacesInfo.objects.all().delete()
        orm_data = AllPlacesInfo.objects.all()
        data = serializers.serialize('json', orm_data)
        res_data = json.loads(data)
        if res_data:
            pass
        else:
            place_info = all_places_Info()
            for i in place_info:
                place = i['place_name']
                distance = randrange(100)
                data = AllPlacesInfo.objects.create(place_name=place, distance=distance)
                data.save()
        return render(request, 'home_page.html')


class fetchAllPlace(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        d = AllPlacesInfo.objects.all()
        data = serializers.serialize('json', d)
        user_data = json.loads(data)
        place_data = []
        for i in user_data:
            print(i)
            place_data.append({'place_id': i['pk'], 'place_name': i['fields']['place_name'],
                               'distance': i['fields']['distance']})
        return JsonResponse({'data': place_data})


class findNearestAgents(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        req_data = request.body
        request_data = json.loads(req_data)
        ag_dis = request_data['ag_dis']
        agents_list = []
        with open(my_file, 'r') as f:
            read_tsv = csv.reader(f, delimiter="\t")
            headers = next(read_tsv)
            latitude = 1.99
            longitude = 93.78
            la_ln = ['latitude', 'longitude']
            headers.extend(la_ln)
            l = 0
            print(headers)
            for row in read_tsv:
                hex1 = '%012x' % random.randrange(16 ** 12)
                # dec_lat = random.random() / 100
                dec_lat = randrange(2500)
                dec_lon = randrange(100)
                lat = latitude + dec_lat
                lon = longitude + dec_lon
                lat_lon = [lat, lon]
                row.extend(lat_lon)
                agents_list.append(dict(zip(headers, row)))
        find_list = []
        for i in agents_list:
            # res_key, res_val = min(i.items(), key=lambda x: abs(val - x[1]))
            # print(res_key)
            dis = i['latitude']
            if dis <= int(ag_dis):
                find_list.append(i)
            else:
                pass
        return JsonResponse({'data': find_list})


