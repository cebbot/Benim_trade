from data.data_manager import DataManager
from strategies.advanced_strategy import AdvancedStrategy
from trading.trader import Trader
from risk_management.risk_manager import RiskManager
from utils.logging import setup_logging
from visualization.visualizer import Visualizer

def main():
    # Setup logging
    logger = setup_logging()
    logger.info("Starting trading bot...")

    # Initialize components
    data_manager = DataManager()
    strategy = AdvancedStrategy()
    trader = Trader()
    risk_manager = RiskManager()
    visualizer = Visualizer()

    try:
        # Main trading loop
        while True:
            # Get market data
            data = data_manager.get_latest_data()
            
            # Generate signals
            signals = strategy.generate_signals(data)
            
            # Apply risk management
            approved_signals = risk_manager.evaluate_signals(signals)
            
            # Execute trades
            trader.execute_trades(approved_signals)
            
            # Visualize results
            visualizer.update_charts(data)
            
    except KeyboardInterrupt:
        logger.info("Shutting down trading bot...")
        trader.close_all_positions()

if __name__ == "__main__":
    main()