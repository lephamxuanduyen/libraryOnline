# Generated by Django 4.2.8 on 2024-03-03 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_rename_pulisher_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(verbose_name='Date the book was published.'),
        ),
        migrations.AlterField(
            model_name='bookcontributor',
            name='role',
            field=models.CharField(choices=[('AUTHOR', 'Author'), ('CO_AUTHOR', 'Co-Author'), ('EDITOR', 'Editor')], max_length=20, verbose_name='The role this contributor had in the book.'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='email',
            field=models.EmailField(help_text='The contact email for the contributor.', max_length=254),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(help_text="The Publisher's website."),
        ),
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(help_text='The Book that this review is for.', on_delete=django.db.models.deletion.CASCADE, to='reviews.book'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, help_text='The date and time the review was created.'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_edited',
            field=models.DateTimeField(help_text='The date and time the review was last edited.', null=True),
        ),
    ]