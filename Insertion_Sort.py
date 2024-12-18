
import time

start_time = time.time()

with open("province_Random.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  
    
def InsertionSort(a_list):
    n = len(a_list)
    
    for i in range(1,n):
        
        temp = a_list[i]
        hole = i
        
        while hole>0 and a_list[hole-1]<temp:
            a_list[hole] = a_list[hole-1]
            hole = hole-1
            
        a_list[hole] = temp
        
    return a_list

a = InsertionSort(lines)

sorted_lines = InsertionSort(lines)
end_time = time.time()
elapsed_time = end_time - start_time

for line in a:
    print(line.strip())

print(f"เวลาที่ใช้: {elapsed_time} วินาที")
