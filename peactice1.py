

import pandas as pd
import geopandas
import matplotlib.pyplot as plt

countries = geopandas.read_file(r"geopandas-tutorial-song\data\ne_110m_admin_0_countries\ne_110m_admin_0_countries.shp")


def print_head_date(__data):
    '''显示前几行数据'''
    head = __data.head()
    print(head)


def print_all_graph(__data):
    '''打印shp'''
    __data.plot()
    # countries.show() the code is wrong
    # 难死我了，终于解决无法show（）的问题了，好多地方给的代码都是错的。
 
    return __data


def print_area(__data):
    '''打印国家、州、面积'''
    __area = __data.geometry.area
    __continent = __data['continent']
    name = __data['name']
    for i in zip(name, __continent, __area):
        print(i)


def print_africa():
    '''打印一个部分'''
    __africa = countries[countries['continent'] == 'Africa']
    __africa.plot()
    plt.show()

def mean_all(__data):
    '''mean()函数功能：求取均值'''
    __mean = __data['pop_est'].mean()
    print('mean is', __mean)
    return __mean

def get_centroid(__data):
    '''求质心'''
    # 新增一列，每个国家的中心点
    __data['geometry'] = __data.centroid
    # 将新增列设置为几何列
    __data = __data.set_geometry('geometry') 
    # __data.plot()
    # plt.show()
    return __data

def data_to_shp(__data):
    '''把GeoDataFrame数据导出到shp文件'''
    __data.to_file(driver='ESRI Shapefile',filename='world_out.shp')


point = get_centroid(countries)

date_to_shp(point)

