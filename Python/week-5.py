s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
name=input("Enter student/'s name: ")
if name ==s1[0] :
    print(name,sum(s1[1:7]))
elif name ==s2[0] :
    print(name,sum(s2[1:7]))
elif name ==s3[0] :
    print(name,sum(s3[1:7]))
else:
    print("Student is not recorded")
