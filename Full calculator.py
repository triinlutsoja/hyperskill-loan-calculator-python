# cmd-line: "python creditcalc.py --principal=1000000 --periods=60 --interest=10"

# First, you should parse the provided parameters to define,
# which ones are known and which one is missing.
import argparse
import math
import sys

parser = argparse.ArgumentParser(description='This program should calculate the missing parameter')

parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")
parser.add_argument("--type")

args = parser.parse_args()
n_arguments = (len(sys.argv))

cant_continue = n_arguments < 5 or args.type == None or args.interest == None
if cant_continue:
    print("Incorrect parameters.")
    sys.exit()

if args.principal is not None:
    principal = float(args.principal)
    if float(args.principal) < 0:
        print("Incorrect parameters")
else:
    principal = None

if args.periods is not None:
    periods = int(args.periods)
    if int(args.periods) < 0:
        periods = None
        print("Incorrect parameters")
else:
    periods = None

if args.interest is not None:
    interest = float(args.interest) / 1200
    if float(args.interest) < 0:
        print("Incorrect parameters")
else:
    interest = None
    # print("Incorrect parameters")

if args.payment is not None:
    payment = float(args.payment)
    if float(args.payment) < 0:
        print("Incorrect parameters")
    if args.type == "diff":
        print("Incorrect parameters")
else:
    payment = None

if args.type == "annuity":
    type = "annuity"
elif args.type == "diff":
    type = "diff"
else:
    type = None
    print("Incorrect parameters")

# Second. Compute the missing value using the formulas mentioned above.
# The calculator should be able to calculate the number of monthly payments,
# the monthly payment amount, and the loan principal.

def calculate_monthly_payment(principal, periods, interest):
    nominator = interest * ((1 + interest) ** periods)
    denominator = ((1 + interest) ** periods - 1)
    m_payment = math.ceil(principal * (nominator/denominator))
    return m_payment

def calculate_loanprincipal(interest, payment, periods):
    lower_nominator = (interest * ((1 + interest) ** periods))
    lower_denominator = (1 + interest) ** periods -1
    upper_denominator = (lower_nominator / lower_denominator)
    loan_principal = math.floor(payment / upper_denominator)
    return loan_principal
def calculate_n_payments(principal, interest, payment):
    n_payments = math.ceil(math.log(payment / (payment - (interest * principal)), (1 + interest)))
    return n_payments

def calculate_diff_payments(interest, periods, principal):
    for current_repayment_month in range(1, (periods + 1)):
        diff_payment = math.ceil(float((principal / periods) + interest * (principal - ((principal * (current_repayment_month - 1)) / periods))))
        print("Month", str(current_repayment_month), ": payment is", diff_payment)
        current_repayment_month += 1

def calculate_overpayment(interest, periods, principal):
    if type == "annuity":
        over_payment = (payment * periods) - principal
        print("Overpayment = " + str(int(over_payment)))
    elif type == "diff":
        over_payment = 0 - principal
        for current_repayment_month in range(1, (periods + 1)):
            diff_payment = math.ceil(float((principal / periods) + interest * (principal - ((principal * (current_repayment_month - 1)) / periods))))
            over_payment += diff_payment
            current_repayment_month += 1
        print("Overpayment = " + str(int(over_payment)))
def months_to_years_and_months(number_of_months):
    result = "It will take "
    years = int(number_of_months / 12)
    if years == 1:
        result += str(years) + " year"
    elif years > 1:
        result += str(years) + " years"
    months = int(number_of_months % 12)
    if months == 1:
        if years == 0:
            result += str(months) + " month"
        else:
            result += " and " + str(months) + " month"
    elif months > 1:
        if years == 0:
            result += str(months) + " months"
        else:
            result += " and " + str(months) + " months"
    result += " to repay this loan!"
    return result



# Finally, output the value users wanted to compute.

if payment == None and principal is not None and periods is not None and interest is not None and type is not None:
    if type == "annuity":
        payment = calculate_monthly_payment(principal, periods, interest)
        print("Your monthly payment = " + str(payment) + "!")
        calculate_overpayment(interest, periods, principal)
    if type == "diff":
        calculate_diff_payments(interest, periods, principal)
        print("")
        calculate_overpayment(interest, periods, principal)

if principal == None and payment is not None and periods is not None and interest is not None and type is not None:
    principal = calculate_loanprincipal(interest, payment, periods)
    print("Your loan principal = " + str(principal) + "!")
    calculate_overpayment(interest, periods, principal)

if periods == None and principal is not None and payment is not None and interest is not None and type == "annuity":
    periods = calculate_n_payments(principal, interest, payment)
    print(months_to_years_and_months(periods))
    calculate_overpayment(interest, periods, principal)