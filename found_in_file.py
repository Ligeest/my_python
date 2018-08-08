filename = "pi.txt"

with open(filename) as file_obj:
    lines = file_obj.readlines()
pi_string=""
for line in lines:
    pi_string += line.rstrip()
birthday = input('请输入生日')
if birthday in pi_string:
    print ("yes")
else:
    print ("no")
    