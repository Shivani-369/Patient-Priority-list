#research
d={"Janaki Deva":"Medium","Hemant Ram":"Low","Hari Gopal":"High","Shruthika":"Medium"}
m=[]
for k,v in d.items():
    if v=="High":
        m.append(k)
for k,v in d.items():
    if v=="Medium":
        m.append(k)
for k,v in d.items():
    if v=="Low":
        m.append(k)
print("priority list",m)
print("highest priority",m[0])


