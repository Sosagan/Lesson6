# В файле Input.txt необбхрдимо написать количество каждой молекулы,к примеру C - 400, H - 500, O - 100
a = []
nums = []
with open('Input', 'r') as file:
    file = file.readlines()
for i in file:
    index = i.rfind(" ") + 1
    number = int(i[index:])
    if i.find("C") != -1 :
        count_C = number // 2
    elif i.find("H") != -1 :
        count_H = number // 6
    elif i.find("O") != -1 :
        count_O = number
output = open("Output.txt", "w")
output.write(str(min(count_C, count_H, count_O)))
output.close()
