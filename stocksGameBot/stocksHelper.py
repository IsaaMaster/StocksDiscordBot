from alpha_vantage.timeseries import TimeSeries
from csvreader import readCSV
import time
apikey = "0SA2DHWSEJAM986Y"

def getPrice(stock): 

    endquote = TimeSeries(key = apikey, output_format='csv')
    

    data,metadata = endquote.get_quote_endpoint(stock)
    info = readCSV(data)
    print(info)
    try:

        return float(info[1][4])
    except:
        print("sleeping...")
        time.sleep(10)
        return getPrice(stock)
        


