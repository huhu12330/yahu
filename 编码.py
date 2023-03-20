import urllib.parse

def double_parse(s):
    k=""
    for i in s:
        if(i==urllib.parse.quote(i)):
            by = bytes(i,'UTF-8')    #先将输入的字符串转化成字节码
            hex = by.hex()    #得 
            k+="%"
            k+=hex
        else:
            a=urllib.parse.quote(i)
            k+=a
        ccc=urllib.parse.quote(k)
        return ccc
    




if __name__ == '__main__':
    a=input("请输入进行url字符串:")
    ss=double_parse(a)
    print(ss)

