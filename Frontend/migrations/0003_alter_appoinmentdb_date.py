# Generated by Django 4.2.3 on 2023-09-02 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0002_alter_appoinmentdb_date_alter_appoinmentdb_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinmentdb',
            name='Date',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]