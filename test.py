import requests

resp = requests.post("https://caesarmobtranslate.fly.dev/caesarmobiletranslate",json={"text":"Hola Mundo","dest":"fr"})
print(resp.json())