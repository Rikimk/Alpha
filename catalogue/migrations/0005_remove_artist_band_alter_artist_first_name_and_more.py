# Generated by Django 4.0.4 on 2022-05-06 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_artist_band_alter_artist_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='band',
        ),
        migrations.AlterField(
            model_name='artist',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_formed', models.DateField()),
                ('albums', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalogue.album')),
                ('genre', models.ManyToManyField(to='catalogue.genre')),
                ('members', models.ManyToManyField(to='catalogue.artist')),
            ],
        ),
    ]