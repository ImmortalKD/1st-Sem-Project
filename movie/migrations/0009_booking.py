# Generated by Django 3.0

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_movie_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(null=True)),
                ('seat', models.CharField(max_length=100, null=True)),
                ('price', models.CharField(max_length=100, null=True)),
                ('ticket', models.DateField(null=True)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.Customer')),
            ],
        ),
    ]
