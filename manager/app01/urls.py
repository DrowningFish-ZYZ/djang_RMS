from django.urls import path
from .views import depart, user, pretty, chart

urlpatterns = [
    # 部门管理
    path('depart/list/', depart.depart_list, name='depart_list'),
    path('depart/add/', depart.depart_add, name='depart_add'),
    path('depart/delete/', depart.depart_delete, name='depart_delete'),
    path('depart/update/', depart.depart_update, name='depart_update'),

    # 用户管理
    path('user/list/', user.user_list, name='user_list'),
    path('user/add/', user.user_add, name='user_add'),
    path('user/update/', user.user_update, name='user_update'),
    path('user/delete/', user.user_delete, name='user_delete'),
    path('user/excel/', user.user_excel, name='user_excel'),

    # 靓号管理
    path('pretty/list/', pretty.pretty_list, name='pretty_list'),
    path('pretty/add/', pretty.pretty_add, name='pretty_add'),
    path('pretty/update/', pretty.pretty_update, name='pretty_update'),
    path('pretty/delete/', pretty.pretty_delete, name='pretty_delete'),

    # 数据统计
    path('chart/user/', chart.chart_user, name='chart_user'),
    path('chart/user/bar/', chart.chart_user_bar, name='chart_user_bar'),
    path('chart/user/pie/', chart.chart_user_pie, name='chart_user_pie'),
    path('chart/user/line/', chart.chart_user_line, name='chart_user_line')
]
