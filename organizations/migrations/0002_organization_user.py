# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone
import model_utils.fields

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(to='organizations.Organization')),
                ('is_staff', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
            ],
            options={
                'verbose_name': 'Link User',
                'verbose_name_plural': 'Link Users',
            },
        ),
        migrations.AlterUniqueTogether(
            name='organizationuser',
            unique_together=set([('user_id', 'organization')]),
        ),
    ]
