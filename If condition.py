#n = input("Enter the Number: ")
#n = int(n)

#if n % 2 == 0:
     #print("Entered number is Even")
#else:
     #print("Entered number is Odd")

#List_1 =["Chicken","Mutton","Fish"]
#List_2 =["Egg","Pasta","Noodles"]
#List_3 =["carrot","beans","Choc"]

#List = input("Enter the item Name:")
#if List in List_1:
 #    print(f"{List} is under List_1")
#elif List in List_2:
 #    print(f"{List} is under List_2")
#elif List in List_3:
 #    print(f"{List} is under List_3")
#else:
 #    print(f"{List} is not under anything")

#height = input("Enter your height: ")
#height = int(height)
#weight = input("Enter your Weight: ")
#weight = float(weight)
#bmi = weight / (height**2)
#if bmi > 30:
 #   print('Obesity')

#elif bmi > 25 and bmi < 29:
 #   print('Overwieght')

#elif bmi > 18.5 and bmi < 25:
 #   print('Normal')

#elif bmi < 18.5:
 #   print('Underweight')



#India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
#USA = ["New York", "Chicago", "Las Vegas", "San Francisco"]
#UK = ["London", "Manchester", "Liverpool", "Nottingham"]
#c = input("Enter the city name:")
#if c in India:
 #     print(f"{c} is in India")
#elif c in USA:
 #     print(f"{c} is in USA")
#elif c in UK:
 #     print(f"{c} is in UK")
#else:
 #     print(f"{c} is not in anything")

India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York","Chicago","Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

City_1 = input("Enter the First City Name:")
City_2 =input("Enter the Second City Name:")

if City_1 in India and City_2 in India:
      print(f"{City_1,City_2} are in India")
elif City_1 in USA and City_2 in USA:
      print(f"{City_1,City_2} are in USA")
elif City_1 in UK and City_2 in UK:
      print(f"{City_1,City_2} are in UK")
else:
      print(f"{City_1,City_2} are not in anything")

