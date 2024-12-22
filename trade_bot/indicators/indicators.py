# indicators/indicators.py
import pandas as pd
import talib

def calculate_ema(data, period, column="close"):
    """Üstel Hareketli Ortalama (EMA) hesaplar."""
    return talib.EMA(data[column], timeperiod=period)

def calculate_rsi(data, period, column="close"):
    """Göreceli Güç Endeksi (RSI) hesaplar."""
    return talib.RSI(data[column], timeperiod=period)

def calculate_macd(data, fast_period, slow_period, signal_period, column="close"):
    """MACD (Moving Average Convergence Divergence) hesaplar."""
    macd, signal, hist = talib.MACD(data[column], fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal_period)
    return macd, signal, hist

def calculate_bollinger_bands(data, period, std_dev, column="close"):
    """Bollinger Bantlarını hesaplar."""
    upper, middle, lower = talib.BBANDS(data[column], timeperiod=period, nbdevup=std_dev, nbdevdn=std_dev)
    return upper, middle, lower

def calculate_stochastic_oscillator(data, k_period, d_period, column_high="high", column_low="low", column_close="close"):
    """Stokastik Osilatör hesaplar."""
    slowk, slowd = talib.STOCH(data[column_high], data[column_low], data[column_close], fastk_period=k_period, slowk_period=d_period, slowd_period=d_period)
    return slowk, slowd

def calculate_all_indicators(data, indicators_config):
    """
    Yapılandırılmış göstergeleri hesaplar.

    Args:
        data (pd.DataFrame): Göstergelerin hesaplanacağı veri.
        indicators_config (dict): Kullanılacak göstergelerin konfigürasyonu.

    Returns:
        pd.DataFrame: Hesaplanmış göstergeleri içeren veri.
    """
    for indicator_name, params in indicators_config.items():
        if indicator_name == "short_ema":
            data["short_ema"] = calculate_ema(data, params["period"])
        elif indicator_name == "long_ema":
            data["long_ema"] = calculate_ema(data, params["period"])
        elif indicator_name == "rsi":
            data["rsi"] = calculate_rsi(data, params["period"])
        elif indicator_name == "macd":
            data["macd"], data["macd_signal"], data["macd_hist"] = calculate_macd(data, params["fast_period"], params["slow_period"], params["signal_period"])
        elif indicator_name == "bollinger":
            data["bollinger_upper"], data["bollinger_middle"], data["bollinger_lower"] = calculate_bollinger_bands(data, params["period"], params["std_dev"])
        elif indicator_name == "stochastic_oscillator":
            data["stoch_k"], data["stoch_d"] = calculate_stochastic_oscillator(data, params["k_period"], params["d_period"])

    return data