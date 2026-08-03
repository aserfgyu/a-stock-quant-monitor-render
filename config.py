"""A股量化监控系统配置 - Render优化版"""
import os

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "10000"))
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", "300"))

INDEX_SYMBOLS = [
    "000001.SH", "399001.SZ", "399006.SZ",
    "000300.SH", "000688.SH",
]

STOCK_SYMBOLS = [
    "600519.SH", "000001.SZ", "300750.SZ",
    "600036.SH", "000858.SZ", "002594.SZ",
    "601318.SH", "600276.SH",
]

ALL_SYMBOLS = INDEX_SYMBOLS + STOCK_SYMBOLS
HISTORY_DAYS = 90

RSI_PERIOD = 14
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9
BB_PERIOD = 20
BB_STD = 2
ATR_PERIOD = 14

CORS_ORIGINS = ["*"]
