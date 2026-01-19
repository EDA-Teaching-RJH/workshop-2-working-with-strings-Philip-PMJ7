def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")

def pounds_to_float(d):
    pounds = float(d.replace("£", ""))
    return pounds

def percent_to_float(p):
    percent = float(p.replace("%", ""))
    percent = percent * 0.01
    return percent

main()
