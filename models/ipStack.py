import requests

'''
Author: Bryan Ison
Date: 2/18/2021

Description:
Ip Stack model represents the json data aquired from the user agent information based on IP.
That info is encoded and returned to us as a json payload.
'''


class IpStack:
    accessKey = "e954b7c34bbf074a2ac8da2a99154cb6"
    accessUrl = "http://api.ipstack.com/"
    ipAddress = ""
    callUrl = ""
    latitude = ""
    longitude = ""
    mapURL = ""
    mapHtmlLink = ''''''

    def __init__(self, ippayload):
        result = ippayload.find(',')  # implementing this fix due to google cloud passing multiple ip addresses!

        # If the cloud proposes multiple ips, only grab the first one.
        if result != -1:
            ippayload = ippayload[0:result]
            print("Parsing multiple ips...")
            print("Final IP: " + ippayload)

        self.ipAddress = ippayload
        self.callUrl = self.accessUrl + self.ipAddress + '?access_key=' + self.accessKey
        print("Calling URL:" + self.callUrl)

    def getData(self):
        response = requests.get(self.callUrl)
        json_data = response.json()
        self.latitude = str(json_data['latitude']).strip()
        self.longitude = str(json_data['longitude']).strip()
        self.mapURL = self.load_map_url()
        print("Map Link: " + self.mapURL)
        self.mapHtmlLink = '''
        <html>
            <body>
                <a href="%s" target="_blank">Run Map</a></html>
                </body>
        </html>
        ''' % self.mapURL

        # for key, value in json_data.items():
        #   print(key, ":", value)
        return json_data

    def load_map_url(self):
        # URL Format = https://nominatim.openstreetmap.org/ui/reverse.html?format=html&lat=PUTLATHERE&lon=PUTLONGHERE&zoom=10

        # Zoom State Values
        # 3 	country
        # 5 	state
        # 8 	county
        # 10 	city
        # 14 	suburb
        # 16 	major streets
        # 17 	major and minor streets
        # 18 	building
        print("Loading map....")
        zoom_state = '10'

        # Wont work on the server!!
        # webbrowser.open('https://nominatim.openstreetmap.org/ui/reverse.html?format=html&lat=' + lat + '&lon=' + long + '&zoom=' + zoom_state + '')

        return 'https://nominatim.openstreetmap.org/ui/reverse.html?format=html&lat=' + self.latitude + '&lon=' + self.longitude + '&zoom=' + zoom_state + ''
