

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(default='', max_length=60)),
                ('model', models.CharField(default='', max_length=60)),
                ('first_name', models.CharField(default='', max_length=60)),
                ('last_name', models.CharField(default='', max_length=60)),
                ('description', models.CharField(default='', max_length=300)),

            ],
        ),
    ]
