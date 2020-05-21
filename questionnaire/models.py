from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from .widgets import OtherRadioSelect
from django.utils.translation import gettext_lazy as _
from .widgets import LikertWidget, BlockedCheckbox
from .fields import MultiBlocker
from django.conf import settings

author = _('Philipp Chapkovski, HSE-Moscow')

doc = _("""
Post-experimental questionnaire for interregional project. 
""")


class Constants(BaseConstants):
    name_in_url = _('Questionnaire')
    players_per_group = None
    num_rounds = 1
    HARD_TO_SAY_CHOICE = [999, _('Затрудняюсь ответить')]

    GENDER_CHOICES = [[0, _('Мужской')], [1, _('Женский')]]
    IS_OCCUPIED_CHOICES = [[False, _('Нет')], [True, _('Да')]]

    RELATIVE_POSITION_CHOICES = [
        (1, _('...ниже, чем в среднем в вашем городе')),
        (2, _('...такой же, как в среднем в вашем городе')),
        (3, _('...выше, чем в среднем в вашем городе')),
        HARD_TO_SAY_CHOICE
    ]

    EDUCATION_CHOICES = [
        [1, _('Средняя школа')],
        [2, _('Среднее профессиональное образование')],
        [3, _('Незаконченное высшее образование')],
        [4, _('Высшее образование')],
        [5, _('Два и более диплома / Ученая степень')],
    ]

    MARITAL_STATUS_CHOICES = [
        [1, _('Не женаты/не замужем')],
        [2, _('Женаты/замужем')],
        [3, _('В отношениях, но официально не состоите в браке')],
        [4, _('Разведены')],
        [5, _('Живете отдельно от супруга/и')],
        [6, _('Вдовец/Вдова')],
        HARD_TO_SAY_CHOICE
    ]

    RELIGION_CHOICES = [
        [1, _('Не исповедую никакой религии (атеист)')],
        [2, _('Католицизм')],
        [3, _('Протестантизм')],
        [4, _('Православие')],
        [5, _('Иудаизм')],
        [6, _('Ислам')],
        [7, _('Индуизм')],
        [8, _('Буддизм')],
        [9, _('Другую религию')]
    ]

    JUSTIFIED_CHOICES = range(1, 11)

    READY_HELP_CHOICES = [
        [1, _('Да')],
        [2, _('Скорее да чем нет')],
        [3, _('Скорее нет чем да')],
        [4, _('Нет')],
        HARD_TO_SAY_CHOICE
    ]
    FEATURE_CHOICES = range(0, 11)
    FEATURE_CHOICES_1_10 = range(1, 11)

    CORRUPTION_CHOICES = [
        [1, _('Коррупция строго преследуется в соответствии с законом и подвергается публичному осуждению')],
        [2,
         _(
             'Коррупция в целом преследуется по закону и осуждается, однако иногда вовлеченным в нее людям удается найти лазейки и уйти от ответственности')],
        [3, _('Коррупция недостаточно преследуется по закону, и иногда подвергается публичному осуждению')],
        [4, _('Коррупция практически безнаказанна, и не осуждается публично')],
        HARD_TO_SAY_CHOICE
    ]

    SATIS_CHOICES = range(0, 11)
    HAPPY_CHOICES = [
        [0, _('Несчастливый человек')],
        [1, _('Счастливый человек')],
    ]

    INCOME_CHOICES = [
        [1, _('Не хватает денег даже на еду')],
        [2, _('Хватает на еду, но не хватает на покупку одежды и обуви')],
        [3, _('Хватает на одежду и обувь, но не хватает на покупку мелкой бытовой техники')],
        [4,
         _(
             'Хватает денег на небольшие покупки, но покупка дорогих вещей (компьютера, стиральной машины, холодильника) требует накоплений или кредита')],
        [5,
         _(
             'Хватает денег на покупки для дома, но на покупку машины, дачи, квартиры необходимо копить или брать кредит')],
        [6, _('Можем позволить себе любые покупки без ограничений и кредитов')]
    ]
    PARTY_CHOICES = [
        [1, _('Единая Россия')],
        [2, _('КПРФ')],
        [3, _('ЛДПР')],
        [4, _('Справедливая Россия')],
        [5, _('Яблоко')],
        [6, _('Другая партия')],
        [7, _('В России нет партии, которой  я симпатизирую')],
        [8, _('Я не интересуюсь политикой')],
        HARD_TO_SAY_CHOICE
    ]
    AgreementChoices4DNK = [
        [1, _('Совершенно согласен')],
        [2, _('Скорее согласен')],
        [3, _('Скорее не согласен')],
        [4, _('Совершенно не согласен')],
        HARD_TO_SAY_CHOICE
    ]
class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.payoff = 15
            p.participant.vars[_('questionnaire_payoff')] = p.payoff.to_real_world_currency(self.session)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    gender = models.BooleanField(initial=None,
                                 choices=Constants.GENDER_CHOICES,
                                 label=_('Ваш пол'),
                                 widget=widgets.RadioSelect())
    education = models.IntegerField(initial=None,
                                    choices=Constants.EDUCATION_CHOICES,
                                    label=_(
                                        """Какой у Вас самый высокий уровень образования, по которому Вы получили аттестат, свидетельство, диплом? """),
                                    widget=widgets.RadioSelect())

    age = models.PositiveIntegerField(label=_('Ваш возраст (полных лет)'),
                                      min=13, max=95,
                                      initial=None)

    marital_status = models.PositiveIntegerField(
        label=_('Ваш семейный статус'),
        choices=Constants.MARITAL_STATUS_CHOICES,
        widget=widgets.RadioSelect()
    )

    religion = models.PositiveIntegerField(
        label=_('Какую религию Вы исповедуете?'),
        choices=Constants.RELIGION_CHOICES,
        widget=widgets.RadioSelect
    )

    general_trust = models.PositiveIntegerField(
        label=_("""Как Вы считаете, в целом большинству людей можно доверять, или же при общении с другими людьми 
            осторожность никогда не повредит?"""),
        choices=[
            [2, _("Нужно быть очень осторожным с другими людьми")],
            [1, _("Большинству людей можно вполне доверять")],
        ],
        widget=widgets.RadioSelect()
    )

    justified_subsidies = models.IntegerField(
        label=_("""Получение государственных пособий, на которые у человека нет права"""),
        choices=Constants.JUSTIFIED_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    justified_freeride = models.IntegerField(
        label=_("""Проезд без оплаты в общественном транспорте"""),
        choices=Constants.JUSTIFIED_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    justified_theft = models.IntegerField(
        label=_("""Кража чужой собственности"""),
        choices=Constants.JUSTIFIED_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    justified_tax_evasion = models.IntegerField(
        label=_("""Неуплата налогов, если есть такая возможность"""),
        choices=Constants.JUSTIFIED_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    justified_corruption = models.IntegerField(
        label=_("""Получение взятки"""),
        choices=Constants.JUSTIFIED_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    justified_violence = models.IntegerField(
        label=_("""Применение насилия в отношении других людей"""),
        choices=Constants.JUSTIFIED_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    ready_help = models.PositiveIntegerField(
        label=_(
            """Готовы ли Вы тратить свои ресурсы на благое дело, даже если не рассчитываете ничего получить взамен?"""),
        choices=Constants.READY_HELP_CHOICES,
        widget=widgets.RadioSelect()
    )

    fairness_general = models.PositiveIntegerField(
        label='',
        choices=Constants.FEATURE_CHOICES_1_10,
        widget=LikertWidget(
            quote=_(
                'Как Вы думаете, могут ли люди в современном обществе разбогатеть только за счет других людей, или уровень благосостояния может вырасти у всех?'),
            label=_(
                'Для ответа выберите значение на шкале от 1 до 10, где 1 означает, что «люди могут разбогатеть только за счет других», а 10 означает, что «благосостояние может вырасти у всех»'),
            left=_('Люди могут разбогатеть только за счет других'),
            right=_('Благосостояние может вырасти у всех'),
        )
    )

    positive_reciprocity = models.PositiveIntegerField(
        label=(""),
        choices=Constants.FEATURE_CHOICES_1_10,
        widget=LikertWidget(
            quote=_(
                "\"Когда кто-либо мне помогает я стараюсь ответить тем же.\"  Справедливо ли это суждение в отношении Вас?"),
            label=_(
                """Для ответа выберите значение на шкале от 0 до 10,
         где 0 означает, что Вы «совершенно не готовы так поступать», а 10 означает, что Вы «готовы поступать именно так»"""
            ),
            left=_('Я совершенно не готов так поступать'),
            right=_('Я готов поступать именно так'),
        )
    )

    negative_reciprocity = models.PositiveIntegerField(
        label='',
        choices=Constants.FEATURE_CHOICES_1_10,
        widget=LikertWidget(
            quote=_(
                """"Если со мной поступили несправедливо, я отомщу при первом же удобном случае,
                даже если это дорого мне обойдется."  Справедливо ли это суждение в отношении Вас?
                """
            ),
            label=_(
                """Для ответа выберите значение на шкале от 0 до 10,
          где 0 означает, что Вы «совершенно не готовы так поступать», а 10 означает, что Вы «готовы поступать именно так»
                """
            ),
            left=_('Я совершенно не готов так поступать'),
            right=_('Я готов поступать именно так'),
        )
    )

    abuse_you = models.PositiveIntegerField(
        label=(''),
        choices=Constants.FEATURE_CHOICES_1_10,
        widget=LikertWidget(
            quote=_(
                'Как Вы думаете, если представится возможность, большинство людей попытались бы использовать вас в своих интересах, или вели бы себя порядочно?'),
            label=_(
                'Для ответа выберите значение на шкале от 0 до 10, где 0 означает, что «люди обязательно попытаются вас использовать», а 10 означает, что «люди поведут себя порядочно»'),
            left=_('Люди обязательно попытаются вас использовать'),
            right=_('Люди поведут себя порядочно'),
        )
    )

    corruption = models.PositiveIntegerField(
        label=_("""Что Вы думаете про борьбу с коррупцией в нашей стране?"""),
        choices=Constants.CORRUPTION_CHOICES,
        widget=widgets.RadioSelect()
    )

    satis = models.PositiveIntegerField(
        label="",
        choices=Constants.SATIS_CHOICES,
        widget=LikertWidget(
            quote=_(
                'Учитывая все обстоятельства, насколько Вы удовлетворены вашей жизнью в целом в эти дни?'),
            label=_(
                """ Для ответа выберите значение на шкале от 0 до 10, где 0 означает «совершенно не удовлетворен», а 10 - «полностью удовлетворен»)"""),
            left=_('Совершенно не удовлетворен'),
            right=_('Полностью удовлетворен'),
        )
    )

    happy = models.BooleanField(
        label=_("""В целом я могу сказать, что я"""),
        choices=Constants.HAPPY_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    income = models.PositiveIntegerField(
        label=_("""Какое высказывание наиболее точно описывает финансовое положение вашей семьи?"""),
        choices=Constants.INCOME_CHOICES,
        widget=widgets.RadioSelect()
    )

    honest_Russia = models.PositiveIntegerField(
        label=_(
            """В нынешней России честному человеку трудно достичь каких-то высот, занять высокое положение в обществе"""),
        choices=Constants.AgreementChoices4DNK,
        widget=widgets.RadioSelect
    )

    party_Russia = models.PositiveIntegerField(
        label=_("""Сторонником какой политической партии вы являетесь, или по крайней мере,симпатизируете ей? """),
        choices=Constants.PARTY_CHOICES,
        widget=OtherRadioSelect(other=(6, _('party_other')))
    )

    relative_position_in_region = models.IntegerField(
        label=_('Ваш средний ежемесячный доход'),
        choices=Constants.RELATIVE_POSITION_CHOICES,
        widget=widgets.RadioSelect()
    )

    is_occupied = models.BooleanField(label=_("В настоящее время вы трудоустроены?"),
                                      choices=Constants.IS_OCCUPIED_CHOICES,
                                      widget=widgets.RadioSelectHorizontal)
