import csv
from collections import defaultdict

from pep_parse.settings import (BASE_DIR, FIELDS_NAME, FILE_NAME, RESULTS,
                                TIME_FORMATED)


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        """Подсчет количества статусов."""
        pep_status = item['status']
        self.results[pep_status] = self.results.get(pep_status, 0) + 1
        return item

    def close_spider(self, spider):
        """Запись данных в файл со сводкой по статусам."""
        file_dir = self.results_dir / FILE_NAME.format(time=TIME_FORMATED)
        with open(file_dir, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows([
                FIELDS_NAME,
                *self.results.items(),
                ('Total', sum(self.results.values())),
            ])
