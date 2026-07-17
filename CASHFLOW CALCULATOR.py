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




npbt = surplus + int_div + prop_div + gen_res + tax_provided

print("\n--- Non-Cash & Non-Operating Adjustments ---")
depreciation = input("Enter Depreciation for the year: ")
goodwill = input("Enter Goodwill amortized: ")
gain_on_sale = input("Enter Gain on sale of fixed assets: ")


operating_profit_bwc = npbt - depreciation + goodwill + gain_on_sale

print("\n--- Working Capital Changes ---")
inc_current_assets = int(input("Enter total Increase in Current Assets: "))
dec_current_assets = int(input("Enter total Decrease in Current Assets: "))
inc_current_liabilities = int(input("Enter total Increase in Current Liabilities: "))
dec_current_liabilities = int(input("Enter total Decrease in Current Liabilities: "))


cash_generated = operating_profit_bwc + inc_current_assets - dec_current_assets - inc_current_liabilities + dec_current_liabilities


final_cash_flow = cash_generated - tax_paid

print("\n-------------------------------------------")
print("Final Cash Flow from Operating Activities is: " + final_cash_flow)



print("\n--- Cash Flow from Investing Activities ---")
sale_fa = input("Enter proceeds from sale of Fixed Assets: ")
purch_fa = int(input("Enter purchase of Fixed Assets: "))
int_received = int(input("Enter Interest Received on investments: "))
div_received = int(input("Enter Dividend Received on investments: "))


investing_cf = sale_fa + purch_fa - int_received - div_received

print("Net Cash from Investing Activities: " + investing_cf)




print("\n--- Cash Flow from Financing Activities ---")
issue_shares = int(input("Enter proceeds from issue of Share Capital: "))
repay_loan = int(input("Enter repayment of Bank Loan: "))
int_paid = int(input("Enter Interest Paid on debentures/loans: "))
div_paid = input("Enter Dividend Paid during the year: ") 

bank_od_change = input("Did Bank Overdraft increase or decrease? (Inc/Dec): ")


if bank_od_change == 'Inc' or 'inc' or 'INC':
    od_amt = int(input("Enter amount of increase: "))
elif bank_od_change == 'Dec' or 'dec' or 'DEC':
    od_decrease = int(input("Enter amount of decrease: "))
    od_amt = od_decrease * -1


financing_cf = issue_shares + repay_loan + int_paid + div_paid - od_amt

print("Net Cash from Financing Activities: " + financing_cf)




print("\n--- Net Increase/Decrease in Cash & Cash Equivalents ---")


total_cash_flow = final_cash_flow + investing_cf + financing_cf

opening_cash = int(input("Enter Opening Cash & Cash Equivalents: "))


closing_cash = total_cash_flow - opening_cash 

print("Calculated Closing Cash & Cash Equivalents: ", closing_cash)

actual_closing = int(input("Enter actual Closing Cash & Cash Equivalents from Balance Sheet: "))

if closing_cash is actual_closing:  
    print("Match successful! Cash Flow Statement tallied.")
else:
    print("Mismatch found. Please check calculations.")
