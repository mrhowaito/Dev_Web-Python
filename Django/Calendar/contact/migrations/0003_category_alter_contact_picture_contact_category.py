# Generated by Django 4.2 on 2023-05-05 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_picture_contact_show_alter_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='picture',
            field=models.ImageField(blank=True, upload_to='Pictures/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='contact',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.category'),
        ),
    ]