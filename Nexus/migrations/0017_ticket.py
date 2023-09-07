# Generated by Django 4.2.4 on 2023-09-02 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nexus', '0016_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Open', max_length=20)),
                ('ticket_type', models.CharField(choices=[('Attendance', 'Attendance'), ('Withdrawal', 'Withdrawal'), ('Assignment Evaluation', 'Assignment Evaluation')], max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nexus.student')),
            ],
        ),
    ]
