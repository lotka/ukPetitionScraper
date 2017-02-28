import requests,json,time,datetime

def get():
    x = requests.get('https://petition.parliament.uk/petitions/171928.json')
    return json.loads(x.text)['data']['attributes']['signature_count']

while True:
    with open('petition.csv','aw') as f:
        s = str(datetime.datetime.today()) + ',' + str(get())+'\n'
        print s
        f.writelines(s)
        time.sleep(10)
