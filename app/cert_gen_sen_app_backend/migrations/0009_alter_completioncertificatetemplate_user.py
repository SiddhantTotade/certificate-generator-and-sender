# Generated by Django 4.1.3 on 2023-03-19 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cert_gen_sen_app_backend', '0008_alter_completioncertificatetemplate_template_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completioncertificatetemplate',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
