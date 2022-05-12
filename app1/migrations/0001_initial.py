# Generated by Django 3.0.14 on 2022-04-30 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudAdopcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=30)),
                ('tipo_casa', models.IntegerField(choices=[(1, 'departamento'), (2, 'casa'), (3, 'casa/patio'), (4, 'parcela')], default='1')),
                ('edad', models.IntegerField(max_length=70)),
                ('region', models.IntegerField(choices=[(1, 'departamento'), (2, 'casa'), (3, 'casa/patio'), (4, 'departamento'), (5, 'casa'), (6, 'casa/patio'), (7, 'departamento'), (8, 'casa'), (9, 'casa/patio'), (10, 'departamento'), (11, 'casa'), (12, 'casa/patio')], default='1')),
                ('ciudad', models.CharField(max_length=20)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
