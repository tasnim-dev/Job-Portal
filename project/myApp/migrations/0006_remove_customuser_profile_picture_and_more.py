# Generated by Django 4.2.9 on 2024-01-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0005_remove_jobseekerprofile_profile_picture_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="customuser", name="profile_picture",),
        migrations.AddField(
            model_name="jobseekerprofile",
            name="profile_picture",
            field=models.ImageField(null=True, upload_to="media/profile_pic"),
        ),
        migrations.AddField(
            model_name="recruiterprofile",
            name="profile_picture",
            field=models.ImageField(null=True, upload_to="media/profile_pic"),
        ),
    ]