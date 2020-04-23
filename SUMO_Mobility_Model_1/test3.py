from __future__ import absolute_import
from __future__ import print_function
from xml.etree.ElementTree import parse

from collections import defaultdict

import os
import sys
import optparse
import random
import LSTM
import pandas as pd
# car setting
CarMaxSpeed = "15.00"




# class decleration
class Car:
    MaxLengthToControl = 180

    route_type_to_lane = {}
    route_type_to_lane["start_W"] = 1
    route_type_to_lane["start_E"] = 1
    route_type_to_lane["start_S"] = 1
    route_type_to_lane["start_N"] = 1
    route_type_to_lane["route_WE"] = 1
    route_type_to_lane["route_WN"] = 2
    route_type_to_lane["route_WS"] = 0
    route_type_to_lane["route_EW"] = 1
    route_type_to_lane["route_EN"] = 0
    route_type_to_lane["route_ES"] = 2
    route_type_to_lane["route_NE"] = 2
    route_type_to_lane["route_NW"] = 0
    route_type_to_lane["route_NS"] = 1
    route_type_to_lane["route_SE"] = 0
    route_type_to_lane["route_SN"] = 1
    route_type_to_lane["route_SW"] = 2

    def __init__(self, route_type, VehId,v_speed):
        self.route_type = route_type
        self.VehId = VehId
        self.v_speed = v_speed
        self.count = self.MaxLengthToControl * 10 / 15

    def new_to_road(self):
        traci.vehicle.add(self.VehId, self.route_type, typeID="VehicleA", departSpeed=self.v_speed,
                          departLane=self.route_type_to_lane[self.route_type])


        traci.vehicle.setSpeedMode(self.VehId, 0)

    def step(self):
        self.count = self.count - 1
        traci.vehicle.setSpeed(self.VehId, float(self.v_speed))
        traci.vehicle.setSpeedMode(self.VehId, 0)
        # print("Speed ", self.VehId, ":",traci.vehicle.getSpeed(self.VehId), "m / s")
        # print("EdgeID of veh ", self.VehId, ": ",traci.vehicle.getRoadID(self.VehId))

        start = str(traci.vehicle.getRouteID(self.VehId)[6])
        if start == 'W':
            r='route_'+start+"N"
            traci.vehicle.setRouteID(self.VehId, r)
        if start == 'E':
            r = 'route_' + start + "S"
            traci.vehicle.setRouteID(self.VehId, r)
        if start == 'S':
            r = 'route_' + start + "W"
            traci.vehicle.setRouteID(self.VehId,  r)
        if start == 'N':
            r = 'route_' + start + "E"
            traci.vehicle.setRouteID(self.VehId, r)

        if self.count <= 0:
            return True
        else:
            return False

class RoadController:
    def __init__(self):
        self.waiting_dispatch = defaultdict(list)
        self.on_road_car = []

    def dispatch_car_from_waiting(self, step):

        cars = self.waiting_dispatch[step]
        for car in cars:
            car.new_to_road()
            self.on_road_car.append(car)

    def assigned_car(self, step_to_roll_out, car):
        self.waiting_dispatch[step_to_roll_out].append(car)

    def step(self):
        for car in self.on_road_car:
            if car.step():
                self.on_road_car.remove(car)

    def get_car_amount(self):
        return len(self.on_road_car)


class ICACC:

    def __init__(self,road_control, car_amount):
        self.new_car = []
        self.road_control = road_control
        self.start_W = 0.4 * car_amount / 14000
        self.start_E = 0.3 * car_amount / 14000
        self.start_S = 0.3 * car_amount / 14000
        self.start_N = 0.3 * car_amount / 14000

    def generate_car(self, step):
        self.new_car.clear()
        count = 0

        # print(a.pre())
        count = count + 1
        if  random.uniform(0, 1) < self.start_W:
            self.new_car.append(("start_W", "v_{}".format(step)))
            count = count + 1
        if random.uniform(0, 1)< self.start_E:
            self.new_car.append(("start_E", "v_{}".format(step)))
            count = count + 1
        if random.uniform(0, 1)< self.start_S:
            self.new_car.append(("start_S", "v_{}".format(step)))
            count = count + 1
        else:
            self.new_car.append(("start_N", "v_{}".format(step)))
            count = count + 1

        return self.new_car

    def optimize(self, step):
        v=[]
        for n in self.new_car:
            v.append(n)
        v_speed = random.randint(0,float(CarMaxSpeed))
        for (route, veh_name) in v:
            self.road_control.assigned_car(step, Car(route, veh_name,v_speed))
        return self.road_control

# we need to import python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa

# simulation setting
SimulationStepLength = 0.1
SimulationEnding = 2000
SimulationDuration = SimulationEnding / SimulationStepLength
print("Duration of Simulation: " + str(SimulationEnding) + " seconds (" + str(SimulationDuration) + " steps)")


def generate_routefile():  # rou.xml 파일 만듦.
    random.seed(42)  # make tests reproducible
    with open("sumo/cross.rou.xml", "w") as routes:
        print("""<routes>""", file=routes)
        # vehicle configuration of simulation
        print("""
        <vType id="VehicleA" accel="3.5" decel="5.0" sigma="0" length="5" maxSpeed="{}" speedFactor="1.0" minGap="0.0"
        guiShape="passenger" speedDev="0" tau="0.1"/>
        """.format(CarMaxSpeed), file=routes)
        # speedFactor="1.0"   speedDev="0"
        # route configuration of simulation
        print("""
        <route id="start_W" edges="L1"/>
        <route id="start_E" edges="L9"/>
        <route id="start_S" edges="L5"/>
        <route id="start_N" edges="L13"/>
        <route id="route_WE" edges="L1 L2 L11 L12 " />
        <route id="route_WN" edges="L1 L2 L15 L16" />
        <route id="route_WS" edges="L1 L2 L7 L8" />
        <route id="route_EW" edges="L9 L10 L3 L4" />
        <route id="route_EN" edges="L9 L10 L15 L16" />
        <route id="route_ES" edges="L9 L10 L7 L8" />
        <route id="route_NE" edges="L13 L14 L11 L12" />
        <route id="route_NW" edges="L13 L14 L3 L4" />
        <route id="route_NS" edges="L13 L14 L7 L8" />
        <route id="route_SE" edges="L5 L6 L11 L12" />
        <route id="route_SN" edges="L5 L6 L15 L16" />
        <route id="route_SW" edges="L5 L6 L3 L4" />
        """, file=routes)
        print("</routes>", file=routes)


def run(car_amount):
    """execute the TraCI control loop"""
    random.seed(42)
    step = 0
    road_control = RoadController()
    intersection_management = ICACC(road_control,car_amount)

    while True:
        if step < SimulationDuration and step % 10 == 0:
            traci.simulationStep()
            a=intersection_management.generate_car(step)
            # print("dd",a)
            b=intersection_management.optimize(step)
            # print("bb", a)
            # vehicles = traci.vehicle.getIDList()
            # if len(vehicles) !=0:
            #     print("v",vehicles)

        road_control.dispatch_car_from_waiting(step)

        road_control.step()
        traci.simulationStep()

        step += 1
        if road_control.get_car_amount() == 0 and step >= SimulationDuration:
            break
    traci.close()
    sys.stdout.flush()



def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options


# this is the main entry point of this script
if __name__ == "__main__":
    car_amount = 20
    options = get_options()

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # first, generate the route file for this simulation
    generate_routefile()  # rou.xml 만든다.
    #
    traci.start([sumoBinary, "-c", "sumo/cross.sumocfg",
                 "--tripinfo-output", "tripinfo.xml"])

    run(int(car_amount))
