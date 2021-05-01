# Generated by Django 2.2.18 on 2021-03-25 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='image_box')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
