#expense = [1000,2000,3000,4000,6000]
#total_expense = 0
#for i in expense:
 #   total_expense = total_expense + i

#print(f"{total_expense} is the answer")
#for i in range(len(expense)):
 #   r = expense[i]
  #  print(f'Month {i+1}, Expense:{r}')
   # total_expense = r + total_expense
#print("Total Expense:",total_expense)

#expense =[1000,1500,2100,1600,2200]

#for i,r in enumerate (expense):
 #   if r>2000:
  #      print(f"Month{i+1} has expense more than 2000")
   #     break

location =["sofa","bed","table","chair","xxx"]
key_place = "chair"

for i in location:
    if i == key_place:
        print("Key is found in",i)
    else:
        print("key is not found in", i)
