"""
ALERTA SÍSMICA DE MÉXICO EN WINDOWS

@ErickMM98

Programa que lee la página del sismológico nacional (SSN) para obtener una sencilla alerta.
"""

import feedparser
from win10toast import ToastNotifier


url_ssn = "http://www.ssn.unam.mx/sismicidad/ultimos/"
xml_ssn = "http://www.ssn.unam.mx/rss/ultimos-sismos.xml"

lim_mag = 5.3

def read_xml_last_sis():
    feed = feedparser.parse(xml_ssn)
    data_sism = feed.entries[0]
    title = data_sism.title

    mag = float(title.split(",")[0])
    lat = data_sism.geo_lat
    lon = data_sism.geo_long

    return title, mag, lat, lon

def make_notificacion(title):
    toaster = ToastNotifier()
    toaster.show_toast("\t\t *** TENEMOS SISMO ***",
                       title,
                       duration=10)


def show_not_windows(_mag,_title):
    if _mag > lim_mag:
        make_notificacion(_title)

if __name__ == '__main__':
    title, mag, lat, lon = read_xml_last_sis()
    show_not_windows(mag,title)
