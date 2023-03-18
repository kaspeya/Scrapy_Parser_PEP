import datetime as dt
from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
RESULTS_DIR = BASE_DIR / RESULTS

DT_FORMAT = '%Y-%m-%dT%H-%M-%S'
FILE_NAME = 'status_summary_{time}.csv'
TIME_FORMATED = dt.datetime.now().strftime(DT_FORMAT)
FIELDS_NAME = ('Статус', 'Количество')


FEEDS = {
    f'{RESULTS}/pep_%(time)s.csv': {
        'format': 'csv',
        # Поля, данные из которых будут выведены в файл, и их порядок.
        'fields': ['number', 'name', 'status'],
        # Если файл с заданным именем уже существует, то
        # при значении False данные будут дописываться в существующий файл;
        # при значении True существующий файл будет перезаписан.
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
