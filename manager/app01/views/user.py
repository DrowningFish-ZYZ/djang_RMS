"""
# @Time    : 2022/10/13 20:03
# @Author  : violet
# @explain : 【UserInfo】用户模型业务逻辑
"""

from django.shortcuts import render, redirect, reverse
from django import http
from .. import models
from .. import utils


# ==================================================== 【UserInfo】用户模型业务逻辑 ====================================================
# GET: /user/list/
def user_list(request: http.HttpRequest) -> http.HttpResponse:
    """ 用户列表 """
    # 分页
    page = request.GET.get('page', 1)
    queryset = models.UserInfo.objects.all()

    pagination, queryset = utils.page.pagination(page, queryset)
    return render(request, 'user_list.html', {'users': queryset, 'pagination': pagination})


# GET: /user/add/
# POST: /user/add/
def user_add(request: http.HttpRequest) -> http.HttpResponse:
    """ 添加用户【modelform 版本】 """
    if request.method == 'GET':
        form = utils.forms.UserModelForm()
        return render(request, 'model_form_add.html', {'form': form, 'title': '新建用户', 'post_url': reverse('user_add')})

    elif request.method == 'POST':
        # 用户提交数据进行数据校验
        form = utils.forms.UserModelForm(data=request.POST)
        if form.is_valid():
            # 校验成功，存储数据
            form.save()
            return redirect(reverse('user_list'))

        else:
            # 数据校验失败，给与错误信息显示
            return render(request, 'model_form_add.html', {'form': form, 'title': '新建用户', 'post_url': reverse('user_add')})

    return http.HttpResponse(status=405)


# GET: /user/update/?pk=
# POST: /user/update/
def user_update(request: http.HttpRequest) -> http.HttpResponse:
    """ 修改用户数据 """
    if request.method == 'GET':
        pk = request.GET.get('pk')
        user = models.UserInfo.objects.filter(pk=pk).first()
        form = utils.forms.UserModelForm(instance=user)
        return render(request, 'user_update.html', {'form': form, 'pk': pk})

    elif request.method == 'POST':
        user = models.UserInfo.objects.filter(pk=request.POST.get('pk')).first()
        form = utils.forms.UserModelForm(data=request.POST, instance=user)
        if form.is_valid():
            # form.instance.字段名 = 值 【除了用户输入的值，也可以给予其它数据值修改】
            form.save()
            return redirect(reverse('user_list'))
        else:
            return render(request, 'user_update.html', {'form': form})

    return http.HttpResponse(status=405)


# GET /user/delete/?pk=
def user_delete(request: http.HttpRequest) -> http.HttpResponse:
    """ 删除用户 """
    models.UserInfo.objects.filter(pk=request.GET.get('pk')).delete()
    return redirect(reverse('user_list'))


def user_excel(request: http.HttpRequest) -> http.FileResponse:
    """ 用户数据导出为 excel 表 """
    queryset = models.UserInfo.objects.all()
    path = utils.files.user_excel(queryset)

    file = open(path, 'rb')
    response = http.FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="user.xlsx"'
    return response