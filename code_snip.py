#Username and password are in this below

#Code snip I used before to access the files:

from datetime import date
from datetime import datetime

my_date = date.today()
a = my_date.strftime("%Y%m%d")
print(a)

dates = ["20220823", "20220824"]
import datetime
from datetime import date

my_date = date.today()

currentime = datetime.datetime.now().hour
hrr = currentime
if hrr < 7:
    my_date = date.today() - datetime.timedelta(1)

a = my_date.strftime("%Y%m%d")
print(a)
b = (my_date - datetime.timedelta(1)).strftime("%Y%m%d")
print(b)
dates = [str(a), str(b)]

loopback = 1
if loopback == 1:
    for x in range(0):
        dates.append((my_date - datetime.timedelta(1 + x)).strftime("%Y%m%d"))

# dates=[str(a)]
from datetime import datetime

dflist = []
for xyy in dates:
    list = ["IA", "IL", "NE", "MN", "IN", "SD", "KS", "OH", "WI", "ND", "US"]
    # list=['US']

    for xxx in list:
        try:
            print(xxx)
            from urllib.request import urlopen, Request
            from svglib.svglib import svg2rlg
            from reportlab.graphics import renderPM

            url = f"https://enterprise.cropprophet.com/GrainEdge/us_wxfcst_charts/{xyy}/{xxx}_corn_ecmwf_pcp.svgz"
            # url=https://enterprise.cropprophet.com/GrainEdge/us_wxfcst_charts/20220809/US_corn_ecmwf_pcp.svgz
            loc = r"C:\Users\rhale\desktop\US_corn_ecmwf_pcp.svgz"
            username = "GrainEdge"
            password = 'kPTdr4omyPAiv37s'

            import urllib.request

            auth_user = username
            auth_passwd = password

            passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
            passman.add_password(None, url, auth_user, auth_passwd)
            authhandler = urllib.request.HTTPBasicAuthHandler(passman)
            opener = urllib.request.build_opener(authhandler)
            urllib.request.install_opener(opener)
            import xmltodict
            import xml.etree.ElementTree as ET

            print(url)

            res = urllib.request.urlopen(url)
            import gzip

            data = res.read()
            a = gzip.decompress(data)
            # a=res.info()
            b = a
            a = a.decode("UTF-8")
        except:
            pass