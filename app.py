import yfinance as yf
from flask import Flask,jsonify


app=Flask('__name__')


stocks=['RELIANCE.NS', 'SBIN.NS', 'ADANIENT.NS', 'ADANIPORTS.NS', 'AXISBANK.NS', 'BHARTIARTL.NS', 'BRITANNIA.NS', 'CIPLA.NS', 'DRREDDY.NS', 'HCLTECH.NS', 'HDFCBANK.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'INFY.NS', 'ITC.NS', 'LT.NS', 'ONGC.NS', 'POWERGRID.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'TITAN.NS', 'TCS.NS', 'WIPRO.NS', 'HEROMOTOCO.NS', 'INDUSINDBK.NS', 'APOLLOHOSP.NS']




@app.route('/')
def news():
    result=[]



    for j in stocks:
        
        ticker=yf.Ticker(j)
        news=ticker.news
       
        
        result.append({
            'title':news[0]['content']['title'],
            'summary':news[0]['content']['summary'],
            'url':news[0]['content']['canonicalUrl']['url']
        })
    
    return jsonify(result)


if __name__ == "__main__":
    app.run(port=5000, debug=True)

