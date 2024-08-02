#lecture9
#code1
s= "hello world"
print("J"+s[1:6]+"M"+s[7:])
#code2
s= "hello world"
print(s[::2])
#code3
s= "hello world"
print(s[:7:2])
#code4
L1=[10,20,30,40]
print(L1[0])
L1[0]=100
print(L1[0])
#code5
S= "Raheja College"
def test():
    count =0
    for aplha in S:
        if aplha== "e":
            count= count + 1
            print(count)
test()
