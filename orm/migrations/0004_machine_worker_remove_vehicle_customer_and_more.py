# Generated by Django 4.0.3 on 2022-04-28 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0003_remove_vehicle_customer_vehicle_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
        migrations.AddField(
            model_name='machine',
            name='worker',
            field=models.ManyToManyField(related_name='Machine', to='orm.worker'),
        ),
    ]
