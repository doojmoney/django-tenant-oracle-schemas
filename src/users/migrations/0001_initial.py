# Generated by Django 2.2.2 on 2019-06-24 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenants', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(help_text='Full name', max_length=50)),
                ('age', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tenant_name', models.ForeignKey(help_text='Tenant name (FK)', on_delete=django.db.models.deletion.CASCADE, to='tenants.Tenant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
