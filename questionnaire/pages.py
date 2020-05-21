from django.utils.translation import gettext_lazy as _
from .generic_pages import Page
from django.conf import settings


class Values(Page):
    values_fields = dict(title="""Укажите, насколько то, о чем говорится ниже, заслуживает оправдания? Для ответа выберите значение на шкале от 1 до 10, 
        где 1 означает "никогда не заслуживает оправдания", а 10 означает "всегда заслуживает оправдания".""",
                         choices=list(range(1, 11)),
                         fields=[
                             'justified_subsidies',
                             'justified_freeride',
                             'justified_theft',
                             'justified_tax_evasion',
                             'justified_corruption',
                             'justified_violence'
                         ])

    form_model = 'player'
    form_fields = [
        'justified_subsidies',
        'justified_freeride',
        'justified_theft',
        'justified_tax_evasion',
        'justified_corruption',
        'justified_violence'
    ]


class StatedPreferences1(Page):
    template_name = 'questionnaire/StatedPreferences.html'
    form_model = 'player'
    form_fields = [
        'general_trust',
        'ready_help',
        'corruption',
    ]


class StatedPreferences2_2(Page):
    template_name = 'questionnaire/StatedPreferences2.html'
    form_model = 'player'
    form_fields = [
        'fairness_general',
        'positive_reciprocity',
        'negative_reciprocity',
        'abuse_you',

    ]

    def vars_for_template(self) -> dict:
        return {
            'range1010': range(0, 11)}


class Personal1(Page):
    form_model = 'player'
    form_fields = [
        'age',
        'gender',
        'education',
        'is_occupied',
        'income',
        'relative_position_in_region',

    ]


class Personal2(Page):
    form_model = 'player'
    form_fields = [
        'satis',
        'happy',
        'honest_Russia',
        'party_Russia',
        'marital_status',
        'religion',
    ]


page_sequence = [
    Values,
    StatedPreferences1,
    StatedPreferences2_2,
    Personal1,
    Personal2
]
