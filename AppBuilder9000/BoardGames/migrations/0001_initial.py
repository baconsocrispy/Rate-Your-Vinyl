from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Publisher', models.CharField(max_length=50)),
                ('Year', models.IntegerField(default=2021)),
                ('Description', models.TextField(default='Type your review here (optional)')),
                ('Thumbnail', models.CharField(blank=True, max_length=100)),
                ('Image', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
