# Generated by Django 3.1.1 on 2020-10-18 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=80)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Chat.chat')),
            ],
        ),
    ]
