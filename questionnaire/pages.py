from django.utils.translation import gettext_lazy as _
from .generic_pages import Page
from django.conf import settings


class Personal1(Page):
    special_fields = ['occupation_parent',
                      'occupation_child',
                      ]
    form_model = 'player'
    form_fields = [
        'age',
        'gender',
        'education',
        'is_occupied',

    ]


class SelfDetermination(Page):
    form_model = 'player'
    form_fields = [

        'religion',
        'religion_other',

    ]


class Trust(Page):
    form_model = 'player'
    form_fields = [
        'general_trust',

    ]


class Values(Page):
    joined_fields = [{
        "title": _(
            'Ниже представлены краткие описание некоторых людей. До какой степени каждый из описанных людей похож или не похож на вас?:'),
        "fields": [
            'similar_newideas',
            'similar_wealthy',
            'similar_safety',
            'similar_hedonic',
            'similar_renowned',
            'similar_care_nearby',
            'similar_adventurous',
            'similar_correct',
            'similar_care_environment',
            'similar_tradition',
            'similar_care_society',
        ]},

        {"title": _("""Укажите, насколько то, о чем говорится ниже, заслуживает оправдания? Для ответа выберите значение на шкале от 1 до 10, 
        где 1 означает "никогда не заслуживает оправдания", а 10 означает "всегда заслуживает оправдания"."""),
         "fields": [
             'justified_subsidies',
             'justified_freeride',
             'justified_theft',
             'justified_tax_evasion',
             'justified_corruption',
             'justified_violence'
         ]},
    ]

    form_model = 'player'
    form_fields = [
        'similar_newideas',
        'similar_wealthy',
        'similar_safety',
        'similar_hedonic',
        'similar_renowned',
        'similar_care_nearby',
        'similar_adventurous',
        'similar_correct',
        'similar_care_environment',
        'similar_tradition',
        'similar_care_society',

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

        'ready_help',


    ]


class StatedPreferences2_1(Page):
    template_name = 'questionnaire/StatedPreferences2.html'
    form_model = 'player'
    form_fields = [
        'freedom',
        'competition',
        'fairness_general',

    ]

    def vars_for_template(self) -> dict:
        return {'range110': range(1, 11),
                }


class StatedPreferences2_2(Page):
    template_name = 'questionnaire/StatedPreferences2.html'
    form_model = 'player'
    form_fields = [

        'positive_reciprocity',
        'negative_reciprocity',
        'abuse_you',

    ]

    def vars_for_template(self) -> dict:
        return {
            'range1010': range(0, 11)}


class StatedPreferences3(Page):
    template_name = 'questionnaire/StatedPreferences.html'
    form_model = 'player'
    form_fields = [
        'fairness_russian',
        'separation_power',
        'independent_judiciary',
        'corruption',
        'civil_rights'
    ]




class RegionsIncome(Page):
    form_model = 'player'

    form_fields = [


        'relative_position_in_region',

    ]


class Personal2(Page):
    form_model = 'player'
    form_fields = [

        'satis',
        'happy',
        'happy_relative',
        'income',
        'honest_Russia',
        'party_Russia',
        'party_other',

        'marital_status',
        'language',
        'language_other',
        'ethnicity',
        'ethnicity_other',
        'living',
        'living_other',
        'city_size',
    ]


page_sequence = [

    Personal1,

    RegionsIncome,
    Trust,
    StatedPreferences1,
    StatedPreferences2_1,
    StatedPreferences2_2,
    StatedPreferences3,
    SelfDetermination,
    Values,
    Personal2
]
