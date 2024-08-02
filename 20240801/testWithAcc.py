import os
import sys
import optparse


# we need to import python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa


def generate_routefile():
    # not needed if you have the .rou.xml
    return


def run():
    # main logic of using TraCI
    # step = 0
    # for step in range(3600):
    #     if 'veh0' in traci.vehicle.getIDList():
    #         traci.vehicle.setSpeed('veh0', 5.0)
    #         traci.vehicle.setAccel('veh0', 1)
    #     traci.simulationStep()
    # traci.close()
    # sys.stdout.flush()
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        if 'test' in traci.vehicle.getIDList():
            if step == 22:
                traci.vehicle.setAcceleration("test",5.0,13)
            if step == 33:
                traci.vehicle.setAcceleration("test", -5.0, 23)
            if step == 58:
                traci.vehicle.setAcceleration("test", 5.0, 13)
        step += 1
    traci.close()

def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options


# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # first, generate the route file for this simulation
    #generate_routefile(), not needed

    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    traci.start([sumoBinary, "-c", "test.sumocfg"])
    run()
