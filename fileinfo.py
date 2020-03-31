######################
n=int(input())#按要求输入一个整数
stack=[5,4,3,2,1]
s=stack
while True:#如果下列循环真实，则一直循环下去
    m=s.pop()#取出栈顶的元素，作为字典序中最小的元素
    if m%n!=0:#如果m不能整除n的时候
        if m>=1000000:
            continue
        if m%10==1:
            s.append(m*10+5)#让字典序大的先入栈，这样栈顶就是字典序最小的数
            s.append(m*10+3)
        elif m%10==2:
            s.append(m*10+4)
            s.append(m*10+3)
        elif m%10==3:
            s.append(m*10+4)
            s.append(m*10+1)
        elif m%10==4:
            s.append(m*10+5)
        elif m%10==5:
            s.append(m*10+5)
            s.append(m*10+4)
            s.append(m*10+3)
            s.append(m*10+2)
            s.append(m*10+1)
    else:
        print(m)
        break
