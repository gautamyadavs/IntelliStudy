# Generated by Django 2.0.3 on 2018-03-30 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('career_picture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Contain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('level', models.CharField(choices=[('beginner', 'beginner'), ('intermediate', 'intermediate'), ('advanced', 'advanced')], default='intermediate', max_length=20)),
                ('content_picture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, default='', max_length=1000, null=True)),
                ('course_picture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(blank=True, default='', max_length=1000, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Course')),
            ],
        ),
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=2)),
                ('date_of_birth', models.DateField(null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('user_type', models.CharField(choices=[('student', 'student'), ('mentor', 'mentor')], default='student', max_length=20)),
                ('job', models.CharField(blank=True, choices=[('Intern', 'Intern'), ('Entry level (0-2 yrs)', 'Entry level (0-2 yrs)'), ('Mid level (2+ yrs)', 'Mid level (2+ yrs)'), ('Manager', 'Manager'), ('Executive', 'Executive'), ('Not Applicable', 'Not Applicable')], max_length=20, null=True)),
                ('qualification', models.CharField(blank=True, choices=[('Below High School', 'Below High School'), ('High School', 'High School'), ('Bachelor Degree', 'Bachelor Degree'), ('Master Degree', 'Master Degree'), ('Doctrate Degree', 'Doctrate Degree')], max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Content')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('beginner', 'beginner'), ('intermediate', 'intermediate'), ('advanced', 'advanced')], default='intermediate', max_length=20)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Has',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('beginner', 'beginner'), ('intermediate', 'intermediate'), ('advanced', 'advanced')], default='intermediate', max_length=20)),
                ('order', models.IntegerField(default=1)),
                ('career_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Career')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, default='', max_length=8000, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_a', models.CharField(blank=True, max_length=100, null=True)),
                ('option_b', models.CharField(blank=True, max_length=100, null=True)),
                ('option_c', models.CharField(blank=True, max_length=100, null=True)),
                ('option_d', models.CharField(blank=True, max_length=100, null=True)),
                ('option_e', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Peer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('question', models.TextField(blank=True, max_length=4000, null=True)),
                ('answer', models.TextField(blank=True, max_length=4000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('beginner', 'beginner'), ('intermediate', 'intermediate'), ('advanced', 'advanced')], default='intermediate', max_length=20)),
                ('question', models.TextField(blank=True, max_length=4000, null=True)),
                ('answer', models.CharField(blank=True, max_length=100, null=True)),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Content')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(default=-1)),
                ('progress', models.CharField(choices=[('ONGOING', 'Ongoing'), ('COMPLETED', 'Completed')], default='ONGOING', max_length=20)),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Content')),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('mentor_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='epsilon.ExtraInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('unique_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='epsilon.ExtraInfo')),
                ('level', models.CharField(choices=[('beginner', 'beginner'), ('intermediate', 'intermediate'), ('advanced', 'advanced')], default='beginner', max_length=20)),
                ('career_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='epsilon.Career')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Question'),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='content',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Course'),
        ),
        migrations.AddField(
            model_name='contain',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Group'),
        ),
        migrations.AddField(
            model_name='score',
            name='unique_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Student'),
        ),
        migrations.AddField(
            model_name='peer',
            name='unique_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Student'),
        ),
        migrations.AddField(
            model_name='message',
            name='unique_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Student'),
        ),
        migrations.AddField(
            model_name='manage',
            name='mentor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Mentor'),
        ),
        migrations.AddField(
            model_name='file',
            name='mentor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Mentor'),
        ),
        migrations.AddField(
            model_name='enroll',
            name='unique_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Student'),
        ),
        migrations.AddField(
            model_name='contain',
            name='unique_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsilon.Student'),
        ),
    ]
