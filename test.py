#count = 0
#while count < 8:
    #print(count)
    #count += 1

def rekenmachine(machine):
    sum_total = sum(machine)
    return sum_total

exp = [45.2, 732.01, 65, 78.4]

print(rekenmachine(exp))



def calculate_savings(income, expenses):
    savings = income - expenses
    return f"Total savings: ${savings:.2f}"

def simple_interest(principal, rate, time):
    interest = principal * (rate / 100) * time
    return f"Simple interest: ${interest:.2f}"

def compound_interest(principal, rate, times_compound, years):
    amount = principal * (rate / 100 / times_compound) ** (times_compound * years)
    interest = amount - principal
    return f"Compound interest: ${interest:.2f}"

command = input("Which command would you like to run fool? Options: expenses, ask_name ")

#if command == "ask_name":
    #name = ask_name()
    #print(f"Hello, {name}!")

if  command == "compound_interest":
    principal = input("What is the principal? ")
    rate = input("What is the rate? ")
    times_compound = ("How many times is the interest compounded per year? ")
    years = ("For how many years? ")
    print(compound_interest(principal, rate, times_compound, years))

elif command == "simple_interest":
    principal = input("")
    rate = input("")
    time = input("")
    print(simple_interest(principal, rate, time))

else:
    print("invalid command")