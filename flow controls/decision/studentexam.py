attend=float(input("num of classes attended"))
held=float(input("num of classes held"))
percentage=(attend/held)*100
if(percentage>75):
    print("allowed")
else:
    print("not allowed")