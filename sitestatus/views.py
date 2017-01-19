from sitestatus import app, render_template
import requests

SITES_LIST = [{ 'name': 'GOOGLE', 'url': 'https://www.google.com', 'status_code': 0, 'status': '' },
         { 'name': 'YAHOO', 'url': 'https://www.yahoo.com', 'status_code': 0, 'status': '' },
         { 'name': 'CNN', 'url': 'http://www.cnn.com', 'status_code': 0, 'status': '' },
         { 'name': 'MOZILLA', 'url': 'https://www.mozilla.org/en-US/', 'status_code': 0, 'status': '' },
         { 'name': 'MICROSOFT', 'url': 'https://www.microsoft.com/en-us/', 'status_code': 0, 'status': '' }]


def get_sites_status(sites):
    for site in sites:
        try:
            r = requests.head(site['url'])
            site['status_code'] = r.status_code
            print(r.status_code)
            if r.status_code in (200, 302, 303, 401):
                site['status'] = 'Operational'
            else:
                site['status'] = r.reason       
        except requests.exceptions.RequestException as e:
            site['status_code'] = 520
            site['status'] = 'Uknown Error'
    return sites


@app.route('/')
def index():
    return render_template('index.html', site_status=get_sites_status(SITES_LIST))

@app.route('/jsdemo')
def jsdemo():
    return render_template('jsdemo.html')