l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encode(word, shift):
    list=[]
    for i in word:
        list+=i
    for i in range(len(list)):
        x=l.index(list[i])
        if x+shift>25:
            list[i]=l[l.index(list[i])+shift-26]
        else:
            list[i]=l[l.index(list[i])+shift]
    str=''
    for i in list:
        str+=i
    print("Encoded string as", str)
            
encode('abc', 1)          #just an example





