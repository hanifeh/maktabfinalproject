# Generated by Django 3.2.5 on 2021-07-31 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_alter_organization_city'),
        ('followup', '0003_alter_followup_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='followup',
            unique_together={('title', 'organization')},
        ),
    ]
