# Generated by Django 4.0.1 on 2022-02-14 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_board_main', '0002_remove_subscription_email'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together={('user', 'job')},
        ),
    ]