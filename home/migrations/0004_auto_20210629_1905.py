# Generated by Django 3.2.4 on 2021-06-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_slider_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('inactivate', 'inactivate')], max_length=40),
        ),
        migrations.AlterField(
            model_name='slider',
            name='rank',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='slider',
            name='status',
            field=models.BooleanField(choices=[('active', 'active'), ('inactivate', 'inactivate')], default=False),
        ),
    ]
