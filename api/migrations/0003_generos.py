# Generated by Django 5.1.1 on 2024-10-21 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_usuarios_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('generos_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_genero', models.CharField(max_length=2555)),
            ],
            options={
                'db_table': 'generos',
            },
        ),
    ]