# Generated by Django 4.2.3 on 2023-10-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whattoeat_api', '0002_alter_ingredient_image_alter_receipe_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='theme',
            field=models.CharField(choices=[('Occasion', (('su', 'Dimanche soir'), ('ch', 'Noël'), ('sv', 'Saint Valentin'), ('ea', 'Pâques'), ('ch', 'Chandeleur'), ('rm', 'Ramadan'), ('hl', 'Halloween'))), ('Localisation', (('it', 'Italien'), ('us', 'Américain'), ('jp', 'Japonnais'), ('eu', 'Européen'), ('as', 'Asiatique'), ('sa', 'Sud-Américain'), ('fr', 'Français'), ('mx', 'Mexicain'), ('en', 'Anglais'), ('bx', 'Belgique'), ('gk', 'Grecque'), ('mg', 'Maghrebin'), ('pt', 'Portugais'), ('in', 'Indien'), ('af', 'Africain'))), ('Autres', (('co', 'Comfort'), ('re', 'Recevoir'), ('bq', 'Barbecue'), ('sp', 'A la soupe !'), ('cl', 'Classiques'), ('ck', 'Cocktails'), ('sm', 'Smoothie'), ('zw', 'Zéro-déchet')))], max_length=2),
        ),
    ]
