with open("file1.txt") as file1:
  list1 = file1.readlines()
    
with open("file2.txt") as file2:
  list2 = file2.readlines()
    
result = [int(num) for num in list1 if num in list2]
 
print(result)


'''
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)

#file = open("new_file.txt")
#contents = file.read()
#print(contents)
#file.close()
with open("weather_data.csv", mode="r", encoding="utf-8") as file:
    contents = file.read()
    print(contents)


with open("weather_data.csv", mode="w", encoding="utf-8") as file:
    file.write("Chris,46.5")


'''new_list = [new_item for item in list]'''
'''example: new_list = [n + 1 for n in numbers]
'''
