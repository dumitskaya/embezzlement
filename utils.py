from shutil import copyfile
from importlib import import_module
import os.path
from otree.api import Page
APP_NAME = 'embez'
pages = import_module(APP_NAME + '.pages')
page_sequence = pages.page_sequence
TEMPLATE_PATH = f'./{APP_NAME}/templates/{APP_NAME}/'
for i in page_sequence:
    if issubclass(i, Page):
        filetocreate = TEMPLATE_PATH + f'{i.__name__}.html'
        if not os.path.exists(filetocreate):
            copyfile(TEMPLATE_PATH + 'MyPage.html', filetocreate)
        else:
            print(f'File {i.__name__} already exists')
    else:
        print("NOPE", i.__name__)