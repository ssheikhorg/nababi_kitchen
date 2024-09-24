# Generated by Django 5.0.9 on 2024-09-24 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contactinfo_footersettings_socialgalleryimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='about_us')),
                ('description', models.TextField()),
                ('feature_1', models.CharField(blank=True, max_length=255, null=True)),
                ('feature_2', models.CharField(blank=True, max_length=255, null=True)),
                ('feature_3', models.CharField(blank=True, max_length=255, null=True)),
                ('feature_4', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'About Us Content',
                'verbose_name_plural': 'About Us Content',
            },
        ),
        migrations.AlterModelOptions(
            name='socialgalleryimage',
            options={'verbose_name_plural': 'Social Gallery Images'},
        ),
        migrations.AlterModelOptions(
            name='specialfacility',
            options={'verbose_name_plural': 'Special Facilities'},
        ),
    ]
