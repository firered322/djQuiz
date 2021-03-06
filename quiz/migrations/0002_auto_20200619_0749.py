# Generated by Django 3.0.7 on 2020-06-19 02:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correct_ans',
        ),
        migrations.RemoveField(
            model_name='question',
            name='wrong_ans1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='wrong_ans2',
        ),
        migrations.AddField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question')),
            ],
        ),
    ]
