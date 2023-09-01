#n = 6
#for i in range(n,1,-1):
 # for j in range(1,i):
  #  print(j,end='')
  #print()

#sum = 0
#for i in range(1,21):
 #   if i % 2 == 0:
  #    sum= i + sum
#print(sum)

dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
total = 0
for i in dice_result:
  if i ==6:
    total +=1
print(total)

