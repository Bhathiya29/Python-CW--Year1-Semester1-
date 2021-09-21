#part 1
try:
    credit_pass=int(input(" please enter your credits at pass  "))
    credit_defer=int(input(" please enter your credits at defer  "))
    credit_fail=int(input(" please enter your credits at fail  "))


    
    if credit_pass==120:
        print("progress")
    elif credit_pass >=100 and credit_pass <=120:
        print("Progress(module trailer)")
    elif credit_pass <=80 and credit_fail<80:
        print("Do not progress(module retriever)")
    elif credit_fail>=80 :
        print("Exclude")
    

        
except:
    print("Please enter a valid input")
