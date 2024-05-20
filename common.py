l1=[1,2,3,4]
l2=[3,4,5,6]
def common_ele(l1,l2):
    l3=[]
    for i in l1:
        if i in l2:
            l3.append(i)

    return l3
            
print(common_ele(l1,l2))
