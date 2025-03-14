# Generated by Django 4.2.11 on 2024-05-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='type',
            field=models.CharField(choices=[('Фильм', 'Movie'), ('ТВ-шоу', 'Tv Show')], max_length=255, verbose_name='type'),
        ),
        migrations.AddConstraint(
            model_name='genrefilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'genre'), name='film_work_genre_idx'),
        ),
        migrations.AddConstraint(
            model_name='personfilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'person', 'role'), name='film_work_person_role_idx'),
        ),
    ]
