def input_user_details():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    gender = input("Enter your gender: ")

    print("Name:", name)
    print("Age:", age)
    print("Email:", email)
    print("Gender:", gender)

def calculate_net_pay():
    rate_of_paye = 0.30
    rate_of_nssf = 0.11
    gross_amount = float(input("Enter your gross amount: "))

    paye = gross_amount * rate_of_paye
    nssf = gross_amount * rate_of_nssf
    net_pay = gross_amount - paye - nssf

    print("Rate of PAYE (30%):", paye)
    print("Rate of NSSF (11%):", nssf)
    print("Gross Amount:", gross_amount)
    print("Net Pay:", net_pay)

input_user_details()
calculate_net_pay()
