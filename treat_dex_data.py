import os
import polars as pl

current_path = os.getcwd()
untreated_path = os.path.join(current_path, 'dex_eth_usdt_jan_2025/untreated')
treated_path = os.path.join(current_path, 'dex_eth_usdt_jan_2025/treated')

# Create treated directory if it doesn't exist
os.makedirs(treated_path, exist_ok=True)

for file in os.listdir(untreated_path):
    if not file.endswith('.csv'):
        continue
        
    print(f"Processing {file}...")
    
    # Read the file with explicit schema
    df = pl.read_csv(
        os.path.join(untreated_path, file),
        dtypes={
            'r_0': pl.String,  # Read as string first to handle large numbers
            'r_1': pl.String,
            'timestamp': pl.Int64
        }
    )
    
    # Convert and compute
    df = df.select([
        # Convert from string and handle scientific notation
        pl.col('r_0').cast(pl.Float64).alias('eth_reserves'),
        pl.col('r_1').cast(pl.Float64).alias('usdt_reserves'),
        # Keep timestamp as is for now
        pl.col('timestamp').alias('timestamp')
    ]).with_columns([
        # Calculate price with proper scaling
        (pl.col('usdt_reserves') / pl.col('eth_reserves') * 1e21).alias('eth_usdt')
    ])
    
    # Remove duplicates and sort by timestamp
    df = df.unique().sort('timestamp')
    
    # Save processed file
    output_file = os.path.join(treated_path, file)
    df.write_csv(output_file)
    print(f"Saved treated file to {output_file}")