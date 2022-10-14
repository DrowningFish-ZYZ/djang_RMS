"""
# @Time    : 2022/10/13 21:02
# @Author  : violet
# @explain : 数据分析图表展示
"""

from django.shortcuts import render, redirect, reverse
from django import http
from django.db.models import Max, Min, Avg, Count
from django.db.models.functions import TruncYear
from .. import models
from datetime import datetime


def chart_user(request: http.HttpRequest) -> http.HttpResponse:
    return render(request, 'charts/user_charts.html')


def chart_user_bar(request: http.HttpRequest) -> http.HttpResponse:
    """ 用户余额汇总 """
    data: dict = models.UserInfo.objects.aggregate(Max('account'), Min('account'), Avg('account'))
    series_data = list(map(lambda value: int(value), data.values()))

    title = '用户余额统计'
    legend = ['余额']
    xAxis = {'data': ['Max', 'Min', 'Mean']}
    series = [{
        'name': '余额', 'type': 'bar', 'data': series_data,
        'itemStyle': {
            'normal': {'label': {'show': True, 'position': 'top', 'textStyle': {'color': 'black', 'fontSize': 16}}}},
    }]

    result = {
        'data': {
            'title': title,
            'legend': legend,
            'xAxis': xAxis,
            'series': series
        }
    }
    return http.JsonResponse(result, safe=False)


def chart_user_pie(request: http.HttpRequest) -> http.HttpResponse:
    """ 用户男女比例 """
    result = models.UserInfo.objects.values('gender').annotate(total=Count('id'))
    data = []
    for item in result: data.append(
        dict(value=item['total'], name=models.UserInfo.gender_choices[item['gender'] - 1][1]))

    # 封装数据
    result = {'data': data}
    return http.JsonResponse(result, safe=False)


def chart_user_line(request: http.HttpRequest) -> http.HttpResponse:
    """ 每年入职人数 """
    result = models.UserInfo.objects.annotate(year=TruncYear('create_time')).values('year').annotate(count=Count('id'))
    xAxis = []
    data = []
    for item in result:
        year: datetime = item['year']
        year_str = year.strftime('%Y')
        count = item['count']
        xAxis.append(year_str)
        data.append(count)

    result = {
        'xAxis': xAxis,
        'data': data
    }
    return http.JsonResponse(result, safe=False)
