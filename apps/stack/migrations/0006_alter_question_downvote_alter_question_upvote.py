# Generated by Django 4.1.4 on 2022-12-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0005_alter_answer_downvote_alter_answer_upvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='downvote',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='upvote',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
