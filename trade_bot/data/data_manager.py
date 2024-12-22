# data/data_manager.py
import ccxt
import pandas as pd
import time
from config import BINANCE_API_KEY, BINANCE_API_SECRET, SYMBOL, TIMEFRAME, DATA_HISTORY, TEST_MODE
from utils.logging import logger

class DataManager:
    def __init__(self):
        self.exchange = ccxt.binance({
            "apiKey": BINANCE_API_KEY,
            "secret": BINANCE_API_SECRET,
            "enableRateLimit": True,
            "options": {
                "defaultType": "future"  # Kaldıraçlı işlemler için "future"
            }
        })
        if TEST_MODE:
            self.exchange.set_sandbox_mode(True)
        self.symbol = SYMBOL
        self.timeframe = TIMEFRAME

    def get_historical_data(self, limit=DATA_HISTORY):
        """
        Binance'den geçmiş verileri çeker.

        Args:
            limit (int): Geriye dönük kaç günlük veri çekileceği.

        Returns:
            pd.DataFrame: Geçmiş verileri içeren DataFrame.
        """
        try:
            logger.info(f"Fetching historical data for {self.symbol} ({self.timeframe}) - {limit} days")
            since = self.exchange.milliseconds() - limit * 24 * 60 * 60 * 1000
            all_candles = []
            while since < self.exchange.milliseconds():
                candles = self.exchange.fetch_ohlcv(self.symbol, self.timeframe, since)
                if not candles:
                    break
                since = candles[-1][0] + 1
                all_candles += candles
                time.sleep(self.exchange.rateLimit / 1000)
            data = pd.DataFrame(all_candles, columns=["timestamp", "open", "high", "low", "close", "volume"])
            data["date"] = pd.to_datetime(data["timestamp"], unit="ms")
            data.set_index("date", inplace=True)
            data.drop_duplicates(inplace=True)
            logger.info(f"Successfully fetched historical data. Rows: {len(data)}")
            return data
        except Exception as e:
            logger.error(f"Error fetching historical data: {e}")
            return None

    def preprocess_data(self, data):
        """
        Verileri ön işleme adımlarını gerçekleştirir.
        Şimdilik sadece boş değerleri kontrol ediyor.

        Args:
            data (pd.DataFrame): İşlenecek veri.

        Returns:
            pd.DataFrame: İşlenmiş veri.
        """
        try:
            logger.info("Preprocessing data...")
            # Eksik değerleri kontrol et
            if data.isnull().values.any():
                logger.warning("Data contains missing values. Handling missing values...")
                # Burada eksik değerleri doldurma stratejisi uygulanabilir (örneğin, ffill, bfill)
                data.fillna(method="ffill", inplace=True)  # Örnek olarak önden doldurma
            logger.info("Data preprocessing completed.")
            return data

        except Exception as e:
            logger.error(f"Error preprocessing data: {e}")
            return None