import requests

response = requests.get ("http://api.nbp.pl/api/exchangerates/tables/A?format=json")

if response.ok == True:
    data = response.json()[0] #dictionary
   

    table = data["table"]
    no = data ["no"]
    effectiveDate = data ["effectiveDate"] 
    
    print ("Exchange rates: " , table, no, effectiveDate)

    rates = data ["rates"]

    for rate in rates:
        currency = rate ["currency"]
        code = rate ["code"]
        mid = rate ["mid"]
        print (currency, "code:" , code, "value:" , mid)
