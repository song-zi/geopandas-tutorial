

import pandas as pd
import geopandas
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, LineString

# 英文教程 https://geopandas.readthedocs.io/en/latest/install.html
# 中文教程 https://www.bbsmax.com/A/Vx5M9KyL5N/

countries = geopandas.read_file(r"geopandas-tutorial-song\data\ne_110m_admin_0_countries\ne_110m_admin_0_countries.shp")
cities = geopandas.read_file(r"geopandas-tutorial-song\data\ne_110m_populated_places")
rivers = geopandas.read_file(r"geopandas-tutorial-song\data\ne_50m_rivers_lake_centerlines")


def print_head_date():
    '''显示前几行数据'''
    __countries = countries
    head = __countries.head()
    print(head)


def print_all_graph():
    '''打印shp'''
    __countries = countries
    __countries.plot()
    # countries.show() the code is wrong
    # 难死我了，终于解决无法show（）的问题了，好多地方给的代码都是错的。
 
    return __countries


def print_area():
    '''打印国家、州、面积'''
    __countries = countries
    area = __countries.geometry.area
    continent = __countries['continent']
    name = __countries['name']
    for i in zip(name, continent, area):
        print(i)


def print_continent(continent):
    '''打印一个部分'''
    __countries = countries
    continent = __countries[__countries['continent'] == continent ]
    continent.plot()
    plt.show()

# print(countries.head())
# print_africa('Asia')


def mean_all():
    '''mean()函数功能：求取均值'''
    __countries = countries
    mean = __countries['pop_est'].mean()
    print('mean is', mean)
    return mean

# mean_all()


def get_centroid(data):
    '''求质心'''
    __countries = data
    # 新增一列，每个国家的中心点
    __countries['geometry'] = __countries.centroid
    # 将新增列设置为几何列
    __countries = __countries.set_geometry('geometry') 
    # __countries.plot()
    # plt.show()
    return __countries

# c = get_centroid(countries)
# c.plot()
# plt.show()


def data_to_shp(data):
    __countries = data
    '''把GeoDataFrame数据导出到shp文件'''
    __countries.to_file(driver='ESRI Shapefile',filename='countries_out.shp')


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



def NDD():
    '''转换GeoSeries中的几何图形到不同的坐标参考系统。
    当前GeoSeries的crs属性必须被设置。
    crs属性需要被指定以用于输出，或是用字典形式或是用EPSG编码方式。'''
    __countries = countries
    __countries = __countries[(__countries['name'] != "Antarctica")]
    countries_mercator = __countries.to_crs(epsg=3395)

    countries_mercator.plot()

    plt.show()


# Note on fiona

def fiona():
    # 'https://blog.csdn.net/theonegis/article/details/80607262
    import fiona
    from shapely.geometry import shape

    with fiona.Env():
        with fiona.open(r"geopandas-tutorial-song\data\ne_110m_admin_0_countries\ne_110m_admin_0_countries.shp") as collection:
            for feature in collection:
                # ... do something with geometry
                geom = shape(feature['geometry'])
                # ... do something with properties
                print(feature['properties']['name'])


def new_gdf():
    '''手动创建一个geodataframe类型数据'''
    df = pd.DataFrame(
        {'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
         'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
         'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
         'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})
    # 把经纬度打包成一列（x, y）
    df['Coordinates']  = list(zip(df.Longitude, df.Latitude))
    # （x, y）把转换成点
    df['Coordinates'] = df['Coordinates'].apply(Point)
    #  把'Coordinates'转换成geometry(几何形状)
    gdf = geopandas.GeoDataFrame(df, geometry='Coordinates')
    ax = countries[countries.continent == 'South America'].plot(
        color='white', edgecolor='black')
    gdf.plot(ax=ax, color='red')
    plt.show()