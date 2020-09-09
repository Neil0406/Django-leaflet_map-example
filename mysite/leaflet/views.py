from django.shortcuts import render
import csv
import pandas as pd
import json
# Create your views here.


def index(request):
    info_path = '~/.../Django-leaflet_map-example/info.csv'       #your info.csv path
    map_path = '~/.../Django-leaflet_map-example/區域經緯度.csv'    #your 區域經緯度.csv path
    info = pd.read_csv(info_path)
    map_ = pd.read_csv(map_path)
    all_list = info.to_dict('recode')
    loc = map_.to_dict('recode')

    _list = []
    for i in loc:
        count = 0
        d = {}
        d['數量'] = 0
        d['座標'] = []
        for j in all_list:
            if str(j['taipei_dist']) != 'nan':
                x = '臺北市' + j['taipei_dist']
                y = '新北市' + j['taipei_dist']
                list_ = []
                if i['行政區名'] == x:
                    d['數量'] = d['數量'] + 1
                elif i['行政區名'] == y:
                    d['數量'] = d['數量'] + 1
            elif str(j['address']) != 'nan' :
                if i['行政區名'][3:] in j['address']:
                    d['數量'] = d['數量'] + 1

        d['區域'] = i['行政區名'][3:]
        d['座標'].append(i['中心點緯度'])           
        d['座標'].append(i['中心點經度'])           
        _list.append(d)

    area = []
    n = []
    lat = []
    lng = []
    for i in _list:
        if i['數量'] != 0:
            area.append(i['區域'])
            n.append(i['數量'])
            lat.append(i['座標'][0])            
            lng.append(i['座標'][1])    
    data = zip(area ,n , lat, lng)

    return render(request, 'index.html',locals())