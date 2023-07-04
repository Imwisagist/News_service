from os import getenv

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import migrations
from dotenv import load_dotenv


def create_superuser(apps, schema_editor):

    load_dotenv()
    Users = get_user_model()

    Users.objects.create_superuser(
        username=getenv('SU_USERNAME'),
        password=getenv('SU_PASSWORD'),
        is_active=True, is_staff=True, is_superuser=True
    )
    print(
        f"\n  Superuser {getenv('SU_USERNAME')} has been created...", end=''
    )


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]
