# Generated by Django 5.1.4 on 2024-12-21 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='description',
            new_name='manifesto',
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='election',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='image',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='election',
            name='description',
        ),
        migrations.AddField(
            model_name='candidate',
            name='party_logo',
            field=models.ImageField(blank=True, null=True, upload_to='party_logos/'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='party_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='voter_id',
            field=models.CharField(default='default_voter_id', max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='electionresult',
            name='election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='voting.election'),
        ),
        migrations.AlterField(
            model_name='electionresult',
            name='vote_count',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='AuditLog',
        ),
    ]
