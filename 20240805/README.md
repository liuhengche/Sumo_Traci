### [biggerAcc](./analysis/csv/biggerAcc.csv)
```python
#code
def run():
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        
        if "0" in traci.vehicle.getIDList(): 
            traci.vehicle.setAcceleration("0", 5, 100)
        if "1" in traci.vehicle.getIDList():
            traci.vehicle.setAcceleration("1", 5, 100)
        if "test" in traci.vehicle.getIDList():
            traci.vehicle.setAcceleration("test", 5, 100)
        if "2" in traci.vehicle.getIDList():
            traci.vehicle.setAcceleration("2", 5, 100)
        if "3" in traci.vehicle.getIDList():
            traci.vehicle.setAcceleration("3", 5, 100)     
        
        step += 1
    traci.close()
```
- `biggerAcc.py` sets the `acceleration`(max acc) of the vehicle to 5, originally 3.5. We could see that it takes less time, and `edge_speed` increases.
- [`smallerAcc.py`](./analysis/csv/smallerAcc.csv) sets the `acceleration` to 2.

### [laneChangeMode256](./analysis/csv/laneChangeMode256.csv)
```python
#code
def run():
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        
        if "0" in traci.vehicle.getIDList(): 
            traci.vehicle.setLaneChangeMode("0", 256)
        if "1" in traci.vehicle.getIDList():
            traci.vehicle.setLaneChangeMode("1", 256)
        if "test" in traci.vehicle.getIDList():
            traci.vehicle.setLaneChangeMode("test", 256)
        if "2" in traci.vehicle.getIDList():
            traci.vehicle.setLaneChangeMode("2", 256)
        if "3" in traci.vehicle.getIDList():
            traci.vehicle.setLaneChangeMode("3", 256)    
        
        step += 1
    traci.close()
```
- Change the [`laneMode`](https://sumo.dlr.de/docs/TraCI/Change_Vehicle_State.html#lane_change_mode_0xb6) for each vehicle to `256`.
- `256` means that all autonomous lane changing is disabled, but safety checks are still handled with collision avoidance.

### [maxDepartSpeed](./analysis/csv/maxDepartSpeed.csv)
Sets higher departure speed. In this case, the vehicles' departure speed is set to 10. We could see that it takes less time, and `edge_speed` increases, similar to that of `biggerAcc`

### [minGap0](./analysis/csv/minGap0.csv)
```python
#code
def run():
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        if "0" in traci.vehicle.getIDList(): 
            traci.vehicle.setMinGap("0", 0)
        if "1" in traci.vehicle.getIDList():
            traci.vehicle.setMinGap("1", 0)
        if "test" in traci.vehicle.getIDList():
            traci.vehicle.setMinGap("test", 0)
        if "2" in traci.vehicle.getIDList():
            traci.vehicle.setMinGap("2", 0)
        if "3" in traci.vehicle.getIDList():
            traci.vehicle.setMinGap("3", 0)
        step += 1
    traci.close()
```
Sets the minimum distance interval between two successive vehiclees on the same lane. Meaning that we now have a tighter car flow model. We could see that `edge_density` and `edge_occupancy` increases.

### [sigma0](./analysis/csv/sigma0.csv)
```python
#code
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        
        if "0" in traci.vehicle.getIDList(): 
            traci.vehicle.setImperfection("0", 0.5)
        if "1" in traci.vehicle.getIDList():
            traci.vehicle.setImperfection("1", 0.5)
        if "test" in traci.vehicle.getIDList():
            traci.vehicle.setImperfection("test", 0.5)
        if "2" in traci.vehicle.getIDList():
            traci.vehicle.setImperfection("2", 0.5)
        if "3" in traci.vehicle.getIDList():
            traci.vehicle.setImperfection("3", 0.5)    
        
        step += 1
    traci.close()
```
`sigma` represents the `imperfection` of the driver, 0 denotes perfect and optimum driving with no random behaviors while 1 denotes maximum randomness. By default, `sigma` is set to 1. We could see that a significant amount of time is saved.

### [speedDeviation1](./analysis/csv/speedDeviation.csv)

`speedDev` refers to the variability in the speed of vehicles, which indicates the standard deviation of the speed factor for vehicles. In this case, it's set to 1, which means the speed could vary a lot in this type.

### [speedFactor](./analysis/csv/speedFactor.csv)
```python
def run():
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()        
        if "0" in traci.vehicle.getIDList(): 
            traci.vehicle.setSpeedFactor("0", 0.5)
        if "1" in traci.vehicle.getIDList():
            traci.vehicle.setSpeedFactor("1", 0.5)
        if "test" in traci.vehicle.getIDList():
            traci.vehicle.setSpeedFactor("test", 1.5)
        if "2" in traci.vehicle.getIDList():
            traci.vehicle.setSpeedFactor("2", 0.5)
        if "3" in traci.vehicle.getIDList():
            traci.vehicle.setSpeedFactor("3", 0.5)           
        step += 1
    traci.close()
```
`speedFactor` is a multiplier applied to the speed limit of a road to determine the desired speed of a vehicle. In this case, it is set to 0.5 for type `car` and 1.5 for `ev`. So the time needed increased significantly.

### [speedMode](./analysis/csv/speedMode.csv)
```python
def run():
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        
        if "0" in traci.vehicle.getIDList(): 
            traci.vehicle.setSpeedMode("0", 32)
        if "1" in traci.vehicle.getIDList():
            traci.vehicle.setSpeedMode("1", 32)
        if "test" in traci.vehicle.getIDList():
            traci.vehicle.setSpeedMode("test", 32)
        if "2" in traci.vehicle.getIDList():
            traci.vehicle.setSpeedMode("2", 32)
        if "3" in traci.vehicle.getIDList():
            traci.vehicle.setSpeedMode("3", 32)    
        step += 1
    traci.close()
```
In this case, we set the speed mode of the vehicles to 32, meaning that the checks for regarding safe speed, maximum acceleration are all off.

### [tau](./analysis/csv/tau2.csv)
`tau` represents the desired minimum time headway between vehicles, similar to `minGap`. The default `tau` is 1.
```python
def run():
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        
        if "0" in traci.vehicle.getIDList(): 
            traci.vehicle.setTau("0", 200)
        if "1" in traci.vehicle.getIDList():
            traci.vehicle.setTau("1", 200)
        if "test" in traci.vehicle.getIDList():
            traci.vehicle.setTau("test", 200)
        if "2" in traci.vehicle.getIDList():
            traci.vehicle.setTau("2", 200)
        if "3" in traci.vehicle.getIDList():
            traci.vehicle.setTau("3", 200)    
        
        step += 1
    traci.close()
```
When we set the tau to a very large value, we could see that sumo would teleport vehicles since the time headway between successive ones are extremely large.



