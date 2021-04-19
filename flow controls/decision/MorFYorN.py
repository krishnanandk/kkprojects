age=int(input("enter age"))
sex=input("sex")
mar=input("martial status")

if(sex=="f"):
    print("place of service is urban areas only")
elif(sex=="m"):
    if(20<age<40):
        print("service of work is anywhere")
    elif(40<age<60):
        print("service of work is in urban areas only")
    else:
        print ("ERROR")