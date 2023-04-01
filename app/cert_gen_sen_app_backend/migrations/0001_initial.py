# Generated by Django 4.1.3 on 2023-04-01 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('name', models.CharField(max_length=200)),
                ('tc', models.BooleanField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
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
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(blank=True, max_length=20, null=True)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('event_department', models.CharField(blank=True, max_length=20, null=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('event_year', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_album', models.ImageField(blank=True, null=True, upload_to='image-album/')),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cert_gen_sen_app_backend.event')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(blank=True, max_length=50, null=True)),
                ('student_id', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=13)),
                ('certificate_status', models.CharField(blank=True, max_length=10, null=True)),
                ('certificate_id', models.CharField(blank=True, max_length=50, null=True)),
                ('certificate_sent_status', models.BooleanField(default=False)),
                ('student_image', models.TextField(blank=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cert_gen_sen_app_backend.event')),
            ],
        ),
        migrations.CreateModel(
            name='MeritCertificateTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.FileField(upload_to='merit-certificate-templates/')),
                ('template_img', models.ImageField(blank=True, null=True, upload_to='merit-certificate-template-images/')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xlsx_file', models.FileField(blank=True, null=True, upload_to='certificates/csv_files/')),
                ('event_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cert_gen_sen_app_backend.event')),
            ],
        ),
        migrations.CreateModel(
            name='CompletionCertificateTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.FileField(upload_to='completion-certificate-templates/')),
                ('template_img', models.ImageField(blank=True, null=True, upload_to='completion-certificate-template-images/')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
