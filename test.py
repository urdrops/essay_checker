'''
import requests

url = "https://pen-to-print-handwriting-ocr.p.rapidapi.com/recognize/"

files = { "srcImg": open('exmpl-test.jpg', 'rb') }
payload = { "Session": "string" }
headers = {
	"X-RapidAPI-Key": "f3aef16d90msh4a9bf5cbd17468ep1c1434jsn4abd1443e3d5",
	"X-RapidAPI-Host": "pen-to-print-handwriting-ocr.p.rapidapi.com"
}

response = requests.post(url, data=payload, files=files, headers=headers)

print(response.json()['value'])
'''
def mult(a,b):
    return a * b
