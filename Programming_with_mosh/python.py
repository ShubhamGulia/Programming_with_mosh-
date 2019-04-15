# print ('Assignment-1')
#
# print("Hospital")
# patient_name= "John_Smith"
# age= 20
# is_new= True
# print("----------------")
# print ('Assignment-2')
# name= input("What's your name? ")
# color=input("Whats your favourite color? ")
# print("Hi, "+name+" likes "+color)
# print("----------------")
# print ('Assignment-3')
# weight=input("Enter the weight( in pounds ): ")
# weight=float(weight)
# weight_KG= weight/2.2
# print("Your Weight(in KG's): "+ str(weight_KG))
# print("Need to convert float to str for concatenation")
# print("----------------")
# print ('Assignment-4')
# name = "Jennifer"
# print(name[1:-1])
# print("----------------")
# print ('Assignment-5')
# x= 10+3*2**2
# print(x)
# x=(2+3)*10-3
# print(x)
# print("----------------")
# print ('Assignment-6')
# price=1000000
# good_credit=False
# if good_credit:
#     print("Estimated price for approval: " + str(0.10*price))
# else:
#     down_payment=0.2*price
#     print(f"Down payment: {down_payment}")
#     print("Estimated price for approval: " + str(0.20 * price))

# print("----------------")
# print ('Assignment-7')
# customer = {
#     "name" : "John Smith",
#     "age": 30,
#     "is_verified": True
# }
# print(customer.keys())
# print(customer.get("name"))
# print("----------------")
# phone={
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine"
# }
# Str_Phone= ""
# Phone= input()
# for number in Phone:
#     Str_Phone += phone.get(number,"!") + " "
#     # gives ! , will be printed if string is not matched
# print(f'hi there {Str_Phone}')
# print("----------------")
# print ('Assignment-1')
# class Person:
#     def __init__(self,name,talk):
#         self.name=name
#         self.talk=talk
#
# person= Person("Shubham", "LOL!!!")
# person1= Person("Shubham1", "LOL1!!!")
#
# print(person.name)
# print(person.talk)
# print(person1.name)
# print(person1.talk)
# import random
#
#
# class Dice:
#     def roll(self):
#         first= random.randint(1,6)
#         second = random.randint(1,6)
#         print ((first, second))
#         #numbers=((1,1),(1,2),(1,3),(1,4),(1,5),(1,6))
#         #print(random.choice(numbers))
#
#
# crazy = Dice()
# crazy.roll()

# print("----------------")
# print ('Assignment-openpyxl')
# pip install openpyxl
# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference
#
#
# wb = xl.load_workbook('transactions.xlsx')
# sheet = wb['Sheet1']
#
# cell = sheet['a1']
#
# cell = sheet.cell(1,1)
#
# print(cell.value)
# print("----------------")
# print(sheet.max_row)
# print("----------------")
#
# for row in range (2, sheet.max_row +1):
#     cell= sheet.cell (row, 3)
#     print(cell.value)
#     corrected_price =cell.value*0.9
#     corrected_price_cell =sheet.cell(row,4)
#     corrected_price_cell.value= corrected_price
#
# values = Reference(sheet,
#                    min_row=2,
#                    max_row=sheet.max_row,
#                    min_col=4,
#                    max_col=4)
# chart= BarChart()
# chart.add_data(values)
# sheet.add_chart(chart)
# wb.save('transaction2.xlsx')

#print("--------------------")

#print ("Creating a function that could do this task from thousands for a file in a sec")


# pip install openpyxl
# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference
#
# def process_workbook(filename):
#
#     wb = xl.load_workbook('filename')
#     sheet = wb['Sheet1']
#
#     cell = sheet['a1']
#
#     cell = sheet.cell(1,1)
#
#     print(cell.value)
#     print("----------------")
#     print(sheet.max_row)
#     print("----------------")
#
#     for row in range (2, sheet.max_row +1):
#         cell= sheet.cell (row, 3)
#         print(cell.value)
#         corrected_price =cell.value*0.9
#         corrected_price_cell =sheet.cell(row,4)
#         corrected_price_cell.value= corrected_price
#
#     values = Reference(sheet,
#                        min_row=2,
#                        max_row=sheet.max_row,
#                        min_col=4,
#                        max_col=4)
#     chart= BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart)
#     wb.save('filename')
#
#

# print("----------------")

# print ('Machine Learning project ')

# print("----------------")

# print ('Assignment-1')

# print("----------------")
