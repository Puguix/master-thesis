# Master-thesis: Lead lag analysis between CEX and DEX

This project collects and stores high-frequency orderbook data from major cryptocurrency exchanges (Binance, Bybit, and OKX) for specified trading pairs.

## Features

- Collects detailed orderbook data for:
  - BTC-USDT
  - ETH-USDT
  - LINK-USDT
- Supports multiple exchanges:
  - Binance
  - Bybit
  - OKX
- Configurable orderbook depth (top 5/10 levels)
- Efficient CSV storage format
- Organized directory structure by exchange and trading pair
- Timestamp precision up to milliseconds

## Prerequisites

- Python 3.8 or higher
- pip (Python Package Manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Project Structure

```
.
├── download_data.py          # Main data collection script
├── orderbook_data/          # Data storage directory
│   ├── binance/
│   │   ├── BTC_USDT/
│   │   ├── ETH_USDT/
│   │   └── LINK_USDT/
│   ├── bybit/
│   └── okx/
├── requirements.txt         # Python dependencies
└── README.md
```

## Data Format

The orderbook data is stored in CSV format with the following naming convention:
```
{SYMBOL}_{DATE}_{TIME}.csv
```

Example: `BTC_USDT_2025-03-06_00-00-00-002000.csv`

Each CSV file contains orderbook snapshots with the following columns:
- Timestamp
- Bid Price
- Bid Volume
- Ask Price
- Ask Volume

## Usage

Run the data collector:

```bash
python download_data.py
```

## Configuration

Modify the script parameters in `download_data.py` to adjust:
- Trading pairs
- Exchanges
- Orderbook depth
- Collection frequency
- Storage format

## Error Handling

The script includes error handling for:
- Network connectivity issues
- API rate limits
- Data validation
- File system operations

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This software is for educational and research purposes only. Use at your own risk. The authors are not responsible for any financial losses incurred while using this software.
```

This updated README:
1. Reflects the Python-based implementation (rather than Node.js)
2. Matches your actual project structure with CSV files
3. Includes the correct file naming convention based on your existing files
4. Provides clear installation and usage instructions
5. Maintains a professional and comprehensive documentation structure

Would you like me to make any specific adjustments to this README?
