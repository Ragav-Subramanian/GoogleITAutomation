# Generated by Django 2.2.16 on 2020-10-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('date', models.DateField()),
                ('feedback', models.CharField(blank=True, default='', max_length=1000)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]