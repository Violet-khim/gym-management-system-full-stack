from django.db import migrations
from django.utils import timezone

def create_initial_metadata(apps, schema_editor):
    MetaData = apps.get_model('user', 'MetaData')
    if not MetaData.objects.exists():
        MetaData.objects.create(
            lastChecked=timezone.now(),
            funds=0
        )

class Migration(migrations.Migration):
    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_metadata),
    ]