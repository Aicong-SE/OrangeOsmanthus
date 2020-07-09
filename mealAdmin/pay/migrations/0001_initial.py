# Generated by Django 2.2.7 on 2020-03-06 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserPayInfo',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='订单编号')),
                ('order_type', models.CharField(choices=[('R', '预订'), ('A', '实时')], max_length=2, verbose_name='订单类型')),
                ('desk_number', models.IntegerField(null=True, verbose_name='桌号')),
                ('take_time', models.DateTimeField(auto_now_add=True, verbose_name='订单生效时间')),
                ('customer_phone', models.CharField(max_length=11, verbose_name='顾客电话')),
                ('order_user_number', models.IntegerField(verbose_name='订单人数')),
            ],
            options={
                'verbose_name': '订单信息表',
                'verbose_name_plural': '订单信息表',
                'db_table': 'user_info',
            },
        ),
    ]
