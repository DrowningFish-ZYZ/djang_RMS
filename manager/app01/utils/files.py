"""
# @Time    : 2022/10/14 15:22
# @Author  : violet
# @explain : 
"""

from django.db.models import QuerySet
import os
import pandas as pd

def user_excel(queryset: QuerySet) -> str:
    """
    使用 Pandas 将表数据转成 excel
    :param queryset: 员工数据
    :return: 文件存储路径
    """

    datas = list()
    for user in queryset:
        depart = user.depart.title
        gender = user.get_gender_display()
        data = user.__dict__
        del data['depart_id']
        del data['_state']
        data['depart'] = depart
        data['gender'] = gender
        data['create_time'] = data['create_time'].strftime('%Y/%m/%d')
        datas.append(data)

    df = pd.DataFrame(datas)
    df.to_excel(f'{os.getcwd()}/app01/static/files/user.xlsx', index=False)
    return f'{os.getcwd()}/app01/static/files/user.xlsx'