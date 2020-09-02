#pylint: disable=unused-variable
#pylint: disable=anomalous-backslash-in-string

import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta
from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError
from urllib.request import urlretrieve

source_columns = ['FIPS','Admin2','Province_State','Country_Region','Lat','Long_','Confirmed','Deaths']

source_path = {'non_kr':'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/','kr_snapshot':'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun='}

target_path = {'summary':'time_series_covid19.csv','geo':'UID_ISO_FIPS_LookUp_Table.csv'}

target_columns = ['Date','adm0_a3','Province/State','Country/Region','Lat','Long','Population','Confirmed','r_Confirmed','i_Confirmed','ri_Confirmed','Tot_Confirmed','iTot_Confirmed','rTot_Confirmed','riTot_Confirmed','Deaths','r_Deaths','i_Deaths','ri_Deaths','Tot_Deaths','iTot_Deaths','rTot_Deaths','riTot_Deaths']

def get_datelist(data,gaps=5):
    # Get last available date to applicable form
    start_dt = datetime.strptime(data['Date'][len(data)-1],'%m/%d/%y').date()
    end_dt = date.today()

    if start_dt < end_dt-timedelta(days=1):
        start_dt -= timedelta(days=gaps)

    appendlist = [(start_dt + timedelta(days=x)).strftime('%m-%d-%Y')+'.csv' for x in range(1,(end_dt-start_dt).days + 1)]

    print(appendlist)
    return appendlist


def read_current():
    # Read current summary file (local)
    file_list = target_path['summary']

    # Current data to be updated
    last = pd.read_csv(target_path['summary'])
    new = last.copy()

    # Get file list to be appended
    append_file = get_datelist(last)
    write_date = ''

    for iter, file_list in enumerate(append_file):
        # Generate file path on Github (Only global files are to be updated, KCDC data to be added)
        # try:
        #     print("Reading Daily global data with the filename: "+file_list)
        #     ds = read_source(file_list,last)
        #     # ds = pd.read_csv(file_path,usecols=read_columns) # daily timeseries
        #     # ds = clean_data(ds)
        #     #
        #     # write_date_w = file_list.split('.')[0]
        #     # column_name = set_colname(file_list.split('.')[0])
        #     #
        #     # if column_name in new_wc.columns:
        #     #     new_wc = new_wc.drop(column_name,axis=1)
        #     # if column_name in new_wd.columns:
        #     #     new_wd = new_wd.drop(column_name,axis=1)
        # except HTTPError:   # Data backlog or time differences
        #     print(file_list+" not found")
        #     break






    # Read remote source from GitHub and KCDC
    # ds = read_source()
    # start_date = get_startdate(ds)
    # new = ds
    #
    # write_date = datetime.strptime(ds.iloc[-1]['Date'],'%m/%d/%y').strftime('%m-%d-%Y')
    #
    # # Write to files
    # write_file(new,'new',write_date)


def read_source(file_list,last_data,start_date=None):
    # Read global data (GitHub)
    file_path = source_path['non_kr']+file_list
    try:
        print("Reading Daily global data with the filename: "+file_list)
        non_kr_ds = pd.read_csv(file_path,usecols=source_columns)
        kr_ds = last_data
        # Transform
        non_kr_ds = clean_data(non_kr_ds)
        kr_ds = clean_data(kr_ds)




#     # wc = pd.read_csv("data/"+src_path['wc'])
#     # wd = pd.read_csv("data/"+src_path['wd'])
#     # # Geographical information will be merged
#     # wc.drop(['Lat','Long'],axis=1,inplace=True)
#     # wd.drop(['Lat','Long'],axis=1,inplace=True)
#     #
#     # # Read KR data
#     # kc = pd.read_csv("data/"+src_path['kc'])
#     # kd = pd.read_csv("data/"+src_path['kd'])
#     # # Geographical information will be merged
#     # kc.drop(['Lat','Long'],axis=1,inplace=True)
#     # kd.drop(['Lat','Long'],axis=1,inplace=True)
#
#     # Read US data
#     uc = pd.read_csv(src_path['uc'])
#     ud = pd.read_csv(src_path['ud'])
#     uc.rename(columns={'iso3':'adm0_a3','Province_State':'Province/State','Country_Region':'Country/Region','Long_':'Long'},inplace=True)
#     ud.rename(columns={'iso3':'adm0_a3','Province_State':'Province/State','Country_Region':'Country/Region','Long_':'Long'},inplace=True)
#
#     # County-level data to be purged
#     uc.drop(['UID','iso2','code3','Admin2','FIPS','Combined_Key'],axis=1,inplace=True)
#     ud.drop(['UID','iso2','code3','Admin2','FIPS','Combined_Key'],axis=1,inplace=True)
#
#     # Append Population column to infections data
#     uc = pd.concat([uc.iloc[:,:5],ud['Population'],uc.iloc[:,5:]],axis=1)
#
#     # Read geographical information
#     geo = pd.read_csv("data/"+src_path['geo'])
#     geo.rename(columns={'iso3':'adm0_a3','Province_State':'Province/State','Country_Region':'Country/Region','Long_':'Long'},inplace=True)
#     geo.drop(['UID','iso2','code3','Admin2','FIPS','Combined_Key'],axis=1,inplace=True)
#
#     # Clean and group datasets
#     wc, wd, kc, kd, uc, ud = clean_data(wc, wd, kc, kd, uc, ud, geo)
#     confirmed = group_by_type(wc,kc,uc,'Confirmed')
#     deaths = group_by_type(wd,kd,ud,'Deaths')
#
#     covid = confirmed.merge(deaths,on=['Date','adm0_a3','Province/State','Country/Region','Lat','Long','Population'])
#
#     # print(covid)
#
#     return covid

if __name__ == '__main__':
    read_current()
