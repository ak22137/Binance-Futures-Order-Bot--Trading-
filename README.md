# Binance Futures Order Bot

A CLI-based trading bot for Binance USDT-M Futures supporting market, limit, and advanced order types.

## Features
- Market Orders
- Limit Orders
- Advanced Orders: OCO, TWAP
- Input validation
- Structured logging

## Setup
1. Clone the repo or unzip the project.
2. Add your Binance API credentials.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- Market Order:
  ```bash
  python src/market_orders.py BTCUSDT BUY 0.01
  ```
- Limit Order:
  ```bash
  python src/limit_orders.py BTCUSDT BUY 0.01 30000
  ```

## Logging
All actions are logged to `bot.log`.

## Testing
You can use historical data for testing order logic.

## Advanced Orders
See `src/advanced/` for OCO and TWAP strategies.

## Documentation
See `report.pdf` for analysis and screenshots.
