# Generated by Django 2.2.5 on 2022-03-02 16:53

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movestate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=50)),
                ('Sity', models.CharField(max_length=60)),
                ('Month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=60)),
                ('Day', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')], default='', max_length=60)),
                ('description', models.TextField(blank=True, default='', max_length=500)),
            ],
            managers=[
                ('Movers', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('movestate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MoveState.Movestate')),
                ('Vehicle_Type', models.CharField(choices=[('SUV', 'SUV'), ('Truck', 'Truck'), ('Trailer', 'Trailer'), ('Big Truck', 'Big Truck'), ('Move Box', 'Move Box')], max_length=60)),
                ('Movers', models.CharField(max_length=50)),
            ],
            bases=('MoveState.movestate',),
        ),
    ]
