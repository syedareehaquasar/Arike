# Generated by Django 4.0.3 on 2022-03-05 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='lsg_body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body_type', models.IntegerField(choices=[(1, 'Grama Panchayath'), (2, 'Block Panchayath'), (3, 'District Panchayath'), (4, 'Nagar Panchayath'), (10, 'Municipality'), (20, 'Corporation'), (50, 'Others')])),
                ('localbody_code', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.district')),
            ],
            options={
                'unique_together': {('district', 'body_type', 'name')},
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='UserProfile',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='Is Verified?'),
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.state'),
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('local_body', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.lsg_body')),
            ],
            options={
                'unique_together': {('local_body', 'name', 'number')},
            },
        ),
    ]