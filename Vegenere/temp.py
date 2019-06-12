m = []
p = m[0]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]

print(ne)
t1 = arr
t2 = arr
i=0
while i<17:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1

print(t1)
print()

p = m[1]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]
print(ne)
t1 = arr
t2 = arr
i=0
while i<14:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1
print(t1)
print()

p = m[2]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]
print(ne)
t1 = arr
t2 = arr
i=0
while i<3:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1
print(t1)
print()

p = m[3]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]
print(ne)
t1 = arr
t2 = arr
i=0
while i<6:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1

print(t1)
print()

p = m[4]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]
print(ne)
t1 = arr
t2 = arr
i=0
while i<11:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1

print(t1)
print()

p = m[5]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]
print(ne)
t1 = arr
t2 = arr
i=0
while i<1:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1

print(t1)
print()

p = m[6]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]
print(ne)
t1 = arr
t2 = arr
i=0
while i<16:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1

print(t1)
print()

p = m[7]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]
print(ne)
t1 = arr
t2 = arr
i=0
while i<5:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1

print(t1)
print()

j=0
m = []
p=""
while (j<8):
    i=j
    p=""
    while (i<len(a)):
        print(a[i],end="")
        p=p+a[i]
        i = i + 8
    j += 1
    m.append(p)
    print()


# for i in arr:
#     print(i,end = " ")
# print()
# for i in ne:
#     print(i,end = " ")
# f = []
# for p in m:
#     i=0
#     arr[26]={0}
#
key = [17, 14, 25, 6, 11, 1, 16, 5]
keyf = []
p = 0
for i in key:
    p = i + 65
    keyf.append(chr(p))
print(keyf)
j=0
plain = ""

for i in a:
    dif = ord(i) - ord(keyf[j])
    if dif >= 0:
        dif = dif + 25
    else:
        dif = 91 + dif
    plain = plain + chr(dif)
    j = ( j + 1 ) % 8
print(plain)
