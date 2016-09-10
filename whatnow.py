import requests

res = requests.get('https://api.tfl.gov.uk/line/mode/tube,overground,dlr,tflrail/status')

res = res.json()
out = {}

for t in res:
    tfl_type = t['name']
    if tfl_type == 'London Overground':
        for st in t['lineStatuses']:
            status_desc = st['statusSeverityDescription']

            print()
            if 'disruption' in st:
                desc = st['disruption']['description']
                print(status_desc, '-', desc)



