from geo import Geo
from shapely import geometry
from shapely.geometry import Polygon, Point
import geopandas as gpd

import time,datetime
class AppendData:
    """
    데이터 전처리
    cell과 edge server위치 데이터에 추가
    """

    def __init__(self, data):
        self.dataset = data

    def extract_vid(self):
        """
        데이터셋에서 존재하는 v_id 즉, 차량들 다 추출.
        """

        veh = []
        road = []
        tim=[]
        # temp=[]
        geo = Geo().boundary()

        for i in self.dataset:
            dataset_s = i.split(' ')  # Remove "\n"
            xy = Point(float(dataset_s[0]), float(dataset_s[1]))
            if (geo.contains(xy).bool() == True):
                time = datetime.datetime.fromtimestamp(int(dataset_s[3])).strftime('%H:%M:%S')
                # print("time[3]",time[0:2],datetime.datetime.fromtimestamp(int(dataset_s[3])).strftime('%H'))
                veh.append([float(dataset_s[0]), float(dataset_s[1]),time])
        if len(veh) >= 2:
            geo_road,t = Geo().road(veh)
            if len(geo_road) >=2:
                print("geo",geo_road)
                print("t",t)
                for i in range(0,len(t)-1):
                    # print("??",t[i+1],t[i])
                    if (int(t[i+1][0:2]) - int(t[i][0:2])) == 0:
                        if i == (len(t)-2):
                           if ((int(t[i + 1][0:2]) - int(t[i][0:2])) == 0) and ((int(t[i][0:2]) - int(t[i-1][0:2])) == 0):
                               road.append(geo_road[i])
                               tim.append(t[i])
                               road.append(geo_road[i+1])
                               tim.append(t[i+1])
                        else:
                            road.append(geo_road[i])
                            tim.append(t[i])

                    elif i !=0 and (int(t[i][0:2]) - int(t[i-1][0:2])) == 0:
                        road.append(geo_road[i])
                        tim.append(t[i])



        return veh,road,tim

