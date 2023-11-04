# Example copied from https://documenter.getpostman.com/view/8854915/Szf26WHn

from http.client import HTTPSConnection # native

conn = HTTPSConnection("www.dataaccess.com")
payload = '''\
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
      <ubiNum>1000</ubiNum>
    </NumberToWords>
  </soap:Body>
</soap:Envelope>
'''
headers = {
  'Content-Type': 'text/xml; charset=utf-8'
}
conn.request("POST", "/webservicesserver/NumberConversion.wso", payload, headers)
res = conn.getresponse()
print(res.read().decode())

import requests
# import xml.etree.ElementTree as ET

url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso"

payload = '''\
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
      <ubiNum>500</ubiNum>
    </NumberToWords>
  </soap:Body>
</soap:Envelope>
'''
headers = {
  'Content-Type': 'text/xml; charset=utf-8'
}

response = requests.post(url, headers=headers, data=payload)
print(response.text)

# root = ET.fromstring(response.text)
# print(root.find('//NumberToWordsResult').text)
# print(root[0][0][0].text)

from zeep import Client # installed via pip

client = Client('https://www.dataaccess.com/webservicesserver/NumberConversion.wso?wsdl')
result = client.service.NumberToWords(1000)

print(result)
