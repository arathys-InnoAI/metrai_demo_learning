from generator import generate_temperatures, get_daily_averages
#start_date,start_temp,num_days,variation,seed
df = generate_temperatures("2024-01-01",20.0,5,5.0,42)

print("Hourly Data (10 rows)")
print(df.head(10))
#print(df.info())
print("\nDaily Averages")
daily = get_daily_averages(df)
print(daily)