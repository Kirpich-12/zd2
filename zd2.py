data_s =  open('input.txt', 'r')
data = data_s.read()
n = int(data)
ans = 0 #значение для ответа

if int(data) > 0:
    for i in range(1, n + 1):
        ans += i
else:
    for i in range(n ,2):
        ans += i



output_data = open('output.txt', 'w')
output_data.write(str(ans))
#запись

data_s.close()
output_data.close()
#ОБЯЗАТЕЛЬНО не забывать
