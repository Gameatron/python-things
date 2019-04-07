age = int(input("Age: "))
zoneMax = round(maxHeartRate * 0.80)
print(f'The "cardio zone" is from {zoneMin} to {zoneMax} bpm.')
zoneMin = round(maxHeartRate * 0.60)
print(f'The maximum heart rate for a {age}-year-old is {maxHeartRate}.')
maxHeartRate = 220 - age