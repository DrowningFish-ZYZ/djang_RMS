"""
# @Time    : 2022/10/13 20:01
# @Author  : violet
# @explain : 【Department】部门模型业务逻辑
"""

from django.shortcuts import render, redirect, reverse
from django import http
from .. import models
from .. import utils


# Create your views here.
# ==================================================== 【Department】部门模型业务逻辑 ====================================================
# GET /depart/list/
def depart_list(request: http.HttpRequest) -> http.HttpResponse:
    """ 部门列表 """
    # 1.在数据库中获取所有的部门
    # [对象, 对象]
    page = request.GET.get('page', 1)
    queryset = models.Department.objects.all()
    # 分页
    pagination, queryset = utils.page.pagination(page, queryset)
    return render(request, "depart_list.html", {'departs': queryset, 'pagination': pagination})


# GET /depart/add/
# POST /depart/add/
def depart_add(request: http.HttpRequest) -> http.HttpResponse:
    """ 添加部门 """
    if request.method == 'GET':
        # 如果是GET请求,返回部门添加界面
        return render(request, 'depart_add.html')

    elif request.method == 'POST':
        # 1.获取提交的POST数据
        title = request.POST.get('title')
        # 2.存储到数据库
        models.Department.objects.create(title=title)
        # 3.重定向回部门列表
        return redirect(reverse('depart_list'))

    return http.HttpResponse(status=405)


# GET /depart/delete/?pk=
def depart_delete(request: http.HttpRequest) -> http.HttpResponse:
    """ 删除部门 """
    # 1.获取GET上传的部门ID
    pk = request.GET.get('pk')
    # 2.构建ID删除部门
    models.Department.objects.filter(pk=pk).delete()
    # 3.跳转回部门列表
    return redirect(reverse('depart_list'))


# GET /depart/update/?pk=
# POST /depart/update/
def depart_update(request):
    """ 修改部门 """
    if request.method == 'GET':
        # 根据ID获取对应部门
        pk = request.GET.get('pk')
        depart = models.Department.objects.filter(pk=pk).first()
        return render(request, 'depart_update.html', {'depart': depart})

    elif request.method == 'POST':
        # 1.获取提交的数据
        pk = request.POST.get('pk')
        title = request.POST.get('title')
        # 2.修改数据
        models.Department.objects.filter(pk=pk).update(title=title)
        # 3.跳转至部门列表
        return redirect(reverse('depart_list'))

    return http.HttpResponse(status=405)
