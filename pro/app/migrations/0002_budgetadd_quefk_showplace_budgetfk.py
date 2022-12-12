# Generated by Django 4.1.4 on 2022-12-12 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetadd',
            name='quefk',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.questionslist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='showplace',
            name='budgetfk',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.budgetadd'),
            preserve_default=False,
        ),
    ]
