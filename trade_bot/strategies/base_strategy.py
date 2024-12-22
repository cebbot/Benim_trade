# strategies/base_strategy.py
from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    def __init__(self, indicators_config):
        self.indicators_config = indicators_config

    @abstractmethod
    def calculate_signals(self, data):
        """
        Verilen veri setine göre alım, satım ve pozisyon kapatma sinyallerini hesaplar.

        Args:
            data (pd.DataFrame): Sinyallerin hesaplanacağı veri.

        Returns:
            pd.DataFrame: 'signal' sütunu eklenmiş veri.
                -1: Satım
                1: Alım
                0: Pozisyonu Kapat
                None: Hiçbir işlem yapma
        """
        pass