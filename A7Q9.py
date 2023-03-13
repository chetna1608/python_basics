vehicles = {'Bicycle', 'Scooter', 'Car', 'Bike', 'Truck', 'Bus', 'Rickshaw'}
heavyVehicles = {'Truck', 'Bus'}
lightVehicles = {'Rickshaw', 'Scooter', 'Bike', 'Bicycle'}

lytVehicles = vehicles - heavyVehicles
print(lytVehicles)

print("    ")
hvyVehicles = vehicles - lightVehicles
print(hvyVehicles)
print("    ")
averageWeightVehicles = lytVehicles & hvyVehicles
print(averageWeightVehicles)
print("    ")
transport = lightVehicles | heavyVehicles
print(transport)
print("    ")
transport.add('Car')
print(transport)
print("    ")
for i in vehicles:
                print(i)
print("    ")
len(vehicles)
print("    ")
min(vehicles)
print("    ")
set.union(vehicles, lightVehicles, heavyVehicles)
