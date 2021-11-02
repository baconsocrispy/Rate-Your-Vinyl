# Generated by Django 2.2.5 on 2021-10-27 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KeyMaster', '0002_auto_20211027_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='genre',
            field=models.CharField(choices=[('Real Time Strategy', 'Real Time Strategy'), ('Role Playing Game', 'Role Playing Game'), ('Massive Multiplayer Online', 'Massive Multiplayer Online'), ('Turn Based Tactics', 'Turn Based Tactics'), ('Action/Adventure', 'Action/Adventure'), ('Open World', 'Open World'), ('First Person Experience', 'First Person Experience'), ('First Person Shooter', 'First Person Shooter'), ('Sports', 'Sports'), ('Simulator', 'Simulator'), ('Indie Game', 'Indie Game'), ('Virtual Reality', 'Virtual Reality'), ('Builder/Survival', 'Builder/Survival'), ('Racing', 'Racing')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='games',
            name='store_name',
            field=models.CharField(choices=[('Epic Games', 'Epic Games'), ('Battle.net', 'Battle.net'), ('Steam', 'Steam'), ('Origin', 'Origin'), ('Oculus', 'Oculus'), ('Good Old Games', 'Good Old Games'), ('Uplay', 'Uplay')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='genre',
            field=models.CharField(choices=[('Real Time Strategy', 'Real Time Strategy'), ('Role Playing Game', 'Role Playing Game'), ('Massive Multiplayer Online', 'Massive Multiplayer Online'), ('Turn Based Tactics', 'Turn Based Tactics'), ('Action/Adventure', 'Action/Adventure'), ('Open World', 'Open World'), ('First Person Experience', 'First Person Experience'), ('First Person Shooter', 'First Person Shooter'), ('Sports', 'Sports'), ('Simulator', 'Simulator'), ('Indie Game', 'Indie Game'), ('Virtual Reality', 'Virtual Reality'), ('Builder/Survival', 'Builder/Survival'), ('Racing', 'Racing')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='store_name',
            field=models.CharField(choices=[('Epic Games', 'Epic Games'), ('Battle.net', 'Battle.net'), ('Steam', 'Steam'), ('Origin', 'Origin'), ('Oculus', 'Oculus'), ('Good Old Games', 'Good Old Games'), ('Uplay', 'Uplay')], default='', max_length=50),
        ),
    ]
