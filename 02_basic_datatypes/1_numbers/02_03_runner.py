'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

#Calculate speed in miles per second
time_seconds = (30*60) + 30
distance_miles = 10
speed_miles_per_second = distance_miles / time_seconds

#Convert speed (miles per second) to miles per hour
speed_miles_per_hour = speed_miles_per_second * 3600

#Convert speed (miles per hour)to kilometers per hour
speed_kilo_hour = speed_miles_per_hour * 1.6
print(f'The speed in kilometers per hour is {speed_kilo_hour}')
