# Generated by Django 4.1.3 on 2023-03-19 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cert_gen_sen_app_backend', '0011_contributedcertificates_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContributedCompletionCertificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.FileField(upload_to='contributed-completion-certificate-templates/')),
                ('template_img', models.ImageField(blank=True, null=True, upload_to='contributed-completion-certificate-template-images/')),
            ],
        ),
        migrations.CreateModel(
            name='ContributedMeritCertificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.FileField(upload_to='contributed-merit-certificate-templates/')),
                ('template_img', models.ImageField(blank=True, null=True, upload_to='contributed-merit-certificate-template-images/')),
            ],
        ),
        migrations.DeleteModel(
            name='ContributedCertificates',
        ),
    ]