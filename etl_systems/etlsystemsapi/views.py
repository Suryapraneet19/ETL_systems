from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django import forms
from django.core.serializers import serialize
import json
from .models import time_logs_challange_table
from rest_framework import status
# Create your views here.

def hello_world(request):
    data = {
        'message': 'Hello, World!'
    }
    return JsonResponse(data)

def fitch_all(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM time_logs_challange_table")
    rows = cursor.fetchall()
    # convert rows to a list of dictionaries
    rows_list = []
    for row in rows:
        row_dict = {}
        for i, col in enumerate(cursor.description):
            row_dict[col[0]] = row[i]
        rows_list.append(row_dict)
    
    return JsonResponse(rows_list, safe=False)

def get_all(request):
    records = time_logs_challange_table.objects.all()
    data = serialize('json', records)
    return JsonResponse(data, safe=False)
