import json
from pprint import pprint
import requests

url = 'https://coronavirus.msal.gov.ar/vacunas/d/8wdHBOsMk/seguimiento-vacunacion-covid/api/datasources/proxy/1/query'

payload_aplicada = {"app":"dashboard","requestId":"Q106","timezone":"","panelId":14,"dashboardId":3,"range":{"from":"2020-12-29T03:00:00.000Z","to":"2021-02-26T13:17:38.629Z","raw":{"from":"2020-12-29T03:00:00.000Z","to":"now"}},"timeInfo":"","interval":"2h","intervalMs":7200000,"targets":[{"data":None,"target":"evolucion_aplicaciones_total_pais","refId":"A","hide":False,"type":"timeseries"}],"maxDataPoints":892,"scopedVars":{"__from":{"text":"1609210800000","value":"1609210800000"},"__to":{"text":"1614345458399","value":"1614345458399"},"__dashboard":{"value":{"name":"Seguimiento vacunación Covid","uid":"8wdHBOsMk"}},"__org":{"value":{"name":"minsal","id":0}},"__interval":{"text":"2h","value":"2h"},"__interval_ms":{"text":"7200000","value":7200000}},"startTime":1614345458682,"rangeRaw":{"from":"2020-12-29T03:00:00.000Z","to":"now"},"adhocFilters":[]}

res = requests.post(url, json=payload_aplicada)
aplicaciones = json.loads(res.text)

pprint(aplicaciones)

