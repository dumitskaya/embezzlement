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
from .widgets import LikertWidget

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Anya'
    players_per_group = 2
    num_rounds = 1
    budget = models.CurrencyField(initial=c(10))
    k_real = random.choice([1, 2, 3, 2, 3, 2, 3])
    tax = c(5)
    HARD_TO_SAY_CHOICE = [999, ('Затрудняюсь ответить')]

    GENDER_CHOICES = [[0, ('Мужской')], [1, ('Женский')]]
    IS_OCCUPIED_CHOICES = [[False, ('Нет')], [True, ('Да')]]
    OCCUPATION_PARENT_CHOICES = [
        [1, ("Руководители")],
        (2, ("Специалисты высшего уровня квалификации")),
        (3, ("Специалисты среднего уровня квалификации")),
        (4, ("Служащие, занятые подготовкой и оформлением документации, учетом и обслуживанием")),
        (5, ("Работники сферы обслуживания и торговли, охраны граждан и собственности")),
        (6, ("Квалифицированные работники сельского и лесного хозяйства, рыбоводства и рыболовства")),
        (7, ("Квалифицированные рабочие промышленности, строительства, транспорта и рабочие родственных занятий")),
        (8, ("Операторы производственных установок и машин, сборщики и водители")),
        (9, ("Неквалифицированные рабочие")),
        (0, ("Военнослужащие")),
    ]
    OCCUPATION_CHILD_CHOICES = [
        (11, ("Руководители высшего звена, высшие должностные лица и законодатели")),
        (12, ("Управляющие в корпоративном секторе и в других организациях")),
        (13, ("Руководители подразделений в сфере производства и специализированных сервисных услуг")),
        (14, (
            "Руководители в гостиничном и ресторанном бизнесе, розничной и оптовой торговле и родственных сферах обслуживания")),
        (21, ("Специалисты в области науки и техники")),
        (22, ("Специалисты в области здравоохранения")),
        (23, ("Специалисты в области образования")),
        (24, ("Специалисты в сфере бизнеса и администрирования")),
        (25, ("Специалисты по информационно-коммуникационным технологиям (ИКТ)")),
        (26, ("Специалисты в области права, гуманитарных областей и культуры")),
        (31, ("Специалисты-техники в области науки и техники")),
        (32, ("Средний медицинский персонал здравоохранения")),
        (33, ("Средний специальный персонал по экономической и административной деятельности")),
        (34, (
            "Средний специальный персонал в области правовой, социальной работы, культуры, спорта и родственных занятий")),
        (35, ("Специалисты-техники в области информационно-коммуникационных технологий (ИКТ)")),
        (41, ("Служащие общего профиля и обслуживающие офисную технику")),
        (42, ("Служащие сферы обслуживания населения")),
        (43, ("Служащие в сфере обработки числовой информации и учета материальных ценностей")),
        (44, ("Другие офисные служащие")),
        (51, ("Работники сферы индивидуальных услуг")),
        (52, ("Продавцы")),
        (53, ("Работники, оказывающие услуги по индивидуальному уходу")),
        (54, ("Работники служб, осуществляющих охрану граждан и собственности")),
        (61, ("Квалифицированные работники сельского хозяйства, производящие товарную продукцию")),
        (62, ("Товарные производители лесной и рыбной продукции и охотники")),
        (63, (
            "Квалифицированные работники сельского хозяйства, рыболовства, охотники и сборщики урожая, производящие продукцию для личного потребления")),
        (71, ("Рабочие, занятые в строительстве, и рабочие родственных занятий (за исключением электриков)")),
        (72, ("Рабочие, занятые в металлообрабатывающем и машиностроительном производстве, механики и ремонтники")),
        (73, (
            "Рабочие, занятые изготовлением прецизионных инструментов и приборов, рабочие художественных промыслов и полиграфического производства")),
        (74, ("Рабочие в области электротехники и электроники")),
        (75,
         (
             "Рабочие пищевой, деревообрабатывающей, текстильной и швейной промышленности и рабочие родственных занятий")),
        (81, ("Операторы промышленных установок и стационарного оборудования")),
        (82, ("Сборщики")),
        (83, ("Водители и операторы подвижного оборудования")),
        (91, ("Уборщики и прислуга")),
        (92, ("Неквалифицированные рабочие сельского и лесного хозяйства, рыбоводства и рыболовства")),
        (93, (
            "Неквалифицированные рабочие, занятые в горнодобывающей промышленности, строительстве, обрабатывающей промышленности и на транспорте")),
        (94, ("Помощники в приготовлении пищи")),
        (95, ("Уличные торговцы и другие неквалифицированные работники, оказывающие различные уличные услуги")),
        (96, ("Неквалифицированные работники по сбору мусора и другие неквалифицированные работники"))
    ]
    RELATIVE_POSITION_CHOICES = [
        (1, ('...ниже, чем в среднем в вашем городе')),
        (2, ('...такой же, как в среднем в вашем городе')),
        (3, ('...выше, чем в среднем в вашем городе')),
        HARD_TO_SAY_CHOICE
    ]
    ETHNICITY_CHOICES = [
        (1, ('Русской')),
        (2, ('Другой')),
        HARD_TO_SAY_CHOICE
    ]

    EDUCATION_CHOICES = [
        [1, ('Средняя школа')],
        [2, ('Среднее профессиональное образование')],
        [3, ('Незаконченное высшее образование')],
        [4, ('Высшее образование')],
        [5, ('Два и более диплома / Ученая степень')],
    ]
    OCCUPATION_STATUS_CHOICES = [
        [1, ('Ученик средней школы, ПТУ')],
        [2, ('Студент дневного вуза, техникума')],
        [3, ('Не работаете по состоянию здоровья, инвалид')],
        [4, ('Пенсионер и не работаете')],
        [5, ('Находитесь в декретном отпуске')],
        [6, ('Находитесь в официальном отпуске по уходу за ребенком до 3 - х лет с сохранением места')],
        [7, ('Домашняя хозяйка, ухаживаете за другими членами семьи, воспитываете детей')],
        [8, ('Временно не работаете по другим причинам и ищете работу')],
        [9, ('Временно не работаете по другим причинам и не хотите работать')],
        [14, ('Другое')],
        HARD_TO_SAY_CHOICE
    ]

    MARITAL_STATUS_CHOICES = [
        [1, ('Не женаты/не замужем')],
        [2, ('Женаты/замужем')],
        [3, ('В отношениях, но официально не состоите в браке')],
        [4, ('Разведены')],
        [5, ('Живете отдельно от супруга/и')],
        [6, ('Вдовец/Вдова')],
        HARD_TO_SAY_CHOICE
    ]
    CITY_SIZE_CHOICES = [
        (1, '< 2,000'),
        (2, '2,000 - 5,000'),
        (3, '5,001- 10,000'),
        (4, '10,001 - 20,000'),
        (5, '20,001 - 50,000'),
        (6, '50,001 - 100,000'),
        (7, '100,001 - 500,000'),
        (8, '> 500,000'),
        (9, ('1 млн. и более')),
    ]
    LIVING_CHOICES = [
        [1, ('Жилье, находящееся в собственности у Вас и/или членов Вашей семьи    ')],
        [2, ('Государственное, муниципальное, ведомственное неприватизированное жилье')],
        [3, ('Арендованное жилье')],
        [4, ('Общежитие')],
        [5, ('Другое')]
    ]
    IncrementChoices5DNK = [
        [1, ('Безусловно увеличился')],
        [2, ('Скорее увеличился')],
        [3, ('Не изменился')],
        [4, ('Скорее уменьшился')],
        [5, ('Безусловно уменьшился')],
        HARD_TO_SAY_CHOICE,
    ]
    RELIGION_CHOICES = [
        [1, ('Не исповедую никакой религии (атеист)')],
        [2, ('Католицизм')],
        [3, ('Протестантизм')],
        [4, ('Православие')],
        [5, ('Иудаизм')],
        [6, ('Ислам')],
        [7, ('Индуизм')],
        [8, ('Буддизм')],
        [9, ('Другую религию')]
    ]
    SAME_MORAL_CHOICES = [
        [1, ('Совершенно согласен')],
        [2, ('Скорее согласен')],
        [3, ('Скорее не согласен')],
        [4, ('Совершенно не согласен')],
        HARD_TO_SAY_CHOICE,
        [6, ('Без ответа, я атеист')]
    ]
    CHURCH_ATTENDANCE_CHOICES = [
        [0, ('Вообще не бываю')],
        [1, ('1 раз в месяц или реже')],
        [2, ('2-3 раза в месяц')],
        [3, ('4 раза в месяц или чаще')],
        HARD_TO_SAY_CHOICE,
        [5, ('Без ответа, я атеист')]
    ]
    JUSTIFIED_CHOICES = range(1, 11)
    RISK_CHOICES = range(0, 11)
    AGREEMENT_CHOICES = [
        [1, ('Безусловно согласия, сплоченности')],
        [2, ('Скорее согласия, сплоченности')],
        [3, ('Скорее несогласия, разобщенности')],
        [4, ('Безусловно несогласия, разобщенности')],
        HARD_TO_SAY_CHOICE
    ]
    SIMILAR_TRUST_CHOICES = [
        [1, ('Безусловно больше')],
        [2, ('Скорее больше')],
        [3, ('Одинаково')],
        [4, ('Скорее меньше')],
        [5, ('Безусловно меньше')],
        HARD_TO_SAY_CHOICE
    ]
    SELF_TRUST_CHOICES = [
        [1, ('Вы доверчивы')],
        [2, ('Вы скорее доверчивы чем нет')],
        [3, ('Вы бываете и доверчивы и недоверчивы')],
        [4, ('Вы скорее недоверчивы')],
        [5, ('Вы недоверчивы')],
        HARD_TO_SAY_CHOICE
    ]
    READY_HELP_CHOICES = [
        [1, ('Да')],
        [2, ('Скорее да чем нет')],
        [3, ('Скорее нет чем да')],
        [4, ('Нет')],
        HARD_TO_SAY_CHOICE
    ]
    FEATURE_CHOICES = range(0, 11)
    FEATURE_CHOICES_1_10 = range(1, 11)
    SEPARATION_POWER_CHOICES = [
        [1, ('Разделение властей существует, система сдержек и противовесов реально работает')],
        [2, ('Разделение властей существует, несмотря на отдельные попытки нарушить систему сдержек и противовесов')],
        [3, ('Разделение властей существует формально, на практике система сдержек и противовесов работает плохо')],
        [4, ('Разделения властей нет, система сдержек и противовесов не работает')],
        HARD_TO_SAY_CHOICE

    ]
    INDEPENDENT_JUD_CHOICES = [
        [1, ('Суды независимы от других общественных институтов и некоррумпированы')],
        [2,
         (
             'Суды в основном независимы, хотя иногда подвержены воздействию других общественных институтов и бывают случаи коррупции')],
        [3,
         (
             'Независимость судов в значительной степени подорвана: они находятся во влиянием других общественных институтов и коррупции')],
        [4, ('Независимых судов в нашей стране нет')],
        HARD_TO_SAY_CHOICE

    ]
    CORRUPTION_CHOICES = [
        [1, ('Коррупция строго преследуется в соответствии с законом и подвергается публичному осуждению')],
        [2,
         (
             'Коррупция в целом преследуется по закону и осуждается, однако иногда вовлеченным в нее людям удается найти лазейки и уйти от ответственности')],
        [3, ('Коррупция недостаточно преследуется по закону, и иногда подвергается публичному осуждению')],
        [4, ('Коррупция практически безнаказанна, и не осуждается публично')],
        HARD_TO_SAY_CHOICE
    ]
    CIVIL_RIGHTS_CHOICES = [
        [1, ('Гражданские права эффективно защищены законом, а их нарушение карается')],
        [2,
         (
             'Гражданские права охраняются законом, но защита недостаточна, и нарушение этих прав не всегда преследуется')],
        [3,
         (
             'Гражданские права обозначены в законе, но на практике нарушаются, и механизмы их защиты, как правило, неэффективны')],
        [4, ('Гражданские права систематически нарушаются, и механизмы их защиты отсутствуют')],
        HARD_TO_SAY_CHOICE
    ]
    SATIS_CHOICES = range(0, 11)
    HAPPY_CHOICES = [
        [0, ('Несчастливый человек')],
        [1, ('Счастливый человек')],
    ]
    RELATIVE_HAPPY_CHOICES = [
        [1, ('1 - Менее счастливы чем они')],
        [2, '2'],
        [3, '3'],
        [4, ('4 - В среднем так же счастлив, как и они')],
        [5, '5'],
        [6, '6'],
        [7, ('7 - Более счастлив чем они')]
    ]
    INCOME_CHOICES = [
        [1, ('Не хватает денег даже на еду')],
        [2, ('Хватает на еду, но не хватает на покупку одежды и обуви')],
        [3, ('Хватает на одежду и обувь, но не хватает на покупку мелкой бытовой техники')],
        [4,
         (
             'Хватает денег на небольшие покупки, но покупка дорогих вещей (компьютера, стиральной машины, холодильника) требует накоплений или кредита')],
        [5,
         (
             'Хватает денег на покупки для дома, но на покупку машины, дачи, квартиры необходимо копить или брать кредит')],
        [6, ('Можем позволить себе любые покупки без ограничений и кредитов')]
    ]
    PARTY_CHOICES = [
        [1, ('Единая Россия')],
        [2, ('КПРФ')],
        [3, ('ЛДПР')],
        [4, ('Справедливая Россия')],
        [5, ('Яблоко')],
        [6, ('Другая партия')],
        [7, ('В России нет партии, которой  я симпатизирую')],
        [8, ('Я не интересуюсь политикой')],
        HARD_TO_SAY_CHOICE
    ]
    AgreementChoices4DNK = [
        [1, ('Совершенно согласен')],
        [2, ('Скорее согласен')],
        [3, ('Скорее не согласен')],
        [4, ('Совершенно не согласен')],
        HARD_TO_SAY_CHOICE
    ]

    TrustChoices4DNK = [
        [1, ('Полностью доверяю')],
        [2, ('В некоторой степени доверяю')],
        [3, ('Не очень доверяю')],
        [4, ('Совсем не доверяю')],
        HARD_TO_SAY_CHOICE
    ]

    SimilarChoices6DNK = [
        [1, ('Очень похож на меня')],
        [2, ('Похож на меня')],
        [3, ('Отчасти похож на меня')],
        [4, ('Немного похож на меня')],
        [5, ('Не похож на меня')],
        [6, ('Совсем не похож на меня')],
    ]

    AgreementChoices5DNK = [
        [1, ('Совершенно согласен')],
        [2, ('Скорее согласен')],
        [3, ('И да и нет')],
        [4, ('Скорее не согласен')],
        [5, ('Совершенно не согласен')],
        HARD_TO_SAY_CHOICE
    ]

    Sibling4 = [
        [1, ('0')],
        [2, ('1')],
        [3, ('2')],
        [4, ('3')],
        [5, ('4 или более')],
    ]

    Region6 = [
        [1, ('0')],
        [2, ('1')],
        [3, ('2-3')],
        [4, ('4-6')],
        [5, ('7 или более')],
    ]
    # Survey1
    Inc5DNK = IncrementChoices5DNK
    # Survey2
    Agree4DNK = AgreementChoices4DNK
    # Survey3
    Trust4DNK = TrustChoices4DNK
    # Surveys4
    Similar6DNK = SimilarChoices6DNK
    # Survey5similar_newideas
    Agree5DNK = AgreementChoices4DNK
    # Survery6
    Sib4 = Sibling4
    # Survery7
    Reg6 = Region6
    SOURCE_CHOICES = [
        [0, ('Я живу/жил/посещал этот регион')],
        [1, ('От родственников и друзей')],
        [2, ('Из социальных сетей (vk, instagram и др.)')],
        [3, ('Из средств массовой информации (газеты, телевидение, интернет-медиа и др.)')],
        [4, ('В школе или университете')],
        [5, ('Другие источники')],
        [999, ('Ничего не знаю о регионе')]
    ]
    BEEN_CHOICES = [
        [0, ('Да')],
        [1, ('Нет')]
    ]


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly(fixed_id_in_group=True)
        else:
            self.group_like_round(1)


class Group(BaseGroup):

    def pay_tax(self):
        """
        Paying the tax
        :return:
        """
        for p in self.get_players():
            p.tax_paid = Constants.tax
            p.budget -= Constants.tax

    def set_payoffs(self):
        """
        Assigns payoffs to every player
        :return:
        """
        players = self.get_players()
        total_tax = c(0)
        for p in players:
            total_tax += c(p.tax_paid)

        officer = self.get_player_by_role('Officer')

        k_officer = officer.set_k

        k_real = officer.k_real
        payoffs = total_tax * k_officer

        for p in players:
            p.payoff = payoffs / 2
            if p == officer:
                p.over_pay += total_tax * (k_real - k_officer)

    def collect_payoffs(self):
        """
        Add payoffs to the budget
        :return:
        """
        for p in self.get_players():
            p.budget += p.payoff + p.over_pay

    def computer_check(self):
        """
        Computer checks for officers and real K
        If do not match
        officers pays a fine
        :return:
        """
        officer = self.get_player_by_role('Officer')
        officer.checked = True
        if officer.k_real > officer.set_k:
            officer.fine = 1.5 * officer.over_pay
            officer.budget -= officer.fine

    def random_check(self):
        r = random.choice([1, 0, 0])
        if r == 1:
            self.computer_check()

    def do_all(self):
        self.pay_tax()
        self.set_payoffs()

        self.random_check()

        self.collect_payoffs()

    def guess(self):
        """
        Collects all guesses for K from all rounds
        :return:
        """
        guesses = []
        p = self.get_player_by_role('Citizen')
        player_obj = p.in_all_rounds()
        for p2 in player_obj:
            guesses.append(p2.guess)

        return guesses

    def random_guess_pick(self):
        """
        Picks a random value of K that Citizen guessed
        :return:
        """
        k = random.choice(self.guess())
        return k

    def additional_payoff(self):
        """
        Distributes additional payoff if a random value of K guessed is equal to the true value
        :return:
        """
        premium = c(0)
        if self.random_guess_pick() == Constants.k_real:
            p = self.get_player_by_role('Citizen')
            p.additional_payoff = c(5)
            p.budget += c(5)
            premium = p.additional_payoff
        return premium

    def get_k(self):
        p = self.get_player_by_role('Officer')
        return p.set_k

class Player(BasePlayer):
    name = models.StringField(initial='name')
    age = models.IntegerField(initial=20)
    budget = models.CurrencyField(initial=c(10))
    k_real = models.IntegerField(initial=Constants.k_real)
    set_k = models.IntegerField(min=0, max=Constants.k_real)  # for officer only
    role = models.StringField()
    tax_paid = models.CurrencyField(initial=c(0))
    over_pay = models.CurrencyField(initial=c(0))
    fine = models.CurrencyField(initial=c(0))
    checked = models.BooleanField(initial=False)
    guess = models.IntegerField(initial=0, blank=True)
    additional_payoff = models.CurrencyField(initial=c(0))

    # Officer questions
    q1 = models.BooleanField(choices=[
        [True, 'Да'],
        [False, 'Нет']
    ], label='Да/Нет')
    q2 = models.BooleanField(choices=[
        [True, 'Да'],
        [False, 'Нет']
    ], label='Да/Нет')
    q3 = models.BooleanField(choices=[
        [True, 'Да'],
        [False, 'Нет']
    ], label='Да/Нет')
    q4 = models.BooleanField(choices=[
        [True, 'Да'],
        [False, 'Нет']
    ], label='Да/Нет')

    # survey
    gender = models.BooleanField(initial=None,
                                 choices=Constants.GENDER_CHOICES,
                                 label=('Ваш пол'),
                                 widget=widgets.RadioSelect())

    education = models.IntegerField(initial=None,
                                    choices=Constants.EDUCATION_CHOICES,
                                    label=(
                                        """Какой у Вас самый высокий уровень образования, по которому Вы получили аттестат, свидетельство, диплом? """),
                                    widget=widgets.RadioSelect())
    age = models.PositiveIntegerField(label=('Ваш возраст (полных лет)'),
                                      min=13, max=95,
                                      initial=None)

    marital_status = models.PositiveIntegerField(
        label=('Ваш семейный статус'),
        choices=Constants.MARITAL_STATUS_CHOICES,
        widget=widgets.RadioSelect()
    )
    religion = models.PositiveIntegerField(
        label=('Какую религию Вы исповедуете?'),
        choices=Constants.RELIGION_CHOICES,
        widget=OtherRadioSelect(other=(9, ('religion_other')))
    )

    relative_position_in_region = models.IntegerField(
        label=('Ваш средний ежемесячный доход'),
        choices=Constants.RELATIVE_POSITION_CHOICES,
        widget=widgets.RadioSelect()
    )

    similar_care_society = models.IntegerField(
        label=("""Для этого человека важно делать что-то хорошее для общества."""),
        choices=Constants.Similar6DNK
    )

    similar_care_nearby = models.IntegerField(
        label=("""Для этого человека важно  заботиться о близких ему людях"""),
        choices=Constants.Similar6DNK
    )

    justified_subsidies = models.IntegerField(
        label=("""Получение государственных пособий, на которые у человека нет права"""),
        choices=Constants.JUSTIFIED_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    justified_freeride = models.IntegerField(
        label=("""Проезд без оплаты в общественном транспорте"""),
        choices=Constants.JUSTIFIED_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    justified_theft = models.IntegerField(
        label=("""Кража чужой собственности"""),
        choices=Constants.JUSTIFIED_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    justified_tax_evasion = models.IntegerField(
        label=("""Неуплата налогов, если есть такая возможность"""),
        choices=Constants.JUSTIFIED_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    justified_corruption = models.IntegerField(
        label=("""Получение взятки"""),
        choices=Constants.JUSTIFIED_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    justified_violence = models.IntegerField(
        label=_("""Применение насилия в отношении других людей"""),
        choices=Constants.JUSTIFIED_CHOICES,
        widget=widgets.RadioSelectHorizontal()
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
        choices=Constants.FEATURE_CHOICES,
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
        choices=Constants.FEATURE_CHOICES,
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
        choices=Constants.FEATURE_CHOICES,
        widget=LikertWidget(
            quote=_(
                'Как Вы думаете, если представится возможность, большинство людей попытались бы использовать вас в своих интересах, или вели бы себя порядочно?'),
            label=_(
                'Для ответа выберите значение на шкале от 0 до 10, где 0 означает, что «люди обязательно попытаются вас использовать», а 10 означает, что «люди поведут себя порядочно»'),
            left=_('Люди обязательно попытаются вас использовать'),
            right=_('Люди поведут себя порядочно'),
        )
    )

    honest_Russia = models.PositiveIntegerField(
        label=(
            """В нынешней России честному человеку трудно достичь каких-то высот, занять высокое положение в обществе"""),
        choices=Constants.Agree5DNK,
        widget=widgets.RadioSelect
    )

    party_Russia = models.PositiveIntegerField(
        label=("""Сторонником какой политической партии вы являетесь, или по крайней мере,симпатизируете ей? """),
        choices=Constants.PARTY_CHOICES,
        widget=OtherRadioSelect(other=(6, _('party_other')))
    )

    income = models.PositiveIntegerField(
        label=("""Какое высказывание наиболее точно описывает финансовое положение вашей семьи?"""),
        choices=Constants.INCOME_CHOICES,
        widget=widgets.RadioSelect()
    )

    def role(self):
        """
        Assign roles to members of a group
        :return:
        """
        if self.id_in_group == 1:
            return "Officer"
        else:
            return "Citizen"
