inp=raw_input()
lines=inp.split(".");
buff=""
print("\n\n\n\n\n")

def printLines(lines):
    for line in lines:
        if(len(line)==1 or line[-2:]=="Dr" or line[-3:]=="Mrs" or line[-2:]== "Mr"):
            buff=line+"."
        elif (line.count("\"")%2==0) and line.count("\"")>1:
            print(line.lstrip()+".")
            buff="";
        elif ('?' in line):
            print("----" +"found questmark" +"---")
            content=line.lstrip().split("?")
            print(buff+content[0]+"?")
            for i in range(1,len(content)-1):
                print(content[i]+"?")
            print(content[len(content)-1]+".")
            buff=""
        elif ('!' in line):
            print("----" +"found !" +"---")
            content=line.lstrip().split("!")
            print(buff+content[0]+"!")
            for i in range(1,len(content)-1):
                print(content[i]+"!")
            print(content[len(content)-1]+".")
            buff=""
        
        else:
            if(len(line.lstrip())>1):
                # print(buff+line.lstrip()+".")  
                buff=""