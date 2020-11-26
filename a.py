l=["Akash","Sharma","ankit","Nitin","Upender","Aman","Avinash","Pankaj"]
s="a"
s1="A"
a=list(filter(lambda x: x if x[0]==s else x[0]==s1,l))
print(a)