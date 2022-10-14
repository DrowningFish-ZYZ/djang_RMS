"""
# @Time    : 2022/10/13 18:38
# @Author  : violet
# @explain : 工具类
"""


from django.utils.safestring import mark_safe
from django.db.models import QuerySet


def paser_fil(data: dict):
    if not data: return ''
    lis = list()
    for key, value in data.items():
        if key and value:
            lis.append(f'&{key}={value}')
    return ''.join(lis)


def pagination(
        page,
        queryset: QuerySet,
        fil=None,
        page_size=10,
        plus=5,
) -> tuple:
    """
    分页组件, 根据传输内容, 给与指定的分页样式
    :param page: 当前页
    :param queryset: 需要分页的数据
    :param fil: 追加条件, 如: {'query': 'xxx', 'age': 12}
    :param page_size: 每页显示数
    :param plus: 显示当前按钮的前后页数
    :return: pagination[自动化分页样式字符串], queryset[分完页的数据]
    """

    page = int(page)
    page_count, div = divmod(queryset.count(), page_size)
    if div: page_count += 1
    start = (page - 1) * page_size
    end = page * page_size

    if page_count < 1: return '', 0, 0

    # 只显示出当前页的前 plus 和后 plus 页
    start_page = page - plus if page - plus >= 1 else 1
    end_page = page + plus if page + plus <= page_count else page_count
    next_page = page + 1 if page + 1 <= page_count else page_count
    prev_page = page - 1 if page - 1 >= 1 else 1

    # 处理 fil
    fil = paser_fil(fil)

    # 拼接字符串
    lis = ['<ul class="pagination">',
           f'<li><a href="?page={prev_page}{fil}" aria-label="Previous"><span aria-hidden="true">«</span></a></li>']
    for i in range(start_page, end_page + 1):
        if i == page:
            lis.append(f'<li class="active"><a href="?page={i}{fil}">{i}</a></li>')
            continue
        lis.append(f'<li><a href="?page={i}{fil}">{i}</a></li>')
    lis.append(f'<li><a href="?page={next_page}{fil}" aria-label="Next"><span aria-hidden="true">»</span></a></li>')
    lis.append('</ul>')
    return mark_safe(''.join(lis)), queryset[start:end]
