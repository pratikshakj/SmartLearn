# Generated by Django 3.1.3 on 2021-01-10 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0031_classroom_c_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=None, max_length=255, null=True, upload_to=''),
        ),
    ]