# working across sets
#1.union
#2.intersection
#3.difference(except)

outdoor_activities = {"hiking","cycling","swimming"}
indoor_activities = {"gaming","reading","cycling"}

print(outdoor_activities.union(indoor_activities))
print(outdoor_activities.intersection(indoor_activities))
print(outdoor_activities.difference(indoor_activities))
print(outdoor_activities.symmetric_difference(indoor_activities))