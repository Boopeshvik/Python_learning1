#Height = input("Enter your Height")
#Height = float(Height)
#Weight = input("Enter your Weight")
#Weight = float(Weight)
#BMI = (Weight/(Height*2))*100
#print(f"{BMI} is your BMI")
#if BMI>30:
   # print("Obesity")
#elif BMI>=25 and BMI<=29:
  #  print("Overweight")
#elif BMI>=18.5 and BMI<=25:
  #  print("Normal")
#elif BMI<18.5:
 #   print("Underweight")

#n = input("Enter the Number:")
#n =int(n)
#if n % 2 !=0:
   # print("Weird")
#else:
   # if n >=2 and n <=5:
        #print("Not Weird")
    #elif n >=6 and n <=20:
      #  print("Weird")
    #elif n > 20:
       # print ("Not Weird")

#Height = input ("Enter Your Height:")
#Weight = input ("Enter your Weight:")
#Height = int(Height)
#Weight = float (Weight)
#bmi = Weight / (Height ** 2)
#print (bmi)

#if bmi < 30:
 #   print("Obesity")
#elif bmi > 25 and bmi < 30:
 #   print("Over Weight")
#elif bmi > 18.5 and bmi < 25:
 #   print ("Normal")
#elif bmi < 18.5:
 #   print ("Weak")

#India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
#USA = ["New York","Chicago","Las Vegas", "San Francisco"]
#UK = ["London", "Manchester", "Liverpool", "Nottingham"]

#city = input("Enter the city name:")
#if city in India:
 #   print(f'{city} is in India')
#elif city in USA:
 #   print(f'{city} is in USA')
#elif city in UK:
 #   print(f'{city} is in UK')
#else:
 #   print(f'{city} not in any list')

India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York","Chicago","Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

City_1 = input("Enter the first city Name:")
City_2 = input("Enter the Second city Name:")
if City_1 in India and City_2 in India:
    print(f'{City_1, City_2} are in India')
elif City_1 in USA and City_2 in USA:
    print(f'{City_1,City_2} are in USA')
elif City_1 in UK and City_2 in UK:
    print(f'{City_1, City_2} are in UK')
else:
    print(f'{City_1,City_2} are not in list')