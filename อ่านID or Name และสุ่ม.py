import re
import random

# อ่านข้อมูลจากไฟล์
with open("province.sql", "r", encoding="utf-8") as province_sql:
    lines = province_sql.readlines()

# เก็บข้อมูล ID หรือ Name
entries = []
for line in lines:
    match = re.search(r"VALUES\s*\((.+?)\);", line)
    if match:
        values = match.group(1)  # ข้อมูลในวงเล็บ VALUES(...)
        split_values = [v.strip().replace("'", "") for v in values.split(",")]
        if len(split_values) >= 2:
            id_value = split_values[0]  # ID
            name_value = split_values[1]  # Name
            entries.append((id_value, name_value))  # เก็บ ID และ Name

# สุ่มลำดับข้อมูล
random.shuffle(entries)

# เขียนผลลัพธ์ใหม่ลงไฟล์ .txt โดยเลือกแค่ ID หรือ Name
with open("province_Random.txt", "w", encoding="utf-8") as output_file:
    for id_value, name_value in entries:
        # เขียนแค่ ID หรือ Name ลงไฟล์
        output_file.write(f"{id_value} {name_value}\n")  # สามารถเปลี่ยนเป็นแค่ ID หรือแค่ Name ได้
