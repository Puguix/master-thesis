import ccxt
import pandas as pd
from datetime import datetime, timedelta
import os
import time

def download_orderbook_data():
    # Configure exchanges
    exchanges = {
        'binance': ccxt.binance({'enableRateLimit': True}),
        'bybit': ccxt.bybit({'enableRateLimit': True}), 
        'okx': ccxt.okx({'enableRateLimit': True})
    }

    # Trading pairs
    pairs = ['ETH/USDT', 'BTC/USDT', 'LINK/USDT']

    # Create base directory for orderbook data
    base_dir = 'orderbook_data'
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Calculate date range (today)
    end_date = datetime.now()
    start_date = end_date.replace(hour=0, minute=0, second=0, microsecond=0)

    # Download data for each exchange and pair throughout the day
    while start_date <= end_date:
        for exchange_id, exchange in exchanges.items():
            for pair in pairs:
                print(f"\nDownloading {pair} from {exchange_id} at {start_date}...")
                try:
                    # Create directory structure
                    pair_dir = os.path.join(base_dir, exchange_id, pair.replace('/', '_'))
                    if not os.path.exists(pair_dir):
                        os.makedirs(pair_dir)

                    # Format pair symbol according to exchange requirements
                    if exchange_id == 'okx':
                        symbol = pair.replace('/', '-')
                    else:
                        symbol = pair

                    # Fetch orderbook
                    orderbook = exchange.fetch_order_book(symbol, limit=10)

                    # Convert to DataFrame
                    bids_df = pd.DataFrame(orderbook['bids'][:10], columns=['price', 'amount'])
                    asks_df = pd.DataFrame(orderbook['asks'][:10], columns=['price', 'amount'])

                    # Add timestamp and side
                    timestamp = start_date.strftime('%Y-%m-%d_%H-%M-%S-%f')
                    bids_df['timestamp'] = timestamp
                    bids_df['side'] = 'bid'
                    asks_df['timestamp'] = timestamp
                    asks_df['side'] = 'ask'

                    # Combine bids and asks
                    combined_df = pd.concat([bids_df, asks_df])

                    # Save to CSV
                    csv_filename = f"{pair.replace('/', '_')}_{timestamp}.csv"
                    csv_path = os.path.join(pair_dir, csv_filename)
                    combined_df.to_csv(csv_path, index=False)

                    print(f"Downloaded orderbook for {pair} from {exchange_id} at {timestamp}")
                    
                    # Respect rate limits
                    time.sleep(exchange.rateLimit / 1000)  # Convert milliseconds to seconds

                except Exception as e:
                    print(f"Error downloading {pair} from {exchange_id}: {str(e)}")
        
        # Increment by 1 minute
        start_date += timedelta(milliseconds=1)

if __name__ == "__main__":
    download_orderbook_data()
