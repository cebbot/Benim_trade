# config.py
import os

# Binance API Anahtarları
BINANCE_API_KEY = os.environ.get("BINANCE_API_KEY")
BINANCE_API_SECRET = os.environ.get("BINANCE_API_SECRET")

# Ticaret Yapılacak Parite
SYMBOL = "BTCUSDT"

# Zaman Aralığı (1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M)
TIMEFRAME = "1h"

# Test Modu (True: Testnet, False: Gerçek Hesap)
TEST_MODE = True

# Veri Geçmişi (gün)
DATA_HISTORY = 365 * 5

# Risk Yönetimi
STOP_LOSS_PERCENTAGE = 0.02  # %2 Stop-Loss
TAKE_PROFIT_PERCENTAGE = 0.05  # %5 Take-Profit
MAX_POSITION_SIZE = 0.5  # Maksimum pozisyon büyüklüğü (hesap bakiyesinin yüzdesi)

# Yapay Zeka Modeli
MODEL_PATH = "models/trained_model.pkl"

# Kullanılacak İndikatörler
INDICATORS = {
    "short_ema": {"period": 12},
    "long_ema": {"period": 26},
    "rsi": {"period": 14},
    "macd": {"fast_period": 12, "slow_period": 26, "signal_period": 9},
    "bollinger": {"period": 20, "std_dev": 2},
    "stochastic_oscillator": {"k_period": 14, "d_period": 3},
}