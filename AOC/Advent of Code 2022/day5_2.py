import time
start = time.time()
lines = open("day5.txt").readlines()
q1 = "RCH"
q2 = "FSLHJB"
q3 = "QTJHDMR"
q4 = "JBZHRGS"
q5 = "BCDTZFPR"
q6 = "GCHT"
q7 = "LWPBZVNS"
q8 = "CGQJR"
q9 = "SFPHRTDL"
data = [0,q1,q2,q3,q4,q5,q6,q7,q8,q9]

for x in lines:
    x = x.split()
    a = data[int(x[3])][:int(x[1])]
    data[int(x[3])] = data[int(x[3])][int(x[1]):]
    data[int(x[5])] = a + data[int(x[5])]

# for i in range(9):
#     print(data[i+1][0])

print(time.time()-start)