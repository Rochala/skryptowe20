# Generated by Django 3.1.4 on 2020-12-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='salesstats',
            name='date',
            field=models.DateField(primary_key=True, serialize=False),
        ),
    ]