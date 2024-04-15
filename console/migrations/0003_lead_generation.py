# Generated by Django 5.0.4 on 2024-04-12 05:54

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0002_remove_regulations_terms_and_conditions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead_generation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_id', models.CharField(max_length=255)),
                ('token_generated_date', models.DateField(default=django.utils.timezone.now)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('lead_source', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_stage', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_position', models.CharField(choices=[('LEAD', 'Lead'), ('ASSIGNED_DEMO', 'AssignedDemo'), ('ATTENDED_DEMO', 'AttendedDemo'), ('REQUEST_DISCOUNT', 'RequestDiscount'), ('OPPORTUNITY', 'Opportunity'), ('ADMITTED', 'Admitted'), ('SPAM', 'Spam')], max_length=100)),
                ('lead_type', models.CharField(blank=True, max_length=255, null=True)),
                ('has_attended_demo', models.BooleanField(default=False)),
                ('request_acceptance', models.BooleanField(default=False)),
                ('plan', models.CharField(blank=True, max_length=255, null=True)),
                ('course_faculty', models.CharField(blank=True, max_length=255, null=True)),
                ('course_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount_fee', models.IntegerField(blank=True, null=True)),
                ('Final_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('admission_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('remaining_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('demo_date', models.DateField(blank=True, null=True)),
                ('batch_no', models.CharField(blank=True, max_length=255, null=True)),
                ('paymentMode', models.CharField(blank=True, max_length=255, null=True)),
                ('paymentid', models.CharField(blank=True, max_length=255, null=True)),
                ('transactionid', models.CharField(blank=True, max_length=255, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('lead_description', models.TextField(blank=True, null=True)),
                ('mql_description', models.TextField(blank=True, null=True)),
                ('sql_description', models.TextField(blank=True, null=True)),
                ('Training_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.trainingtype')),
                ('branch_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.branchmodel')),
                ('course_interested_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.course')),
                ('crn_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Register_model', to='console.register_model')),
                ('enquiry_taken_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.register_model')),
            ],
        ),
    ]