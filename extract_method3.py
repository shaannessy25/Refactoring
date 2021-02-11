"""Extract Method"""
import math
START_X = 4
START_Y = 4.25

END_X = 53
END_Y = -5.35
# Calculate the distance between the two circle
distance = math.sqrt((START_X-END_X)**2 + (START_Y - END_Y)**2)
print('distance', distance)

START_A = -36
START_B = 97

END_A = .34
END_B = .91
# calcualte the length of vector AB vector which is a vector between A and B points.
length = math.sqrt((START_A-END_A)*(START_A-END_A) +
                   (START_B-END_B)*(START_B-END_B))
print('length', length)
