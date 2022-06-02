# Generated by Django 2.2.5 on 2022-06-02 10:03

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_genre', models.CharField(choices=[('Science-Fiction', 'Science-Fiction'), ('Action and Adventure', 'Action and Adventure'), ('Fantasy', 'Fantasy'), ('History', 'History'), ('Horror', 'Horror'), ('Comic Book', 'Comic Book'), ('Mystery', 'Mystery'), ('Poetry', 'Poetry')], max_length=20)),
                ('book_title', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('book_description', models.CharField(max_length=100)),
                ('book_rating', models.CharField(choices=[('1/5', '1/5'), ('2/5', '2/5'), ('3/5', '3/5'), ('4/5', '4/5'), ('5/5', '5/5')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('Rating', models.CharField(max_length=100)),
                ('Source', models.CharField(max_length=100)),
            ],
            managers=[
                ('Favorite_Book', django.db.models.manager.Manager()),
            ],
        ),
    ]
