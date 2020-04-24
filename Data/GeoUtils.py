import math
from math import *
from shapely import geometry
from shapely.geometry import Polygon, Point
import geopandas as gpd

es_center = {}


class GeoUtil:
    """
    upper class
    지리적 정보 이용하여 경위도간 거리 측정.
    """

    def calc_offset(d, lat):
        """
        haversine distance 식을 이용해 반경에 따른
        geography상의 x축과 y축의 오프셋 값을 구함.
        """
        return (
            abs(180 * d / 6371 / 1000 / math.pi),
            abs(360 * math.asin(math.sin(d / 6371 / 2 / 1000) / math.cos(lat * math.pi / 180)) / math.pi)
        )

    def radian(degree):
        return math.acos(-1) / 180 * degree

    def coordinate_after_rotation(c, degree, offsets):
        return (
            c[0] + math.cos(GeoUtil.radian(degree)) * offsets[0],
            c[1] + math.sin(GeoUtil.radian(degree)) * offsets[1]
        )

    def degree2radius(degree):
        return degree * (math.pi / 180)

    def hex_coordinates(center_cell):
        # 반경(meter)
        d = 300
        # 866.0254
        rotating_degree = 90  # hexagon cell
        offsets = GeoUtil.calc_offset(d, center_cell[0])
        print("offset",offsets)
        coordinates = [GeoUtil.coordinate_after_rotation(center_cell, d, offsets) for d in
                       range(0, 360 + 1, rotating_degree)]
        return coordinates

    def get_harversion_distance(x1, y1, x2, y2, round_decimal_digits=5):
        """
        경위도 (x1,y1)과 (x2,y2) 점의 거리를 반환.
        Harversion Formula 이용하여 2개의 경위도간 거래를 구함(단위:m).
        """
        R = 6371  # 지구의 반경(단위: km)
        dLat = GeoUtil.degree2radius(x2 - x1)
        dLon = GeoUtil.degree2radius(y2 - y1)

        a = math.sin(dLat / 2) * math.sin(dLat / 2) \
            + (math.cos(GeoUtil.degree2radius(x1)) \
               * math.cos(GeoUtil.degree2radius(x2)) \
               * math.sin(dLon / 2) * math.sin(dLon / 2))
        b = 2 * 1000 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return round(R * b, round_decimal_digits)

    def calc_center(center_cell):
        """
        cell 중심 구하기
        """
        # 반경(meter)
        d = round(300 * math.sqrt(3), 4)  # 866.0254 (500 *루트3)
        rotating_degree = 60  # hexagon cell
        offsets = GeoUtil.calc_offset(d, center_cell[0])

        def coordinate(center_cell, degree, offsets):
            return (
                center_cell[0] + math.sin(GeoUtil.radian(degree)) * offsets[0],
                center_cell[1] + math.cos(GeoUtil.radian(degree)) * offsets[1]
            )

        coordinates = [coordinate(center_cell, d, offsets) for d in range(0, 360 + 1, rotating_degree)]
        return coordinates

    def calc_es_center(center_cell):
        """
        cell 중심 구하기
        """
        # 반경(meter)
        d = 250  # 866.0254 (500 *루트3)
        rotating_degree = 120  # hexagon cell
        offsets = GeoUtil.calc_offset(d, center_cell[0])

        def coordinate(center_cell, degree, offsets):
            return (
                center_cell[0] + math.cos(GeoUtil.radian(degree)) * offsets[0],
                center_cell[1] + math.sin(GeoUtil.radian(degree)) * offsets[1]
            )

        coordinates = [coordinate(center_cell, d, offsets) for d in range(0, 360 + 1, rotating_degree)]
        return coordinates


class CellES(GeoUtil):
    """
    sub class
    cell과 es 반경 설정.
    """
    center_cell1 = (37.777181, -122.466188)
    # center_cell2 = GeoUtil.calc_center(center_cell1)[0]  # -22.889251, -43.27360796190272
    # center_cell3 = GeoUtil.calc_center(center_cell2)[0]  # -22.889251, -43.265153923805435
    # center_cell4 = GeoUtil.calc_center(center_cell1)[4]  # -22.895995912014918, -43.286289019048645
    # center_cell5 = GeoUtil.calc_center(center_cell1)[5]  # -22.895995912014918, -43.27783498095136
    # center_cell6 = GeoUtil.calc_center(center_cell2)[5]  # -22.895995912014918, -43.26938094285408
    # center_cell7 = GeoUtil.calc_center(center_cell5)[4]  # -22.902740824029834, -43.28206221012783
    # center_cell8 = GeoUtil.calc_center(center_cell7)[0]  # -22.902740824029834, -43.27360733136028

    boundary_cell1 = GeoUtil.hex_coordinates(center_cell1)
    # boundary_cell2 = GeoUtil.hex_coordinates(center_cell2)
    # boundary_cell3 = GeoUtil.hex_coordinates(center_cell3)
    # boundary_cell4 = GeoUtil.hex_coordinates(center_cell4)
    # boundary_cell5 = GeoUtil.hex_coordinates(center_cell5)
    # boundary_cell6 = GeoUtil.hex_coordinates(center_cell6)
    # boundary_cell7 = GeoUtil.hex_coordinates(center_cell7)
    # boundary_cell8 = GeoUtil.hex_coordinates(center_cell8)

    def cell(self):  # cell 반경
        print("boundary_cell1",self.boundary_cell1)
        cell1 = gpd.GeoSeries([Polygon(self.boundary_cell1)])
        # cell2 = gpd.GeoSeries([Polygon(self.boundary_cell2)])
        # cell3 = gpd.GeoSeries([Polygon(self.boundary_cell3)])
        # cell4 = gpd.GeoSeries([Polygon(self.boundary_cell4)])
        # cell5 = gpd.GeoSeries([Polygon(self.boundary_cell5)])
        # cell6 = gpd.GeoSeries([Polygon(self.boundary_cell6)])
        # cell7 = gpd.GeoSeries([Polygon(self.boundary_cell7)])
        # cell8 = gpd.GeoSeries([Polygon(self.boundary_cell8)])
        print("cell1",len(cell1))
        return cell1

    # def edgeserver(self):  # edge server 반경
    #
    #     center_cell = [self.center_cell1, self.center_cell2, self.center_cell3, self.center_cell4, self.center_cell5,
    #                    self.center_cell6, self.center_cell7, self.center_cell8]
    #     boundary_cell = [self.boundary_cell1, self.boundary_cell2, self.boundary_cell3, self.boundary_cell4,
    #                      self.boundary_cell5, self.boundary_cell6, self.boundary_cell7, self.boundary_cell8]
    #
    #     for i in range(1, 9):
    #         globals()['c{}_es1'.format(i)] = gpd.GeoSeries([Polygon(
    #             [center_cell[i - 1], boundary_cell[i - 1][1], boundary_cell[i - 1][2], boundary_cell[i - 1][3],
    #              center_cell[i - 1]])])
    #         globals()['c{}_es2'.format(i)] = gpd.GeoSeries([Polygon(
    #             [center_cell[i - 1], boundary_cell[i - 1][3], boundary_cell[i - 1][4], boundary_cell[i - 1][5],
    #              center_cell[i - 1]])])
    #         globals()['c{}_es3'.format(i)] = gpd.GeoSeries([Polygon(
    #             [center_cell[i - 1], boundary_cell[i - 1][5], boundary_cell[i - 1][6], boundary_cell[i - 1][1],
    #              center_cell[i - 1]])])
    #
    #     c1 = [c1_es1, c1_es2, c1_es3]
    #     c2 = [c2_es1, c2_es2, c2_es3]
    #     c3 = [c3_es1, c3_es2, c3_es3]
    #     c4 = [c4_es1, c4_es2, c4_es3]
    #     c5 = [c5_es1, c5_es2, c5_es3]
    #     c6 = [c6_es1, c6_es2, c6_es3]
    #     c7 = [c7_es1, c7_es2, c7_es3]
    #     c8 = [c8_es1, c8_es2, c8_es3]
    #
    #     return c1, c2, c3, c4, c5, c6, c7, c8
    #
    # def es_center(self):
    #     cell1 = GeoUtil.calc_es_center(self.center_cell1)
    #     es_center['C1 ES1'] = cell1[0]
    #     es_center['C1 ES2'] = cell1[1]
    #     es_center['C1 ES3'] = cell1[2]
    #
    #     cell2 = GeoUtil.calc_es_center(self.center_cell2)
    #     es_center['C2 ES1'] = cell2[0]
    #     es_center['C2 ES2'] = cell2[1]
    #     es_center['C2 ES3'] = cell2[2]
    #
    #     cell3 = GeoUtil.calc_es_center(self.center_cell3)
    #     es_center['C3 ES1'] = cell3[0]
    #     es_center['C3 ES2'] = cell3[1]
    #     es_center['C3 ES3'] = cell3[2]
    #
    #     cell4 = GeoUtil.calc_es_center(self.center_cell4)
    #     es_center['C4 ES1'] = cell4[0]
    #     es_center['C4 ES2'] = cell4[1]
    #     es_center['C4 ES3'] = cell4[2]
    #
    #     cell5 = GeoUtil.calc_es_center(self.center_cell5)
    #     es_center['C5 ES1'] = cell5[0]
    #     es_center['C5 ES2'] = cell5[1]
    #     es_center['C5 ES3'] = cell5[2]
    #
    #     cell6 = GeoUtil.calc_es_center(self.center_cell6)
    #     es_center['C6 ES1'] = cell6[0]
    #     es_center['C6 ES2'] = cell6[1]
    #     es_center['C6 ES3'] = cell6[2]
    #
    #     cell7 = GeoUtil.calc_es_center(self.center_cell7)
    #     es_center['C7 ES1'] = cell7[0]
    #     es_center['C7 ES2'] = cell7[1]
    #     es_center['C7 ES3'] = cell7[2]
    #
    #     cell8 = GeoUtil.calc_es_center(self.center_cell8)
    #     es_center['C8 ES1'] = cell8[0]
    #     es_center['C8 ES2'] = cell8[1]
    #     es_center['C8 ES3'] = cell8[2]
    #
    #     return es_center

c1 = CellES().cell()
print("A",c1)

# es_center=CellES().es_center()
# print("b",es_center)



