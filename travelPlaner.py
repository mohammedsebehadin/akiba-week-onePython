# Destination
# Distance in kilometers
# Average speed in km/h
destination=input("ur destination")
distance=float(input("distance from ur place"))
speed=float(input("the average speed u goes per hour"))
print("estimated travel time",distance/speed)
timeByHour=distance/speed;
print("the estimated travel time ", timeByHour*60)
minute=timeByHour*60
second=print("the estimated travel time by second",minute*60)
