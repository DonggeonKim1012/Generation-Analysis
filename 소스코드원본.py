pip install requests
import bs4

from urllib.requests import urlopen
from bs4 import BeautifulSoup

class PowerPlant:
    Name=''
    Type_of_Generation=''
    Amount_of_Generation=0
    Month=''

url="http://opendata.kwater.or.kr/openapi-data/service/pubd/electric/elcpReport/list?stDt=2018-01&edDt=2018-12&numOfRows=1219&pageNo=1&ServiceKey=xeBSfOCdLZmd1Ipzi51C7C3Sm4rf2soPNMvcEwNV0zs4JdxHnev0uz21x8e%2BjavbKn%2BJ4Vug48jcJVcOz86iNw%3D%3D"
xml=urlopen(url)
soup=BeautifulSoup(xml.read(), "xml")
Name_list =[]
for i in soup.find_all('elcpwstnNm'):
    Name_list.append(i.get_text())
Type_list=[]
for i in soup.find_all('elcpwstnClsCd'):
    Type_list.append(str(i.get_text()))
Amount_list=[]
for i in soup.find_all('r2'):
    Amount_list.append(int(i.get_text().replace(',','')))
Month_list=[]
for i in soup.find_all('stdrDe'):
    Month_list.append(str(i.get_text()))
Plant_list=[]
for i in range(1219):
    a=PowerPlant()
    a.Name=Name_list[i]
    a.Type_of_Generation=Type_list[i]
    a.Amount_of_Generation=Amount_list[i]
    a.Month=Month_list[i]
    Plant_list.append(a)

Water_Power_Montly_sum=[0,0,0,0,0,0,0,0,0,0,0,0]
Tidal_Power_Montly_sum=[0,0,0,0,0,0,0,0,0,0,0,0]
PhotoVoltaic_Power_Montly_sum=[0,0,0,0,0,0,0,0,0,0,0,0]
Wind_Power_Montly_sum=[0,0,0,0,0,0,0,0,0,0,0,0]
etc_Power_Montly_sum=[0,0,0,0,0,0,0,0,0,0,0,0]
    
for i in Plant_list:
    if i.Type_of_Generation== "0001" or i.Type_of_Generation == "0002":
        if i.Month=="2018-01":
            Water_Power_Montly_sum[0]=Water_Power_Montly_sum[0] + i.Amount_of_Generation
        elif i.Month=="2018-02":
            Water_Power_Montly_sum[1]=Water_Power_Montly_sum[1] + i.Amount_of_Generation
        elif i.Month=="2018-03":
            Water_Power_Montly_sum[2]=Water_Power_Montly_sum[2] + i.Amount_of_Generation
        elif i.Month=="2018-04":
            Water_Power_Montly_sum[3]=Water_Power_Montly_sum[3] + i.Amount_of_Generation
        elif i.Month=="2018-05":
            Water_Power_Montly_sum[4]=Water_Power_Montly_sum[4] + i.Amount_of_Generation
        elif i.Month=="2018-06":
            Water_Power_Montly_sum[5]=Water_Power_Montly_sum[5] + i.Amount_of_Generation
        elif i.Month=="2018-07":
            Water_Power_Montly_sum[6]=Water_Power_Montly_sum[6] + i.Amount_of_Generation
        elif i.Month=="2018-08":
            Water_Power_Montly_sum[7]=Water_Power_Montly_sum[7] + i.Amount_of_Generation
        elif i.Month=="2018-09":
            Water_Power_Montly_sum[8]=Water_Power_Montly_sum[8] + i.Amount_of_Generation
        elif i.Month=="2018-10":
            Water_Power_Montly_sum[9]=Water_Power_Montly_sum[9] + i.Amount_of_Generation
        elif i.Month=="2018-11":
            Water_Power_Montly_sum[10]=Water_Power_Montly_sum[10] + i.Amount_of_Generation
        else:
            Water_Power_Montly_sum[11]=Water_Power_Montly_sum[11] + i.Amount_of_Generation
    elif i.Type_of_Generation== "0003":
        if i.Month=="2018-01":
            Tidal_Power_Montly_sum[0]=Tidal_Power_Montly_sum[0] + i.Amount_of_Generation
        elif i.Month=="2018-02":
            Tidal_Power_Montly_sum[1]=Tidal_Power_Montly_sum[1] + i.Amount_of_Generation
        elif i.Month=="2018-03":
            Tidal_Power_Montly_sum[2]=Tidal_Power_Montly_sum[2] + i.Amount_of_Generation
        elif i.Month=="2018-04":
            Tidal_Power_Montly_sum[3]=Tidal_Power_Montly_sum[3] + i.Amount_of_Generation
        elif i.Month=="2018-05":
            Tidal_Power_Montly_sum[4]=Tidal_Power_Montly_sum[4] + i.Amount_of_Generation
        elif i.Month=="2018-06":
            Tidal_Power_Montly_sum[5]=Tidal_Power_Montly_sum[5] + i.Amount_of_Generation
        elif i.Month=="2018-07":
            Tidal_Power_Montly_sum[6]=Tidal_Power_Montly_sum[6] + i.Amount_of_Generation
        elif i.Month=="2018-08":
            Tidal_Power_Montly_sum[7]=Tidal_Power_Montly_sum[7] + i.Amount_of_Generation
        elif i.Month=="2018-09":
            Tidal_Power_Montly_sum[8]=Tidal_Power_Montly_sum[8] + i.Amount_of_Generation
        elif i.Month=="2018-10":
            Tidal_Power_Montly_sum[9]=Tidal_Power_Montly_sum[9] + i.Amount_of_Generation
        elif i.Month=="2018-11":
            Tidal_Power_Montly_sum[10]=Tidal_Power_Montly_sum[10] + i.Amount_of_Generation
        else:
            Tidal_Power_Montly_sum[11]=Tidal_Power_Montly_sum[11] + i.Amount_of_Generation
            
    elif i.Type_of_Generation== "0004":
        if i.Month=="2018-01":
            PhotoVoltaic_Power_Montly_sum[0]=PhotoVoltaic_Power_Montly_sum[0] + i.Amount_of_Generation
        elif i.Month=="2018-02":
            PhotoVoltaic_Power_Montly_sum[1]=PhotoVoltaic_Power_Montly_sum[1] + i.Amount_of_Generation
        elif i.Month=="2018-03":
            PhotoVoltaic_Power_Montly_sum[2]=PhotoVoltaic_Power_Montly_sum[2] + i.Amount_of_Generation
        elif i.Month=="2018-04":
            PhotoVoltaic_Power_Montly_sum[3]=PhotoVoltaic_Power_Montly_sum[3] + i.Amount_of_Generation
        elif i.Month=="2018-05":
            PhotoVoltaic_Power_Montly_sum[4]=PhotoVoltaic_Power_Montly_sum[4] + i.Amount_of_Generation
        elif i.Month=="2018-06":
            PhotoVoltaic_Power_Montly_sum[5]=PhotoVoltaic_Power_Montly_sum[5] + i.Amount_of_Generation
        elif i.Month=="2018-07":
            PhotoVoltaic_Power_Montly_sum[6]=PhotoVoltaic_Power_Montly_sum[6] + i.Amount_of_Generation
        elif i.Month=="2018-08":
            PhotoVoltaic_Power_Montly_sum[7]=PhotoVoltaic_Power_Montly_sum[7] + i.Amount_of_Generation
        elif i.Month=="2018-09":
            PhotoVoltaic_Power_Montly_sum[8]=PhotoVoltaic_Power_Montly_sum[8] + i.Amount_of_Generation
        elif i.Month=="2018-10":
            PhotoVoltaic_Power_Montly_sum[9]=PhotoVoltaic_Power_Montly_sum[9] + i.Amount_of_Generation
        elif i.Month=="2018-11":
            PhotoVoltaic_Power_Montly_sum[10]=PhotoVoltaic_Power_Montly_sum[10] + i.Amount_of_Generation
        else:
            PhotoVoltaic_Power_Montly_sum[11]=PhotoVoltaic_Power_Montly_sum[11] + i.Amount_of_Generation
    
    elif i.Type_of_Generation== "0006":
        if i.Month=="2018-01":
            Wind_Power_Montly_sum[0]=Wind_Power_Montly_sum[0] + i.Amount_of_Generation
        elif i.Month=="2018-02":
            Wind_Power_Montly_sum[1]=Wind_Power_Montly_sum[1] + i.Amount_of_Generation
        elif i.Month=="2018-03":
            Wind_Power_Montly_sum[2]=Wind_Power_Montly_sum[2] + i.Amount_of_Generation
        elif i.Month=="2018-04":
            Wind_Power_Montly_sum[3]=Wind_Power_Montly_sum[3] + i.Amount_of_Generation
        elif i.Month=="2018-05":
            Wind_Power_Montly_sum[4]=Wind_Power_Montly_sum[4] + i.Amount_of_Generation
        elif i.Month=="2018-06":
            Wind_Power_Montly_sum[5]=Wind_Power_Montly_sum[5] + i.Amount_of_Generation
        elif i.Month=="2018-07":
            Wind_Power_Montly_sum[6]=Wind_Power_Montly_sum[6] + i.Amount_of_Generation
        elif i.Month=="2018-08":
            Wind_Power_Montly_sum[7]=Wind_Power_Montly_sum[7] + i.Amount_of_Generation
        elif i.Month=="2018-09":
            Wind_Power_Montly_sum[8]=Wind_Power_Montly_sum[8] + i.Amount_of_Generation
        elif i.Month=="2018-10":
            Wind_Power_Montly_sum[9]=Wind_Power_Montly_sum[9] + i.Amount_of_Generation
        elif i.Month=="2018-11":
            Wind_Power_Montly_sum[10]=Wind_Power_Montly_sum[10] + i.Amount_of_Generation
        else:
            Wind_Power_Montly_sum[11]=Wind_Power_Montly_sum[11] + i.Amount_of_Generation
            
    else:
        if i.Month=="2018-01":
            etc_Power_Montly_sum[0]=etc_Power_Montly_sum[0] + i.Amount_of_Generation
        elif i.Month=="2018-02":
            etc_Power_Montly_sum[1]=etc_Power_Montly_sum[1] + i.Amount_of_Generation
        elif i.Month=="2018-03":
            etc_Power_Montly_sum[2]=etc_Power_Montly_sum[2] + i.Amount_of_Generation
        elif i.Month=="2018-04":
            etc_Power_Montly_sum[3]=etc_Power_Montly_sum[3] + i.Amount_of_Generation
        elif i.Month=="2018-05":
            etc_Power_Montly_sum[4]=etc_Power_Montly_sum[4] + i.Amount_of_Generation
        elif i.Month=="2018-06":
            etc_Power_Montly_sum[5]=etc_Power_Montly_sum[5] + i.Amount_of_Generation
        elif i.Month=="2018-07":
            etc_Power_Montly_sum[6]=etc_Power_Montly_sum[6] + i.Amount_of_Generation
        elif i.Month=="2018-08":
            etc_Power_Montly_sum[7]=etc_Power_Montly_sum[7] + i.Amount_of_Generation
        elif i.Month=="2018-09":
            etc_Power_Montly_sum[8]=etc_Power_Montly_sum[8] + i.Amount_of_Generation
        elif i.Month=="2018-10":
            etc_Power_Montly_sum[9]=etc_Power_Montly_sum[9] + i.Amount_of_Generation
        elif i.Month=="2018-11":
            etc_Power_Montly_sum[10]=etc_Power_Montly_sum[10] + i.Amount_of_Generation
        else:
            etc_Power_Montly_sum[11]=etc_Power_Montly_sum[11] + i.Amount_of_Generation

sum1=0
for i in Water_Power_Montly_sum:
    sum1= sum1 +i
sum2=0
for i in Tidal_Power_Montly_sum:
    sum2= sum2 +i
sum3=0
for i in PhotoVoltaic_Power_Montly_sum:
    sum3= sum3 +i
sum4=0
for i in Wind_Power_Montly_sum:
    sum4= sum4 +i
sum5=0
for i in etc_Power_Montly_sum:
    sum5= sum5 +i

Water_Power_Montly_sum.extend([sum1,16600000])
Tidal_Power_Montly_sum.extend([sum2,0])
PhotoVoltaic_Power_Montly_sum.extend([sum3,46200000])
Wind_Power_Montly_sum.extend([sum4,111500000])
etc_Power_Montly_sum.extend([sum5,51900000])

nuclear_power = []
with open('데이터 원본 2(원전 호기별 발전량 및 이용률).csv', 'r') as file:
    for lineContent in file:
        nuclear_power.append(lineContent.strip('\n').split(','))
nuclear_sum=0
for i in nuclear_power[1:]:
    nuclear_sum= nuclear_sum + int(i[1])
nuclear_power=['-','-','-','-','-','-','-','-','-','-','-',nuclear_sum,'-',76000000]

import numpy as np
import pandas as pd

data={"수력": Water_Power_Montly_sum, "조력": Tidal_Power_Montly_sum, "태양광": PhotoVoltaic_Power_Montly_sum, "풍력": Wind_Power_Montly_sum, "기타": etc_Power_Montly_sum, "원자력": nuclear_power}
df=pd.DataFrame(data, columns=["수력","조력","태양광","풍력","기타", "원자력"], index=["2018-01","2018-02","2018-03","2018-04","2018-05","2018-06","2018-07","2018-08","2018-09","2018-10","2018-11","2018-12","계","독일2018"])
df
