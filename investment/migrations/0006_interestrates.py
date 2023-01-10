# Generated by Django 4.0.5 on 2023-01-05 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0005_property_other_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(null=True)),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='investment.property')),
            ],
        ),
    ]
