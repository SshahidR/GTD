from django.db import models
from core.models import BaseMasterModel

# Create your models here.

class TemplateContent(BaseMasterModel):
    template_name = models.CharField(max_length=256, unique=True)
    html_content = models.TextField()
    has_lines = models.BooleanField(default=False)
    template_file = models.FileField(blank=True, null=True, upload_to='html_templates')
    has_header_logo = models.BooleanField(default=False)
    has_footer_logo = models.BooleanField(default=False)
    
    no_of_lines_sections = models.PositiveSmallIntegerField(default=1)

    def __str__(self) -> str:
        return self.template_name
    

class CompanyLogo(BaseMasterModel):
    entity_type = models.CharField(max_length=240, blank=True, null=True)
    org_id = models.IntegerField( blank=True, null=True)
    entity_name = models.CharField(max_length=240, blank=True, null=True)
    header_logo = models.BinaryField(blank=True, null=True)
    footer_logo = models.BinaryField(blank=True, null=True)
    creation_date = models.DateTimeField()
    created_by = models.CharField(max_length=240)
    last_update_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=240)


class ConcReqHdr(BaseMasterModel):
    header_id = models.IntegerField( blank=True, null=True)
    request_id = models.IntegerField( blank=True, null=True)
    phase_code = models.CharField(max_length=5, blank=True, null=True)
    status_code = models.CharField(max_length=5, blank=True, null=True)
    request_date = models.DateField(blank=True, null=True)
    requested_by = models.IntegerField( blank=True, null=True)
    requested_start_date  = models.DateField(blank=True, null=True)
    responsibility_application_id = models.IntegerField( blank=True, null=True)
    responsibility_id = models.IntegerField( blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.IntegerField( blank=True, null=True)
    last_update_login = models.IntegerField( blank=True, null=True)
    actual_start_date = models.DateField(blank=True, null=True)
    actual_completion_date = models.DateField(blank=True, null=True)
    argument_text  = models.CharField(max_length=240, blank=True, null=True)
    request_type = models.CharField(max_length=5, blank=True, null=True)
    program_application_id = models.IntegerField( blank=True, null=True)
    concurrent_program_id= models.IntegerField( blank=True, null=True)
    program_short_name = models.CharField(max_length=30, blank=True, null=True)
    program  = models.TextField(blank=True, null=True)
    requestor = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=240, blank=True, null=True)
    user_concurrent_program_name = models.CharField(max_length=240, blank=True, null=True)
    refresh_date = models.DateField(blank=True, null=True)
    time_taken= models.IntegerField( blank=True, null=True)
    request_status = models.CharField(max_length=240, blank=True, null=True)
    org_id= models.IntegerField( blank=True, null=True)


class ConcReqDtl(BaseMasterModel):
    header_id = models.IntegerField( blank=True, null=True)
    parameter_name = models.CharField(max_length=240, blank=True, null=True)
    prompt = models.CharField(max_length=240, blank=True, null=True)
    parameter_value = models.CharField(max_length=240, blank=True, null=True)
    column_seq_num = models.IntegerField( blank=True, null=True)


class ConcProgMaster(BaseMasterModel):
    application_id = models.IntegerField( blank=True, null=True)
    application_short_name = models.CharField(max_length=50, blank=True, null=True)
    concurrent_program_id = models.IntegerField( blank=True, null=True)
    user_concurrent_program_name = models.CharField(max_length=240, blank=True, null=True)
    concurrent_program_name = models.CharField(max_length=30, blank=True, null=True)
    column_seq_num = models.IntegerField( blank=True, null=True)
    end_user_column_name = models.CharField(max_length=30, blank=True, null=True)
    prompt = models.CharField(max_length=100, blank=True, null=True)
    required_flag = models.CharField(max_length=5, blank=True, null=True)
    display_flag = models.CharField(max_length=5, blank=True, null=True)
    flex_value_set_id = models.IntegerField( blank=True, null=True)
    flex_value_set_name = models.CharField(max_length=60, blank=True, null=True)
    default_type = models.CharField(max_length=5, blank=True, null=True)
    default_value = models.CharField(max_length=2000, blank=True, null=True)
    default_format = models.CharField(max_length=30, blank=True, null=True)
    validation_type = models.CharField(max_length=100, blank=True, null=True)
    select_query = models.CharField(max_length=4000, blank=True, null=True)
    pg_sql_query = models.CharField(max_length=4000, blank=True, null=True)
    date_format = models.CharField(max_length=4000, blank=True, null=True)

# class FlexValueSets(models.Model):
#     flex_value_set_id = models.IntegerField()
#     flex_value_set_name = models.CharField(max_length=60)
#     last_update_date = models.DateField()
#     last_updated_by = models.BigIntegerField()
#     creation_date = models.DateField()
#     created_by = models.BigIntegerField()
#     last_update_login = models.BigIntegerField()
#     validation_type = models.CharField(max_length=1)
#     protected_flag = models.CharField(max_length=1)
#     security_enabled_flag = models.CharField(max_length=1)
#     longlist_flag = models.CharField(max_length=1)
#     format_type = models.CharField(max_length=1)
#     maximum_size = models.IntegerField()
#     alphanumeric_allowed_flag = models.CharField(max_length=1)
#     uppercase_only_flag = models.CharField(max_length=1)
#     numeric_mode_enabled_flag = models.CharField(max_length=1)
#     description = models.CharField(max_length=240, blank=True, null=True)
#     dependant_default_value = models.CharField(max_length=60, blank=True, null=True)
#     dependant_default_meaning = models.CharField(max_length=240, blank=True, null=True)
#     parent_flex_value_set_id = models.IntegerField(blank=True, null=True)
#     minimum_value = models.CharField(max_length=150, blank=True, null=True)
#     maximum_value = models.CharField(max_length=150, blank=True, null=True)
#     number_precision = models.IntegerField(blank=True, null=True)
#     zd_edition_name = models.CharField(max_length=30)
#     zd_sync = models.CharField(max_length=30)
    
#     class Meta:
#         db_table  = "flex_value_sets"
# class FlexValues(models.Model):
#     row_id = models.TextField(blank=True, null=True)  # This field type is a guess.
#     flex_value_set_id = models.IntegerField()
#     flex_value_id = models.BigIntegerField()
#     flex_value = models.CharField(max_length=150)
#     last_update_date = models.DateField()
#     last_updated_by = models.BigIntegerField()
#     creation_date = models.DateField()
#     created_by = models.BigIntegerField()
#     last_update_login = models.BigIntegerField(blank=True, null=True)
#     enabled_flag = models.CharField(max_length=1)
#     summary_flag = models.CharField(max_length=1)
#     start_date_active = models.DateField(blank=True, null=True)
#     end_date_active = models.DateField(blank=True, null=True)
#     parent_flex_value_low = models.CharField(max_length=60, blank=True, null=True)
#     parent_flex_value_high = models.CharField(max_length=60, blank=True, null=True)
#     structured_hierarchy_level = models.BigIntegerField(blank=True, null=True)
#     hierarchy_level = models.CharField(max_length=30, blank=True, null=True)
#     compiled_value_attributes = models.CharField(max_length=2000, blank=True, null=True)
#     value_category = models.CharField(max_length=30, blank=True, null=True)
#     attribute1 = models.CharField(max_length=240, blank=True, null=True)
#     attribute2 = models.CharField(max_length=240, blank=True, null=True)
#     attribute3 = models.CharField(max_length=240, blank=True, null=True)
#     attribute4 = models.CharField(max_length=240, blank=True, null=True)
#     attribute5 = models.CharField(max_length=240, blank=True, null=True)
#     attribute6 = models.CharField(max_length=240, blank=True, null=True)
#     attribute7 = models.CharField(max_length=240, blank=True, null=True)
#     attribute8 = models.CharField(max_length=240, blank=True, null=True)
#     attribute9 = models.CharField(max_length=240, blank=True, null=True)
#     attribute10 = models.CharField(max_length=240, blank=True, null=True)
#     attribute11 = models.CharField(max_length=240, blank=True, null=True)
#     attribute12 = models.CharField(max_length=240, blank=True, null=True)
#     attribute13 = models.CharField(max_length=240, blank=True, null=True)
#     attribute14 = models.CharField(max_length=240, blank=True, null=True)
#     attribute15 = models.CharField(max_length=240, blank=True, null=True)
#     attribute16 = models.CharField(max_length=240, blank=True, null=True)
#     attribute17 = models.CharField(max_length=240, blank=True, null=True)
#     attribute18 = models.CharField(max_length=240, blank=True, null=True)
#     attribute19 = models.CharField(max_length=240, blank=True, null=True)
#     attribute20 = models.CharField(max_length=240, blank=True, null=True)
#     attribute21 = models.CharField(max_length=240, blank=True, null=True)
#     attribute22 = models.CharField(max_length=240, blank=True, null=True)
#     attribute23 = models.CharField(max_length=240, blank=True, null=True)
#     attribute24 = models.CharField(max_length=240, blank=True, null=True)
#     attribute25 = models.CharField(max_length=240, blank=True, null=True)
#     attribute26 = models.CharField(max_length=240, blank=True, null=True)
#     attribute27 = models.CharField(max_length=240, blank=True, null=True)
#     attribute28 = models.CharField(max_length=240, blank=True, null=True)
#     attribute29 = models.CharField(max_length=240, blank=True, null=True)
#     attribute30 = models.CharField(max_length=240, blank=True, null=True)
#     attribute31 = models.CharField(max_length=240, blank=True, null=True)
#     attribute32 = models.CharField(max_length=240, blank=True, null=True)
#     attribute33 = models.CharField(max_length=240, blank=True, null=True)
#     attribute34 = models.CharField(max_length=240, blank=True, null=True)
#     attribute35 = models.CharField(max_length=240, blank=True, null=True)
#     attribute36 = models.CharField(max_length=240, blank=True, null=True)
#     attribute37 = models.CharField(max_length=240, blank=True, null=True)
#     attribute38 = models.CharField(max_length=240, blank=True, null=True)
#     attribute39 = models.CharField(max_length=240, blank=True, null=True)
#     attribute40 = models.CharField(max_length=240, blank=True, null=True)
#     attribute41 = models.CharField(max_length=240, blank=True, null=True)
#     attribute42 = models.CharField(max_length=240, blank=True, null=True)
#     attribute43 = models.CharField(max_length=240, blank=True, null=True)
#     attribute44 = models.CharField(max_length=240, blank=True, null=True)
#     attribute45 = models.CharField(max_length=240, blank=True, null=True)
#     attribute46 = models.CharField(max_length=240, blank=True, null=True)
#     attribute47 = models.CharField(max_length=240, blank=True, null=True)
#     attribute48 = models.CharField(max_length=240, blank=True, null=True)
#     attribute49 = models.CharField(max_length=240, blank=True, null=True)
#     attribute50 = models.CharField(max_length=240, blank=True, null=True)
#     flex_value_meaning = models.CharField(max_length=150)
#     description = models.CharField(max_length=240, blank=True, null=True)
#     attribute_sort_order = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         db_table  = "flex_values"

class concreqhdr_stg(BaseMasterModel):
    header_id = models.IntegerField( blank=True, null=True)
    request_id = models.IntegerField( blank=True, null=True)
    phase_code = models.CharField(max_length=5, blank=True, null=True)
    status_code = models.CharField(max_length=5, blank=True, null=True)
    request_date = models.DateTimeField(blank=True, null=True)
    requested_by = models.IntegerField( blank=True, null=True)
    requested_start_date  = models.DateField(blank=True, null=True)
    responsibility_application_id = models.IntegerField( blank=True, null=True)
    responsibility_id = models.IntegerField( blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.IntegerField( blank=True, null=True)
    last_update_login = models.IntegerField( blank=True, null=True)
    actual_start_date = models.DateTimeField(blank=True, null=True)
    actual_completion_date = models.DateTimeField(blank=True, null=True)
    argument_text  = models.CharField(max_length=240, blank=True, null=True)
    request_type = models.CharField(max_length=5, blank=True, null=True)
    program_application_id = models.IntegerField( blank=True, null=True)
    concurrent_program_id= models.IntegerField( blank=True, null=True)
    program_short_name = models.CharField(max_length=30, blank=True, null=True)
    program  = models.TextField(blank=True, null=True)
    requestor = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=240, blank=True, null=True)
    user_concurrent_program_name = models.CharField(max_length=240, blank=True, null=True)
    refresh_date = models.DateField(blank=True, null=True)
    time_taken= models.IntegerField( blank=True, null=True)
    request_status = models.CharField(max_length=240, blank=True, null=True)
    output_file = models.BinaryField(blank=True, null=True)
    output_file_extn = models.CharField(max_length=30, blank=True, null=True)
    org_id= models.IntegerField( blank=True, null=True)


class concreqdtl_stg(BaseMasterModel):
    header_id = models.IntegerField( blank=True, null=True)
    parameter_name = models.CharField(max_length=240, blank=True, null=True)
    prompt = models.CharField(max_length=240, blank=True, null=True)
    parameter_value = models.CharField(max_length=240, blank=True, null=True)
    column_seq_num = models.IntegerField( blank=True, null=True)