#program to calculate cashflow

#operating activities
n_surplus = int(input("Enter Current Year P/L Bal: "))
o_surplus = int(input("Enter Previous Year P/L Bal: "))

surplus = n_surplus - o_surplus

int_div = int(input("Enter Current Year interim dividend: "))
prop_div = int(input("Enter Previous Year proposed dividend: "))

n_gen_res = int(input("Enter Current Year general reserve: "))
o_gen_res = int(input("Enter Previous Year general reserve: "))

gen_res = n_gen_res - o_gen_res

n_tax_prov = int(input("Enter Current Year tax provision: "))
o_tax_prov = int(input("Enter Previous Year tax provision: "))


tax_decision = input("Specify whether there is any adjustment related to tax mentioned below: ")
if tax_decision == 'Yes' or 'YES' or 'yes':
    tax_adjustment = input("Mention the name of the tax ('normal' for income tax and 'other' for others) : ")
    if tax_adjustment == 'Normal' or 'Normal' or 'NORMAL':
        print("Is the tax provided or paid?")
        tax_response1 = input("Answer: ")
        if tax_response1 == "PROVIDED" or "Provided" or "provided":
            print("Tax: Provided")
            tax_provided = input("Enter the amt: ")
        elif tax_response1 == "PAID" or "Paid" or "paid":
            print("Tax: Paid")
            tax_paid = input("Enter the amt: ")
    elif tax_adjustment == "other" or "OTHER" or "Other":
        tax_response2 = input("Mention the name of the tax: ")
        
else:
    print("No necessary adjustments found")
