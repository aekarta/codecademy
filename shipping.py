weight=41.5

#Ground Shipping
if (weight<=2):
  cost=weight*1.5+20
elif(weight<=6):
  cost=weight*3+20
elif(weight<=10):
  cost=weight*4+20
else:
  cost=weight*4.75+20
print("Ground shipping:",cost)

#Ground Shipping Premium
cost_premium=125.00
print("Ground shipping Premium:",cost_premium)

#Drone shipping
if (weight<=2):
  cost=weight*4.5
elif(weight<=6):
  cost=weight*9
elif(weight<=10):
  cost=weight*12
else:
  cost=weight*14.25
print("Drone shipping:",cost)
