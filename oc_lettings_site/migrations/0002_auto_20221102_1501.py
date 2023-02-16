from django.db import migrations


def migrate_datas(apps, schema_editor):

    try:
        OldAddress = apps.get_model('oc_lettings_site', 'Address')
        OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    except LookupError:
        return

    NewAddress = apps.get_model('lettings', 'Address')
    NewAddress.objects.bulk_create(
        NewAddress(number=old_object.number, 
                   street=old_object.street, 
                   city=old_object.city, 
                   state=old_object.state, 
                   zip_code=old_object.zip_code, 
                   country_iso_code=old_object.country_iso_code
                   )
        for old_object in OldAddress.objects.all()
    )
    
    NewLetting = apps.get_model('lettings', 'Letting')
    NewLetting.objects.bulk_create(
        NewLetting(title=old_object.title, address_id=old_object.address_id)
        for old_object in OldLetting.objects.all()
    )


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_datas),
    ]
