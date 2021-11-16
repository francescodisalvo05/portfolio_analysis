import logging
import os
from typing import Text
import pandas as pd
from scripts.data.load import load_csv
from scripts.extraction.yahoo_extraction import extract_data_from_yahoo
from scripts.portfolio.utils import check_date


class Ticker:

    def __init__(self,
                 ticker_id: Text,
                 folder_dir: Text,
                 name: Text = None,
                 isin: Text = None,
                 instrument: Text = None,
                 risk: int = None,
                 fee: float = None):
        self.id = ticker_id

        self.name = name,
        self.isin = isin,
        self.instrument = instrument,
        self.risk = risk,
        self.fee = fee

        self.path = f'{folder_dir}/{ticker_id}.csv'
        self.logger = logging.getLogger(f'{ticker_id}')

        self.data = self._init_data()

    def _init_data(self) -> pd.DataFrame:

        if os.path.exists(self.path):
            data = load_csv(self.path)
        else:
            data = self._load_data(start_date=None)
            self.logger.info(f' > Saving ticker data at {self.path}')
            data.to_csv(self.path)

        return data

    def _load_data(self, start_date):
        data = extract_data_from_yahoo(ticker=self.id,
                                       start_date=start_date)
        if data is not None:
            return data
        else:
            return data

    def get_data_from_date(self,
                           start_date: Text,
                           end_date: Text):
        check = check_date(start_date) and check_date(end_date)
        if not check:
            return None

        filter_df = self.data[start_date: end_date]

        return filter_df

    def update_data(self):
        last_date = str((self.data.index.to_list()[-1]).date())
        update_data = self._load_data(start_date=last_date)

        self.data = self.data.append(update_data)

        self.save()

        return

    def save(self):
        self.logger.info(f' > Saving ticker data at {self.path}')
        self.data.to_csv(self.path)

        return
