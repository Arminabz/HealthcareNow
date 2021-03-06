# Generated by Django 2.2.6 on 2019-11-05 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Healthcare_Categories',
            fields=[
                ('UserID', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('UserName', models.CharField(blank=True, max_length=50)),
                ('UserEmail', models.CharField(blank=True, max_length=50)),
                ('UserPassword', models.CharField(blank=True, max_length=50)),
                ('SpecialistServices', models.IntegerField(blank=True)),
                ('PreventativeCare', models.IntegerField(blank=True)),
                ('DiagnosticTest', models.IntegerField(blank=True)),
                ('GenericDrugs', models.IntegerField(blank=True)),
                ('OutpatientSurgery', models.IntegerField(blank=True)),
                ('ImmediateMedicalAttention', models.IntegerField(blank=True)),
                ('OutpatientInpatient', models.IntegerField(blank=True)),
                ('Pregnancy', models.IntegerField(blank=True)),
                ('HomeHealthCare', models.IntegerField(blank=True)),
                ('RehabilationServices', models.IntegerField(blank=True)),
                ('SkilledNursingCare', models.IntegerField(blank=True)),
            ],
        ),
    ]
