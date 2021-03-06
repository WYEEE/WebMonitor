# Generated by Django 2.2.13 on 2021-02-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_task_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='selector',
            field=models.TextField(help_text='一行一个元素选择器，每一行的格式为：选择器名称{选择器内容}，例如：title{//*[@id="id3"]/h3/text()}。其中 url 为系统保留选择器名称，请不要使用且无法被覆盖', verbose_name='元素选择器'),
        ),
        migrations.AlterField(
            model_name='task',
            name='template',
            field=models.TextField(blank=True, help_text='可为空，自定义发送的通知内容格式，按照选择器名称进行替换，具体示例见文档', verbose_name='消息体模板'),
        ),
    ]
