n=int(input())#按要求输入一个整数
stack=[5,4,3,2,1]
s=stack
while True:#如果下列循环真实，则一直循环下去
    m=s.pop()#取出栈顶的元素，作为字典序中最小的元素
