"""数据获取 - Render优化版"""
import os, time, logging
from datetime import datetime, timedelta
from typing import Dict, List
from pathlib import Path
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataFetcher:
    def __init__(self, use_ifind=False):
        self.use_ifind = use_ifind
        self._cache = {}
        self._cache_time = {}
        self.ttl = 300

    def _mock(self, ticker: str, start: str, end: str) -> pd.DataFrame:
        np.random.seed(hash(ticker) % 2**32)
        s = datetime.strptime(start, '%Y-%m-%d')
        e = datetime.strptime(end, '%Y-%m-%d')
        dates = []
        c = s
        while c <= e:
            if c.weekday() < 5: dates.append(c)
            c += timedelta(days=1)
        base = {'000001.SH':3900,'399001.SZ':14500,'399006.SZ':3600,'000300.SH':4700,'000688.SH':1800,
                '600519.SH':1300,'000001.SZ':11,'300750.SZ':400,'600036.SH':35,'000858.SZ':160,
                '002594.SZ':280,'601318.SH':48,'600276.SH':45}.get(ticker, 100)
        n = len(dates)
        ret = np.random.normal(0.0005, 0.015, n)
        prices = base * np.exp(np.cumsum(ret))
        data = []
        for i,d in enumerate(dates):
            p = prices[i]
            data.append({
                'time': d.strftime('%Y%m%d'),
                'open': round(p*(1+np.random.normal(0,0.005)),2),
                'high': round(p*(1+abs(np.random.normal(0,0.008))),2),
                'low': round(p*(1-abs(np.random.normal(0,0.008))),2),
                'close': round(p,2),
                'volume': int(np.random.uniform(1e7,5e8)),
                'thscode': ticker, 'thsname_cn': ticker,
            })
        return pd.DataFrame(data)

    def fetch(self, ticker: str, days: int = 90) -> pd.DataFrame:
        end = datetime.now().strftime('%Y-%m-%d')
        start = (datetime.now()-timedelta(days=days)).strftime('%Y-%m-%d')
        key = f"{ticker}_{start}_{end}"
        if key in self._cache and time.time()-self._cache_time.get(key,0) < self.ttl:
            return self._cache[key]
        df = self._mock(ticker, start, end)
        self._cache[key] = df
        self._cache_time[key] = time.time()
        return df

    def fetch_batch(self, tickers: List[str], days: int = 90) -> Dict[str, pd.DataFrame]:
        return {t: self.fetch(t, days) for t in tickers}
