from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

TOLOKA_PARTICIPATION_FEE = 0.25
CENTS_PER_TOKEN = 2

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=CENTS_PER_TOKEN / 100,
    participation_fee=0.00,
    doc="",
    use_browser_bots=False,
    toloka_participation_fee=TOLOKA_PARTICIPATION_FEE
)

SESSION_CONFIGS = [
    dict(
        name='baseline',
        display_name="Embezzlement game - baseline",
        num_demo_participants=2,
        app_sequence=[
            'start',
            'embez',
            'last'
        ],
        treatment='baseline',
        toloka=True,
        toloka_sandbox=True
    ),

    dict(
        name='q',
        display_name="Questionnaire + Toloka code",
        num_demo_participants=1,
        app_sequence=['questionnaire', 'last'],
        toloka=True,
        toloka_sandbox=True

    ),
    dict(
        name='full',
        display_name="Full version",
        num_demo_participants=2,
        app_sequence=['start', 'embez', 'questionnaire', 'last'],
        toloka=True,
        toloka_sandbox=True

    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ru'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 2
ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'k4y6sr0h22wfig5f0ish2w$pqy7ze)&sbqvff#zd)5i$wu-_i$'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree', 'django.contrib.admin', ]
EXTENSION_APPS = ['tolokaregister']
TOLOKA_API = environ.get('TOLOKA_API')
SANDBOX_TOLOKA_API = environ.get('SANDBOX_TOLOKA_API')
DECIMAL_SEPARATOR = '.'
FORMAT_MODULE_PATH = [
    'start.formats',
]
