# Generated by Django 2.1.5 on 2019-01-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_file', models.FileField(blank=True, null=True, upload_to='uploaded_media')),
                ('is_label', models.BooleanField(default=False)),
                ('is_inhouse', models.BooleanField(default=False)),
                ('text', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Uploaded media file history',
                'verbose_name': 'Uploaded media file history',
                'ordering': ['created'],
            },
        ),
    ]
