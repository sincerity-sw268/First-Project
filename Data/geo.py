import math
from math import *
from shapely import geometry
from shapely.geometry import Polygon, Point
import geopandas as gpd

intersection1 = gpd.GeoSeries([Polygon([(37.779335, -122.459830),(37.779248, -122.459825),(37.779246, -122.459934),(37.779332, -122.459936),(37.779335, -122.459830)])])
intersection2 = gpd.GeoSeries([Polygon([(37.777515, -122.459683),(37.777361, -122.459674),(37.777361, -122.459847),(37.777511, -122.459849),(37.777515, -122.459683)])])
intersection3 = gpd.GeoSeries([Polygon([(37.779335, -122.460866),(37.779185, -122.460846),(37.779179, -122.461059),(37.779327, -122.461071),(37.779335, -122.460866)])])
intersection4 = gpd.GeoSeries([Polygon([(37.777469, -122.460742),(37.777297, -122.460727),(37.777295, -122.460896),(37.777459, -122.460894),(37.777469, -122.460742)])])
intersection5 = gpd.GeoSeries([Polygon([(37.779283, -122.461921),(37.779138, -122.461905),(37.779134, -122.462115),(37.779283, -122.462118),(37.779283, -122.461921)])])
intersection6 = gpd.GeoSeries([Polygon([(37.777408, -122.461817),(37.777267, -122.461814),(37.777262, -122.461975),(37.777403, -122.461995),(37.777408, -122.461817)])])
intersection7 = gpd.GeoSeries([Polygon([(37.779219, -122.463018),(37.779091, -122.462997),(37.779091, -122.463187),(37.779217, -122.463185),(37.779219, -122.463018)])])
intersection8 = gpd.GeoSeries([Polygon([(37.777359, -122.462870),(37.777210, -122.462854),(37.777205, -122.463038),(37.777349, -122.463039),(37.777359, -122.462870)])])
intersection9 = gpd.GeoSeries([Polygon([(37.779168, -122.464091),(37.779053, -122.464078),(37.779043, -122.464247),(37.779166, -122.464266),(37.779168, -122.464091)])])
intersection10 = gpd.GeoSeries([Polygon([(37.777317, -122.463966),(37.777156, -122.463945),(37.777150, -122.464138),(37.777311, -122.464140),(37.777317, -122.463966)])])

road1 = gpd.GeoSeries([Polygon([(37.779335, -122.459830), (37.779248, -122.459825), (37.779229, -122.458769),(37.779375, -122.458769),(37.779335, -122.459830)])])
road2 = gpd.GeoSeries([Polygon([(37.777515, -122.459683),(37.777361, -122.459674),(37.777205, -122.458634),(37.777633, -122.458656),(37.777515, -122.459683)])])
road3 = gpd.GeoSeries([Polygon([(37.779332, -122.459936),(37.779335, -122.459830),(37.781176, -122.459938),(37.781170, -122.460095),(37.779332, -122.459936)])])
road4 = gpd.GeoSeries([Polygon([(37.779246, -122.459934), (37.779248, -122.459825), (37.777515, -122.459683),(37.777511, -122.459849),(37.779246, -122.459934)])])
road5 = gpd.GeoSeries([Polygon([(37.777361, -122.459847), (37.777361, -122.459674), (37.775586, -122.459529),(37.775596, -122.459703),(37.777361, -122.459847)])])
road6 = gpd.GeoSeries([Polygon([(37.779335, -122.460866),(37.779185, -122.460846),(37.779246, -122.459934),(37.779332, -122.459936),(37.779335, -122.460866)])])
road7 = gpd.GeoSeries([Polygon([(37.777469, -122.460742),(37.777297, -122.460727), (37.777361, -122.459847),(37.777511, -122.459849),(37.777469, -122.460742)])])
road8 = gpd.GeoSeries([Polygon([(37.779327, -122.461071),(37.779335, -122.460866),(37.781103, -122.461008),(37.781082, -122.461175),(37.779327, -122.461071)])])
road9 = gpd.GeoSeries([Polygon([(37.779185, -122.460846),(37.777469, -122.460742),(37.777459, -122.460894),(37.779179, -122.461059),(37.779185, -122.460846)])])
road10 = gpd.GeoSeries([Polygon([(37.777295, -122.460896),(37.777297, -122.460727),(37.775529, -122.460598),(37.775532, -122.460776),(37.777295, -122.460896)])])
road11 = gpd.GeoSeries([Polygon([(37.779283, -122.461921),(37.779138, -122.461905),(37.779179, -122.461059),(37.779327, -122.461071),(37.779283, -122.461921)])])
road12 = gpd.GeoSeries([Polygon([(37.777408, -122.461817),(37.777267, -122.461814),(37.777295, -122.460896),(37.777459, -122.460894),(37.777408, -122.461817)])])
road13 = gpd.GeoSeries([Polygon([(37.779283, -122.461921),(37.781048, -122.462055),(37.781048, -122.462259),(37.779283, -122.462118),(37.779283, -122.461921)])])
road14 = gpd.GeoSeries([Polygon([(37.779134, -122.462115),(37.779138, -122.461905),(37.777408, -122.461817),(37.777403, -122.461995),(37.779134, -122.462115)])])
road15 = gpd.GeoSeries([Polygon([(37.777262, -122.461975),(37.777267, -122.461814),(37.775489, -122.461676),(37.775491, -122.461847),(37.777262, -122.461975)])])
road16 = gpd.GeoSeries([Polygon([(37.779219, -122.463018),(37.779091, -122.462997),(37.779134, -122.462115),(37.779283, -122.462118),(37.779219, -122.463018)])])
road17 = gpd.GeoSeries([Polygon([(37.777359, -122.462870),(37.777210, -122.462854),(37.777262, -122.461975),(37.777403, -122.461995),(37.777359, -122.462870)])])
road18 = gpd.GeoSeries([Polygon([(37.779219, -122.463018),(37.781008, -122.463137),(37.781002, -122.463308),(37.779217, -122.463185),(37.779219, -122.463018)])])
road19 = gpd.GeoSeries([Polygon([(37.779091, -122.463187),(37.779091, -122.462997),(37.777359, -122.462870),(37.777349, -122.463039),(37.779091, -122.463187)])])
road20 = gpd.GeoSeries([Polygon([(37.777205, -122.463038),(37.777210, -122.462854),(37.775432, -122.462745),(37.775428, -122.462910),(37.777205, -122.463038)])])
road21 = gpd.GeoSeries([Polygon([(37.779168, -122.464091),(37.779053, -122.464078),(37.779091, -122.463187),(37.779217, -122.463185),(37.779168, -122.464091)])])
road22 = gpd.GeoSeries([Polygon([(37.777317, -122.463966),(37.777156, -122.463945),(37.777205, -122.463038),(37.777349, -122.463039),(37.777317, -122.463966)])])

class Geo():
    """
    sub class
    cell과 es 반경 설정.
    """
    def boundary(self):  # cell 반경
        boundary_geo=[(37.780891, -122.464204),(37.781078, -122.458946),(37.775532, -122.458495),(37.775450, -122.463837)]
        geo = gpd.GeoSeries([Polygon(boundary_geo)])
        return geo

    def road(self,veh):
        road=[]
        time = []
        for i in veh:
            xy = Point(float(i[0]), float(i[1]))
            if (intersection1.contains(xy).bool() == True):
                road.append('intersection1')
                time.append(i[2])
            elif (intersection2.contains(xy).bool() == True):
                road.append('intersection2')
                time.append(i[2])
            elif (intersection3.contains(xy).bool() == True):
                road.append('intersection3')
                time.append(i[2])
            elif (intersection4.contains(xy).bool() == True):
                road.append('intersection4')
                time.append(i[2])
            elif (intersection5.contains(xy).bool() == True):
                road.append('intersection5')
                time.append(i[2])
            elif (intersection6.contains(xy).bool() == True):
                road.append('intersection6')
                time.append(i[2])
            elif (intersection7.contains(xy).bool() == True):
                road.append('intersection7')
                time.append(i[2])
            elif (intersection8.contains(xy).bool() == True):
                road.append('intersection8')
                time.append(i[2])
            elif (road1.contains(xy).bool() == True):
                road.append('road1')
                time.append(i[2])
            elif (road2.contains(xy).bool() == True):
                road.append('road2')
                time.append(i[2])
            elif (road3.contains(xy).bool() == True):
                road.append('road3')
                time.append(i[2])
            elif (road4.contains(xy).bool() == True):
                road.append('road4')
                time.append(i[2])
            elif (road5.contains(xy).bool() == True):
                road.append('road5')
                time.append(i[2])
            elif (road6.contains(xy).bool() == True):
                road.append('road6')
                time.append(i[2])
            elif (road7.contains(xy).bool() == True):
                road.append('road7')
                time.append(i[2])
            elif (road8.contains(xy).bool() == True):
                road.append('road8')
                time.append(i[2])
            elif (road9.contains(xy).bool() == True):
                road.append('road9')
                time.append(i[2])
            elif (road10.contains(xy).bool() == True):
                road.append('road10')
                time.append(i[2])
            elif (road11.contains(xy).bool() == True):
                road.append('road11')
                time.append(i[2])
            elif (road12.contains(xy).bool() == True):
                road.append('road12')
                time.append(i[2])
            elif (road13.contains(xy).bool() == True):
                road.append('road13')
                time.append(i[2])
            elif (road14.contains(xy).bool() == True):
                road.append('road14')
                time.append(i[2])
            elif (road15.contains(xy).bool() == True):
                road.append('road15')
                time.append(i[2])
            elif (road16.contains(xy).bool() == True):
                road.append('road16')
                time.append(i[2])
            elif (road17.contains(xy).bool() == True):
                road.append('road17')
                time.append(i[2])
            elif (road18.contains(xy).bool() == True):
                road.append('road18')
                time.append(i[2])
            elif (road19.contains(xy).bool() == True):
                road.append('road19')
                time.append(i[2])
            elif (road20.contains(xy).bool() == True):
                road.append('road20')
                time.append(i[2])
            elif (road21.contains(xy).bool() == True):
                road.append('road21')
                time.append(i[2])
            elif (road22.contains(xy).bool() == True):
                road.append('road22')
                time.append(i[2])
            else:
                road=[]
                time=[]
        # print("road",road)
        return road,time


# c1 = CellES().cell()
#
# xy = Point(37.778788,-122.467078)
# print("A",c1.contains(xy))
# xy = Point(37.781306, -122.467926)
# print("A",c1.contains(xy))

# es_center=CellES().es_center()
# print("b",es_center)

 # intersection1 = [(37.779335, -122.459830),(37.779248, -122.459825),(37.779246, -122.459934),(37.779332, -122.459936)]
        # intersection2=[(37.777515, -122.459683),(37.777361, -122.459674),(37.777361, -122.459847),(37.777511, -122.459849)]
        # intersection3=[(37.779335, -122.460866),(37.779185, -122.460846),(37.779179, -122.461059),(37.779327, -122.461071)]
        # intersection4=[(37.777469, -122.460742),(37.777297, -122.460727),(37.777295, -122.460896),(37.777459, -122.460894)]
        # intersection5=[(37.779283, -122.461921),(37.779138, -122.461905),(37.779134, -122.462115),(37.779283, -122.462118)]
        # intersection6=[(37.777408, -122.461817),(37.777267, -122.461814),(37.777262, -122.461975),(37.777403, -122.461995)]
        # intersection7=[(37.779219, -122.463018),(37.779091, -122.462997),(37.779091, -122.463187),(37.779217, -122.463185)]
        # intersection8=[(37.777359, -122.462870),(37.777210, -122.462854),(37.777205, -122.463038),(37.777349, -122.463039)]
        # intersection9=[(37.779168, -122.464091),(37.779053, -122.464078),(37.779043, -122.464247),(37.779166, -122.464266)]
        # intersection10=[(37.777317, -122.463966),(37.777156, -122.463945),(37.777150, -122.464138),(37.777311, -122.464140)]
        #
        # boundary_road1 = [(37.779335, -122.459830), (37.779248, -122.459825), (37.779229, -122.458769),(37.779375, -122.458769)]
        # road1 = gpd.GeoSeries([Polygon(boundary_road1)])
        # boundary_road2 = [(37.777515, -122.459683),(37.777361, -122.459674),(37.777205, -122.458634),(37.777633, -122.458656)]
        # road2 = gpd.GeoSeries([Polygon(boundary_road2)])
        # boundary_road3 = [(37.779332, -122.459936),(37.779335, -122.459830),(37.781176, -122.459938),(37.781170, -122.460095) ]
        # road3 = gpd.GeoSeries([Polygon(boundary_road3)])
        # boundary_road4 = [(37.779246, -122.459934), (37.779248, -122.459825), (37.777515, -122.459683),(37.777511, -122.459849)]
        # road4 = gpd.GeoSeries([Polygon(boundary_road4)])
        # boundary_road5 = [(37.777361, -122.459847), (37.777361, -122.459674), (37.775586, -122.459529),(37.775596, -122.459703)]
        # road5 = gpd.GeoSeries([Polygon(boundary_road5)])
        # boundary_road6 = [(37.779335, -122.460866),(37.779185, -122.460846),(37.779246, -122.459934),(37.779332, -122.459936)]
        # road6 = gpd.GeoSeries([Polygon(boundary_road6)])
        # boundary_road7 = [(37.777469, -122.460742),(37.777297, -122.460727), (37.777361, -122.459847),(37.777511, -122.459849)]
        # road7 = gpd.GeoSeries([Polygon(boundary_road7)])
        # boundary_road8 = [(37.779327, -122.461071),(37.779335, -122.460866),(37.781103, -122.461008),(37.781082, -122.461175) ]
        # road8 = gpd.GeoSeries([Polygon(boundary_road8)])
        # boundary_road9 = [(37.779185, -122.460846),(37.777469, -122.460742),(37.777459, -122.460894),(37.779179, -122.461059)]
        # road9 = gpd.GeoSeries([Polygon(boundary_road9)])
        # boundary_road10 = [(37.777295, -122.460896),(37.777297, -122.460727),(37.775529, -122.460598),(37.775532, -122.460776)]
        # road10 = gpd.GeoSeries([Polygon(boundary_road10)])
        # boundary_road11 = [(37.779283, -122.461921),(37.779138, -122.461905),(37.779179, -122.461059),(37.779327, -122.461071)]
        # road11 = gpd.GeoSeries([Polygon(boundary_road11)])
        # boundary_road12= [(37.777408, -122.461817),(37.777267, -122.461814),(37.777295, -122.460896),(37.777459, -122.460894)]
        # road12 = gpd.GeoSeries([Polygon(boundary_road12)])
        # boundary_road13 = [(37.779283, -122.461921),(37.781048, -122.462055),(37.781048, -122.462259),(37.779283, -122.462118)]
        # road13 = gpd.GeoSeries([Polygon(boundary_road13)])
        # boundary_road14 = [(37.779134, -122.462115),(37.779138, -122.461905),(37.777408, -122.461817),37.777403, -122.461995]
        # road14 = gpd.GeoSeries([Polygon(boundary_road14)])
        # boundary_road15 = [(37.777262, -122.461975),(37.777267, -122.461814),(37.775489, -122.461676),(37.775491, -122.461847)]
        # road15 = gpd.GeoSeries([Polygon(boundary_road15)])
        # boundary_road16 = [(37.779219, -122.463018),(37.779091, -122.462997),(37.779134, -122.462115),(37.779283, -122.462118)]
        # road16 = gpd.GeoSeries([Polygon(boundary_road16)])
        # boundary_road17 = [(37.777359, -122.462870),(37.777210, -122.462854),(37.777262, -122.461975),(37.777403, -122.461995)]
        # road17= gpd.GeoSeries([Polygon(boundary_road17)])
        # boundary_road18 = [(37.779219, -122.463018),(37.781008, -122.463137),(37.781002, -122.463308),(37.779217, -122.463185)]
        # road18 = gpd.GeoSeries([Polygon(boundary_road18)])
        # boundary_road19 = [(37.779091, -122.463187),(37.779091, -122.462997),(37.777359, -122.462870),(37.777349, -122.463039)]
        # road19 = gpd.GeoSeries([Polygon(boundary_road19)])
        # boundary_road20 = [(37.777205, -122.463038),(37.777210, -122.462854),(37.775432, -122.462745),(37.775428, -122.462910)]
        # road20 = gpd.GeoSeries([Polygon(boundary_road20)])
        # boundary_road21 = [(37.779168, -122.464091),(37.779053, -122.464078),(37.779091, -122.463187),(37.779217, -122.463185)]
        # road21 = gpd.GeoSeries([Polygon(boundary_road21)])
        # boundary_road22 = [(37.777317, -122.463966),(37.777156, -122.463945),(37.777205, -122.463038),(37.777349, -122.463039)]
        # road22 = gpd.GeoSeries([Polygon(boundary_road22)])


