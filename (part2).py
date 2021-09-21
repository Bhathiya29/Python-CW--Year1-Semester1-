# part 2

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
    elif credit_pass >=100 and credit_pass<=120:
        print("Progress(module trailer)")
    elif credit_pass <=80 and credit_fail<80:
        print("Do not progress(module retriever)")
    elif credit_fail>=80:
        print("Exclude")
    
except:
    print("integer required")    


