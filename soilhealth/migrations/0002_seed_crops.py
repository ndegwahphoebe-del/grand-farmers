
from django.db import migrations


def add_crops(apps, schema_editor):
    Crop = apps.get_model('soilhealth', 'Crop')

    crops = [
        'Avocado',
        'Beans',
        'Cabbage',
        'Coffee',
        'Maize',
        'Onions',
        'Watermelons',
        'Wheat',
    ]

    for crop_name in crops:
        Crop.objects.get_or_create(name=crop_name)


def remove_crops(apps, schema_editor):
    Crop = apps.get_model('soilhealth', 'Crop')

    crops = [
        'Avocado',
        'Beans',
        'Cabbage',
        'Coffee',
        'Maize',
        'Onions',
        'Watermelons',
        'Wheat',
    ]

    Crop.objects.filter(name__in=crops).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('soilhealth', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_crops, remove_crops),
    ]
