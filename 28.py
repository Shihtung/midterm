a=input("輸入第一列: ")
b=input("輸入第二列: ")
a1=a.split(" ")
b1=b.split(" ")
det=(int(a1[0])*int(b1[1]))-(int(a1[1])*int(b1[0]))
print(str(int(b1[1])/det)+" "+str(int(b1[0])/-det))
print(str(int(a1[1])/-det)+" "+str(int(a1[0])/det))