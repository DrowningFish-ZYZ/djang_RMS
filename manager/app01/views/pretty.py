"""
# @Time    : 2022/10/13 20:03
# @Author  : violet
# @explain : 【PrettyNum】靓号模型业务逻辑
"""

from django.shortcuts import render, redirect, reverse
from django import http
from .. import models
from .. import utils


# ==================================================== 【PrettyNum】靓号模型业务逻辑 ====================================================
# GET /pretty/list/?q=&page=
def pretty_list(request: http.HttpRequest) -> http.HttpResponse:
    # 条件查询
    fil = dict(mobile__contains=request.GET.get('q')) if request.GET.get('q') else dict()
    queryset = models.PrettyNum.objects.filter(**fil).order_by('-level')
    # 分页
    page = int(request.GET.get('page', 1))  # 当前页
    pagination, queryset = utils.page.pagination(page, queryset, fil={'q': request.GET.get('q')})
    return render(request, 'pretty_list.html', {'prettys': queryset, 'pagination': pagination})


# GET /pretty/add/?pk=
# POST /pretty/add/
def pretty_add(request: http.HttpRequest) -> http.HttpResponse:
    """ 新建号码 """
    if request.method == 'GET':
        form = utils.forms.PrettyModelForm()
        return render(request, 'model_form_add.html', {'form': form, 'title': '新建号码', 'post_url': reverse('pretty_add')})

    elif request.method == 'POST':
        form = utils.forms.PrettyModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('pretty_list'))

        else:
            return render(request, 'model_form_add.html', {'form': form, 'title': '新建号码', 'post_url': reverse('pretty_add')})

    return http.HttpResponse(status=405)


# GET /pretty/update/?pk=
# POST /pretty/update/
def pretty_update(request: http.HttpRequest) -> http.HttpResponse:
    if request.method == 'GET':
        pk = request.GET.get('pk')
        pretty = models.PrettyNum.objects.filter(pk=pk).first()
        form = utils.forms.PrettyUpdateModelForm(instance=pretty)
        return render(request, 'pretty_update.html', {'form': form, 'pk': pk})

    elif request.method == 'POST':
        pretty = models.PrettyNum.objects.filter(pk=request.POST.get('pk')).first()
        form = utils.forms.PrettyUpdateModelForm(data=request.POST, instance=pretty)
        if form.is_valid():
            form.save()
            return redirect(reverse('pretty_list'))

        else:
            return render(request, 'pretty_update.html', {'form': form, 'pk': request.POST.get('pk')})

    return http.HttpResponse(status=405)


# GET /pretty/update/?pk=
def pretty_delete(request: http.HttpRequest) -> http.HttpResponse:
    models.PrettyNum.objects.filter(pk=request.GET.get('pk')).delete()
    return redirect(reverse('pretty_list'))
