# Generated by Django 2.0.8 on 2018-08-21 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20180818_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=20)),
                ('apath', models.CharField(max_length=100)),
                ('fid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='auth_role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App.auth')),
            ],
        ),
        migrations.CreateModel(
            name='axf_shopcar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('isselect', models.BooleanField(default=False)),
                ('goodsid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App.axf_goods')),
            ],
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(max_length=20)),
                ('rdesc', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='role_member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App.member')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App.role')),
            ],
        ),
        migrations.AddField(
            model_name='axf_shopcar',
            name='memberid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App.member'),
        ),
        migrations.AddField(
            model_name='auth_role',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App.role'),
        ),
    ]
