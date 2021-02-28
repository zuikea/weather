#!/usr/bin/env python
#coding=utf-8
import urllib2
from xml.etree import cElementTree as ET
class GetWeather:
    def __init__(self):
        self.weather = self.makexml()
    def makexml(self):
        url = "http://weather.yahooapis.com/forecastrss?w=2151330&u=c"
        res = urllib2.urlopen(url)
        xmlfile = open("yahoo.xml",'w')
        xmlfile.writelines(res.read())
        xmlfile.close()
        return self.xmlET()

    def xmlET(self):
        tree = ET.ElementTree(file="yahoo.xml")
        forecast = []
        for elem in tree.iter(tag="{http://xml.weather.yahoo.com/ns/rss/1.0}forecast"):
            forecast.append(elem.attrib)
        return self.msg(forecast)

    def msg(self,forecast):
        msg_data = ""
        fmt = "\n%s              %s    %s   %s\n"%("日期","天气","最高温","最低温")
        msg_data += fmt
        for i in forecast:
            msg_data += "%s        %s    %s    %s"%(i['date'],i['text'],i['high'],i['low'])
            msg_data +="\n"
        return msg_data

if __name__ == "__main__":
    w = GetWeather()
    print w.weather
