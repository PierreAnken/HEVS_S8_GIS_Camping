# Generated by Django 2.2.5 on 2020-06-05 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CampMAP', '0002_camper_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='camper',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='CampMAP.Camper'),
        ),
        migrations.AlterModelTable(
            name='camper',
            table='CampMAP_camper',
        ),
    ]
