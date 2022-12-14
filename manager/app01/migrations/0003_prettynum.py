# Generated by Django 2.2.5 on 2022-10-12 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20221012_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrettyNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('level', models.SmallIntegerField(choices=[(1, '一级'), (2, '二级'), (3, '三级'), (4, '四级')], default=1, verbose_name='级别')),
                ('status', models.SmallIntegerField(choices=[(1, '使用'), (2, '未使用')], default=2, verbose_name='状态')),
            ],
        ),
    ]
