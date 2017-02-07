"""Without using inbuilt fns"""
myfile1=open("C:\\Users\\nandi\\PycharmProjects\\Practice\\coderbyte\\file1.txt", "rb")
k1= myfile1.readlines()
print k1

myfile2=open("C:\\Users\\nandi\\PycharmProjects\\Practice\\coderbyte\\file2.txt", "rb")
k2= myfile2.readlines()
print k2

myfile3=open("C:\\Users\\nandi\\PycharmProjects\\Practice\\coderbyte\\file3.txt", "rb")
k3= myfile3.readlines()
print k3

myfile4=open("C:\\Users\\nandi\\PycharmProjects\\Practice\\coderbyte\\file4.txt", "rb")
k4= myfile4.readlines()
print k4

myfile5=open("C:\\Users\\nandi\\PycharmProjects\\Practice\\coderbyte\\file5.txt", "rb")
k5= myfile5.readlines()
print k5

myfile=open("C:\\Users\\nandi\\PycharmProjects\\Practice\\coderbyte\\filemerge.txt", "wb")
k=myfile.write("Merging all files  \n ")
k= myfile.writelines(k1)
k= myfile.writelines(k2)
k= myfile.writelines(k3)
k= myfile.writelines(k4)
k= myfile.writelines(k5)

#Method 2

files=["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]
for file in files:
    f=open(file,"rb")
    k=f.readlines()
    l=open("merge.txt", "ab")
    l.write("Merge file")
    l.writelines(k)


