# Generated by Django 2.2.6 on 2019-12-04 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chooseplan', '0012_finaloutput'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthcare_categories',
            name='formSubmissions',
        ),
        migrations.DeleteModel(
            name='finaloutput',
        ),
        migrations.DeleteModel(
            name='Healthcare_Categories',
        ),
    ]