# Generated by Django 2.2.6 on 2019-11-10 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chooseplan', '0011_auto_20191109_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='finaloutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Best_plans', models.CharField(blank=True, max_length=500)),
                ('FinalSubmissions', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chooseplan.questions')),
            ],
        ),
    ]
