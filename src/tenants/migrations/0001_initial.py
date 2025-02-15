# Generated by Django 2.2.2 on 2019-06-24 11:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tenant_name', models.CharField(blank=True, help_text='Tenant name', max_length=20, unique=True)),
            ],
        ),
    ]
