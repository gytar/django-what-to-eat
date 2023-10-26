# Generated by Django 4.2.3 on 2023-10-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whattoeat_api', '0004_rename_temps_de_préparation_receipe_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='Type',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='type_ingr',
            field=models.CharField(choices=[('fru', 'Fruit'), ('veg', 'Légume'), ('leg', 'Légumineuse'), ('car', 'Simili-carne'), ('sau', 'Sauce'), ('dai', 'Simili laitier'), ('sta', 'Féculent'), ('cer', 'Céréale'), ('flo', 'Farine'), ('hel', 'Aides culinaires'), ('swe', 'Sucré'), ('oth', 'Autres')], default='oth', max_length=3, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='time',
            field=models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Temps de préparation'),
        ),
    ]
