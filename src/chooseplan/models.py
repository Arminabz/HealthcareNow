from multiselectfield import MultiSelectField
from django.db import models

# Create your models here.


class questions(models.Model):
    Gender = (
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Prefer not to say")

    )

    Age = (
    ("4", "18-24"),
    ("5", "25-34"),
    ("6", "35-44"),
    ("7", "45-54")
    )


    Are_you_currently_taking_pescribed_medication = (
    ("8GD", "Yes"),
    ("9", "No")
    )

    Do_you_receive_regular_physicals_and_health_screenings = (
    ("10DT", "Yes"),
    ("11", "No")
    )

    Do_you_get_routine_vaccines_or_flu_shots = (
    ("12PC", "Yes"),
    ("13", "No")
    )

    Do_you_often_come_in_for_routine_checkups = (
    ("14PC", "Yes"),
    ("15", "No")
    )

    Do_you_need_prenatal_maternity_services = (
    ("16P", "Yes"),
    ("17", "No")
    )

    Do_you_need_treatement_for_HIV_or_Aids = (
    ("18GD", "Yes"),
    ("19", "No")
    )

    Do_you_often_deal_with_skin_conditions = (
    ("20S", "Yes"),
    ("21", "No")
    )

    Do_you_often_participate_in_sports = (
    ("24IMARS", "Yes"),
    ("25", "No")
    )

    Are_you_diagnosed_with_heart_disease = (
    ("26OSSNC", "Yes"),
    ("27", "No")
    )

    Are_you_diagnosed_with_cancer = (
    ("28SNC", "Yes"),
    ("29", "No")
    )

    Are_you_pregnant = (
    ("30P", "Yes"),
    ("31", "No")
    )

    Are_you_diabetic = (
    ("32S", "Yes"),
    ("33", "No")
    )

    Do_you_need_help_with_substance_abuse = (
    ("34OSIS", "Yes"),
    ("35", "No")
    )

    Do_you_have_a_labor_intensive_job = (
    ("36IMA", "Yes"),
    ("37", "No")
    )

    Do_you_often_feel_chronic_pain = (
    ("38RS", "Yes"),
    ("39", "No")
    )

    Are_you_diagnosed_with_a_mental_health_condition = (
    ("40OSIS", "Yes"),
    ("41", "No")
    )

    Do_you_come_in_for_annual_mammogram_or_prostate_exams = (
    ("42DT", "Yes"),
    ("43", "No")
    )

    Are_you_a_candidate_for_cataract_surgery = (
    ("44OS", "Yes"),
    ("45", "No")
    )

    Are_you_a_candidate_for_knee_replacement = (
    ("46HHC", "Yes"),
    ("47", "No")
    )

    Are_you_a_candidate_for_hip_replacement = (
    ("48HHC", "Yes"),
    ("49", "No")
    )

    Gender = models.CharField(max_length=500, blank=True, choices=Gender)
    Age = models.CharField(max_length=500, blank=True, choices=Age)
    Are_you_currently_taking_pescribed_medication = models.CharField(max_length=500, blank=True, choices=Are_you_currently_taking_pescribed_medication)
    Do_you_receive_regular_physicals_and_health_screenings = models.CharField(max_length=500, blank=True, choices=Do_you_receive_regular_physicals_and_health_screenings)
    Do_you_get_routine_vaccines_or_flu_shots = models.CharField(max_length=500, blank=True, choices=Do_you_get_routine_vaccines_or_flu_shots)
    Do_you_often_come_in_for_routine_checkups = models.CharField(max_length=500, blank=True, choices=Do_you_often_come_in_for_routine_checkups)
    Do_you_need_prenatal_maternity_services = models.CharField(max_length=500, blank=True, choices=Do_you_need_prenatal_maternity_services)
    Do_you_need_treatement_for_HIV_or_Aids= models.CharField(max_length=500, blank=True, choices=Do_you_need_treatement_for_HIV_or_Aids)
    Do_you_often_deal_with_skin_conditions= models.CharField(max_length=500, blank=True, choices=Do_you_often_deal_with_skin_conditions )
    Do_you_often_participate_in_sports = models.CharField(max_length=500, blank=True, choices= Do_you_often_participate_in_sports)
    Are_you_diagnosed_with_heart_disease = models.CharField(max_length=500, blank=True, choices=Are_you_diagnosed_with_heart_disease)
    Are_you_diagnosed_with_cancer = models.CharField(max_length=500, blank=True, choices=Are_you_diagnosed_with_cancer)
    Are_you_pregnant = models.CharField(max_length=500, blank=True, choices=Are_you_pregnant)
    Are_you_diabetic = models.CharField(max_length=500, blank=True, choices=Are_you_diabetic)
    Do_you_need_help_with_substance_abuse = models.CharField(max_length=500, blank=True, choices=Do_you_need_help_with_substance_abuse)
    Do_you_have_a_labor_intensive_job= models.CharField(max_length=500, blank=True, choices=Do_you_have_a_labor_intensive_job)
    Do_you_often_feel_chronic_pain = models.CharField(max_length=500, blank=True, choices=Do_you_often_feel_chronic_pain)
    Are_you_diagnosed_with_a_mental_health_condition = models.CharField(max_length=500, blank=True, choices=Are_you_diagnosed_with_a_mental_health_condition)
    Do_you_come_in_for_annual_mammogram_or_prostate_exams = models.CharField(max_length=500, blank=True, choices=Do_you_come_in_for_annual_mammogram_or_prostate_exams)
    Are_you_a_candidate_for_cataract_surgery = models.CharField(max_length=500, blank=True, choices=Are_you_a_candidate_for_cataract_surgery)
    Are_you_a_candidate_for_knee_replacement = models.CharField(max_length=500, blank=True, choices=Are_you_a_candidate_for_knee_replacement)
    Are_you_a_candidate_for_hip_replacement = models.CharField(max_length=500, blank=True, choices=Are_you_a_candidate_for_hip_replacement)
