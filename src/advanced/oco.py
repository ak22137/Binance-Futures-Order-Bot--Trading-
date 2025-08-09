"""
OCO (One-Cancels-the-Other) order logic for Binance Futures Order Bot
"""
import logging

def place_oco_order(symbol, quantity, take_profit, stop_loss):
    # Validate inputs
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Invalid symbol")
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    if take_profit <= 0 or stop_loss <= 0:
        raise ValueError("Prices must be positive")
    logging.info(f"Placing OCO order: {symbol} {quantity} TP={take_profit} SL={stop_loss}")
    # TODO: Integrate with Binance API
    return {"status": "success", "symbol": symbol, "quantity": quantity, "take_profit": take_profit, "stop_loss": stop_loss}
