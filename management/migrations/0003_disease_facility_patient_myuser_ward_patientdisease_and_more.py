# Generated by Django 4.0.3 on 2022-03-05 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_district_localbody_state_alter_myuser_is_verified_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(choices=[('DM', 'D-32'), ('Hypertension', 'HT-58'), ('IHD', 'IDH-21'), ('COPD', 'DPOC-144'), ('Dementia', 'DM-62'), ('CVA', 'CAV-89'), ('Cancer', 'C-98'), ('CKD', 'DC-25')], default='primary_nurse', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('PHC', 'PHC'), ('CHC', 'CHC')], default='primary_nurse', max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=14)),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.ward')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('landmark', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=14)),
                ('gender', models.CharField(max_length=15)),
                ('emergency_phone_number', models.CharField(max_length=14)),
                ('expired_time', models.DateTimeField(default=None)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.facility')),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.ward')),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='ward',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='management.ward'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='PatientDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.disease')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.patient')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=14)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('relation', models.CharField(choices=[('Mother', 'Mother'), ('Father', 'Father'), ('Sibling', 'Sibling'), ('Spouse', 'Spouse'), ('Guardian', 'Guardian'), ('Friend', 'Friend'), ('Grand Parents', 'Grand Parents'), ('Not Related', 'Not Related')], default='primary_nurse', max_length=100)),
                ('address', models.TextField()),
                ('education', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('remarks', models.TextField()),
                ('is_primary', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.patient')),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='facility',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='management.facility'),
            preserve_default=False,
        ),
    ]
