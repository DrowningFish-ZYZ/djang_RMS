from django.db import models


# Create your models here.
class Department(models.Model):
    """ 部门表 """
    title = models.CharField(verbose_name='标题', max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """ 员工表 """
    gender_choices = ((1, '男'), (2, '女'))

    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    # create_time = models.DateTimeField(verbose_name='入职时间')
    create_time = models.DateField(verbose_name='入职时间')
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)

    # 外键约束【使当前表与 Department 关联】
    #   - to: 与那张表关联
    #   - to_field: 与表中的那个列关联
    #   - 生成的 depart 会变成 depart_id
    # 当关联外表的主键某些数据被删除时, 两种处理方式
    # 1.级联删除【on_delete=models.CASCADE】
    # 2.置空【null=True, blank=True, on_delete=models.SET_NULL】
    depart = models.ForeignKey(verbose_name='部门', to='Department', to_field='id', on_delete=models.CASCADE)


class PrettyNum(models.Model):
    """ 靓号表 """
    level_choices = ((1, '一级'), (2, '二级'), (3, '三级'), (4, '四级'))
    status_choices = ((1, '使用'), (2, '未使用'))

    mobile = models.CharField(verbose_name='手机号', max_length=11)
    price = models.IntegerField(verbose_name='价格')
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=2)