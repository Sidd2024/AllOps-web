# Generated by Django 4.0.6 on 2022-09-28 06:53

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Allops', '0007_opportunity_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mails',
            name='fields',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Internship', 'Internship'), ('Externship', 'Externship'), ('Student Program', 'Student Program'), ('Scholarship', 'Scholarship'), ('Apprenticeship', 'Apprenticeship'), ('Training', 'Training'), ('Language', 'Language'), ('Social Good', 'Social Good'), ('Open Ended', 'Open Ended'), ('Meet up', 'Meet up'), ('Conference', 'Conference'), ('Workshop', 'Workshop'), ('Machine Learning/AI', 'Machine Learning/AI'), ('Blockchain', 'Blockchain'), ('Design', 'Design'), ('Web', 'Web'), ('AR/VR', 'AR/VR'), ('Gaming', 'Gaming'), ('IoT', 'IoT'), ('DevOps', 'DevOps'), ('Cloud', 'Cloud'), ('Cybersecurity', 'Cybersecurity'), ('Mobile', 'Mobile'), ('Data', 'Data'), ('Music/Art', 'Music/Art')], max_length=241),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='interest',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Internship', 'Internship'), ('Externship', 'Externship'), ('Student Program', 'Student Program'), ('Scholarship', 'Scholarship'), ('Apprenticeship', 'Apprenticeship'), ('Training', 'Training'), ('Language', 'Language'), ('Social Good', 'Social Good'), ('Open Ended', 'Open Ended'), ('Meet up', 'Meet up'), ('Conference', 'Conference'), ('Workshop', 'Workshop'), ('Machine Learning/AI', 'Machine Learning/AI'), ('Blockchain', 'Blockchain'), ('Design', 'Design'), ('Web', 'Web'), ('AR/VR', 'AR/VR'), ('Gaming', 'Gaming'), ('IoT', 'IoT'), ('DevOps', 'DevOps'), ('Cloud', 'Cloud'), ('Cybersecurity', 'Cybersecurity'), ('Mobile', 'Mobile'), ('Data', 'Data'), ('Music/Art', 'Music/Art')], max_length=241),
        ),
    ]