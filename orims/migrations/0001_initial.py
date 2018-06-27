# Generated by Django 2.0.2 on 2018-06-27 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_level', models.CharField(choices=[('unit-admin', 'Unit Level Administrator'), ('branch-admin', 'Branch Level administrator'), ('dept-admin', 'Department Level Administrator'), ('ofc-admin', 'Office Level Administrator'), ('select', 'Select Administrator Level')], default='select', max_length=30)),
            ],
            options={
                'db_table': 'Administrator',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('placement_time', models.DateTimeField()),
                ('start_time', models.DateTimeField()),
                ('stop_time', models.DateTimeField()),
                ('reason', models.TextField(max_length=512)),
                ('appointment_mode', models.CharField(choices=[('pend', 'Pending'), ('canc', 'Canceled'), ('fwd', 'Forwarded'), ('conf', 'Confirmed'), ('setd', 'Settled'), ('non', 'None')], default='non', max_length=15)),
            ],
            options={
                'db_table': 'Appointment',
            },
        ),
        migrations.CreateModel(
            name='Avails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availer', models.CharField(max_length=15)),
                ('session_start', models.DateTimeField()),
                ('session_stop', models.DateTimeField()),
            ],
            options={
                'db_table': 'Avails',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=30)),
                ('branch_level', models.CharField(choices=[('main', 'Main Branch'), ('other', 'Other Branch')], default='other', max_length=15)),
                ('registration_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Branch',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_first_name', models.CharField(max_length=15)),
                ('client_last_name', models.CharField(max_length=15)),
                ('client_contact', models.CharField(max_length=15)),
                ('client_location_district', models.CharField(max_length=15)),
                ('client_location_town', models.CharField(max_length=15)),
                ('appointment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Appointment')),
            ],
            options={
                'db_table': 'Client',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=15)),
                ('office_number', models.CharField(blank=True, max_length=15, null=True)),
                ('fax_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=15, null=True)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Branch')),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=50)),
                ('department_description', models.TextField(max_length=1024)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Branch')),
            ],
            options={
                'db_table': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=15)),
                ('county', models.CharField(blank=True, max_length=15, null=True)),
                ('sub_county', models.CharField(blank=True, max_length=15, null=True)),
                ('parish', models.CharField(blank=True, max_length=15, null=True)),
                ('town', models.CharField(max_length=15)),
                ('zone', models.CharField(blank=True, max_length=15, null=True)),
                ('unique_direction', models.CharField(blank=True, max_length=15, null=True)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Branch')),
            ],
            options={
                'db_table': 'Location',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('office_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('office_name', models.CharField(max_length=50)),
                ('office_description', models.TextField(max_length=1024)),
                ('office_working_time', models.CharField(choices=[('default', 'Standard Working Dime and Days'), ('custom', 'Set Custom Working Time for office')], default='default', max_length=30)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Department')),
            ],
            options={
                'db_table': 'Office',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sch_date', models.DateField(max_length=3, verbose_name='Date when Schedule is made')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('sch_reason', models.TextField(max_length=512)),
                ('appointment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Appointment')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Office')),
            ],
            options={
                'db_table': 'Schedule',
            },
        ),
        migrations.CreateModel(
            name='ServiceUnit',
            fields=[
                ('unit_id', models.AutoField(primary_key=True, serialize=False)),
                ('unit_name', models.CharField(max_length=30)),
                ('unit_type', models.CharField(choices=[('select', 'Select Type of service unit'), ('min', 'Ministry'), ('org', 'Organization'), ('firm', 'Firm'), ('other', 'Others')], default='select', max_length=15)),
                ('unit_description', models.TextField(max_length=1024)),
                ('unit_logo', models.CharField(max_length=500)),
                ('unit_featured_image', models.CharField(max_length=500)),
                ('unit_cover_photo', models.CharField(max_length=500)),
                ('system_admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_admin.SystemAdmin')),
            ],
            options={
                'db_table': 'ServiceUnit',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('staff_first_name', models.CharField(max_length=15)),
                ('staff_last_name', models.CharField(max_length=15)),
                ('staff_profile_photo', models.CharField(max_length=512)),
                ('staff_designation', models.CharField(choices=[('system_admin', 'System administrator'), ('Official', 'Official'), ('receptionist', 'Receptionist'), ('select', 'Select Staff Designation')], default='select', max_length=15)),
                ('about_staff', models.TextField(max_length=512)),
                ('office_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Office')),
            ],
            options={
                'db_table': 'Staff',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=15, unique=True)),
                ('user_password', models.CharField(max_length=50)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Staff')),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='WorkingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(max_length=3)),
                ('work_start_time', models.TimeField(default='08:00:00:00')),
                ('work_end_time', models.TimeField(default='17:00:00:00')),
                ('office_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Office')),
            ],
            options={
                'db_table': 'WorkingTime',
            },
        ),
        migrations.AddField(
            model_name='branch',
            name='unit_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.ServiceUnit'),
        ),
        migrations.AddField(
            model_name='avails',
            name='availed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Staff'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Staff'),
        ),
        migrations.AddField(
            model_name='administrator',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Staff'),
        ),
    ]
