# Generated by Django 3.2.4 on 2021-08-24 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.IntegerField(primary_key=True, serialize=False)),
                ('address_line1', models.TextField()),
                ('address_line2', models.TextField()),
                ('city', models.TextField()),
                ('state', models.CharField(max_length=2)),
                ('postal_code', models.PositiveIntegerField()),
                ('country', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user_address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='addy', to='client.address')),
            ],
        ),
    ]
