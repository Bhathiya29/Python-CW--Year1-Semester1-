#part3



def R1():
    x=credit_pass
    if x in range(0,121,20):
        print()
    else:
        print("out of range")
def R2():
    y=credit_deffer
    if y in range (0,121,20):
        print()
    else:
        print("out of range")
def R3():
    z=credit_fail
    if z in range(0,121,20):
        print()
    else:
        print("out of range")
            
passed=[ ]
module_trail=[ ]
module_retriever=[ ]
exclude=[ ]
try:

    
    credit_pass=int(input("please enter your credits at pass  "))
    R1()
    credit_deffer=int(input("please enter your credits at deffer  "))
    R2()
    credit_fail=int(input("please enter your credits at fail  "))
    R3()
   

    if credit_pass + credit_deffer + credit_fail!=120:
        print("total incorrect")
    elif credit_pass==120:
        print("progress")
        passed.append("progress")
    elif credit_pass >=100 and credit_pass<=120:
        print("Progress(module trailer)")
        module_trail.append("Progress(module trailer)")
    elif credit_pass <=80 and credit_fail <80:
        print("Do not progress(module retriever)")
        module_retriever.append("No progress(module retriever)")
    elif credit_fail>=80:
        print("Exclude")
        exclude.append("exclude")
    

except:
    print("integer required")
print("\n")
answer=input(" would you like to enter another set of data? \n Enter 'y' for yes and 'q'to quit and see results ")
while "y"== answer:
    
    
    try:
        print("\n")
        credit_pass=int(input("please enter your credits at pass  "))
        R1()
        credit_deffer=int(input("please enter your credits at deffer  "))
        R2()
        credit_fail=int(input("please enter your credits at fail  "))
        R3()
       
        
    

        if credit_pass + credit_deffer + credit_fail!=120:
            print("total incorrect")
        elif credit_pass==120:
           print ("progress")
           passed.append("progress")
        elif credit_pass >=100 and credit_pass<=120:
            print("Progress(module trailer)")
            module_trail.append("Progress(module trailer)")
        elif credit_pass <=80 and credit_fail <80:
            print("Do not progress(module retriever)")
            module_retriever.append("Do not progress(module retriever)")
        elif credit_fail >=80:
            print("Exclude")
            exclude.append("Exclude")
        
    except:
        print("integer required")
    print("\n")
    answer=input(" would you like to enter another set of data? \n Enter 'y' for yes and 'q'to quit and see results ")
else:
    q=str(passed.count("progress"))
    qi=(int(q)*"*")
    w=str(module_trail.count("Progress(module trailer)"))
    wi=(int(w)*"*")
    e=str(module_retriever.count("Do not progress(module retriever)"))
    ei=(int(e)*"*")
    r=str(exclude.count("Exclude"))
    ri=(int(r)*"*")
print("\n")
print(" Horizontal histogram ")
    
print(f" progress  {q}  :{qi}")
print(f" Trailer {w}    :{wi}")
print(f" Retriever {e}  :{ei}")
print(f" Exclude {r}    :{ri}")
print("\n")
all_results=(int(q)+int(w)+int(e)+int(r))
print(all_results, " outcomes in total")



















    
