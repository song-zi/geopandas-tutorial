

import pandas as pd
import geopandas
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, LineString


countries = geopandas.read_file(r"geopandas-tutorial-song\data\ne_110m_admin_0_countries\ne_110m_admin_0_countries.shp")
cities = geopandas.read_file(r"geopandas-tutorial-song\data\ne_110m_populated_places")
rivers = geopandas.read_file(r"geopandas-tutorial-song\data\ne_50m_rivers_lake_centerlines")


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


def area_and_distance():
    p = Point(0, 0)
    polygon = Polygon([(1, 1), (2,2), (2, 1)])
    # 多边形面积
    a = polygon.area
    # 点到多边形的距离
    d = polygon.distance(p)
    print(a)
    print(d)

def show_together():
    '''Plotting our different layers together'''
    # 轮廓，填充，尺寸
    ax = countries.plot(edgecolor='green', facecolor='none', figsize=(15, 10))
    rivers.plot(ax=ax, )
    cities.plot(ax=ax, color='red')
    # 设置显示的经纬度
    ax.set(xlim=(-20, 60), ylim=(-40, 40))
    return ax

ax = show_together()

plt.show()