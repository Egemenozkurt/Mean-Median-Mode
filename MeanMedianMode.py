#Define data
numbers = [30, 45, 17, 54, 25, 54, 80, 60]
len_numbers = len(numbers)
numbers.sort()
#Find Mean
sumNum = sum(numbers) #Calculate sum of all numbers
mean = sumNum / len_numbers #sum of all numbers divided by number of numbers

#Find Median
if len_numbers % 2 == 0:#if there are even number of numbers
    median1 = numbers[len_numbers//2]
    median2 = numbers[len_numbers//2 - 1]
    median = (median1 + median2)/2
else: #if there are odd number of numbers
    median = numbers[len_numbers//2]

#Find Mode
List=[]
counter = 0
while counter < len(numbers):#ordering numbers lowest to highest in new list
    List.append(numbers.count(numbers[counter]))
    counter += 1 
d1 = dict(zip(numbers, List))
mode={k for (k,l) in d1.items() if l == max(List)}

#Print Mean, Median, Mode
print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)

#Could be also found with statistics library
import statistics

print("\nWith statistics library")

#Mean
print("Mean: ", statistics.mean(numbers))
 
#Median
print("Median: ", statistics.median(numbers))

#Mode
print("Mode: ", statistics.multimode(numbers))
