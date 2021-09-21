
    
student_grades=["progress","progress(module trailer)","progress(module trailer)","Do not Progress - module retriever","Do not Progress - module retriever",
                "Do not Progress - module retriever","Do not Progress - module retriever","exclude","exclude","exclude"]
def results():
    for grade in student_grades:
        print(grade)

def histogram():
    p=student_grades.count("progress")
    pi=int(p)*"*"
    pmr=student_grades.count("progress(module trailer)")
    pmri=int(pmr)*"*"
    d=student_grades.count("Do not Progress - module retriever")
    di=int(d)*"*"
    e=student_grades.count("exclude")
    ei=int(e)*"*"
    print(f"progress  {p}   :{pi}  ")
    print(f"Trailing  {pmr}   :{pmri}")
    print(f"Retriever {d}   :{di}  ")
    print(f"excluded  {e}   :{ei}  ")
    print("\n")
    print(p+pmr+d+e," outcomes in total")
results()
print("\n")
histogram()
