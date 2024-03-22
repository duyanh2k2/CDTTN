# Generated by Django 5.0.1 on 2024-03-22 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_benhnhan_datek'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhongKham',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NamePK', models.CharField(max_length=200)),
                ('SoPhong', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='benhnhan',
            name='DateK',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 19, 56, 18, 191247)),
        ),
    ]