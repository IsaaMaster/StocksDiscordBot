from alpha_vantage.timeseries import TimeSeries
apikey = "0SA2DHWSEJAM986Y"
ts = TimeSeries(key='YOUR_API_KEY')

data= ts.get_intraday_extended('GME')

print(data)