import math
import argparse
import sys

parser = argparse.ArgumentParser(
    description="Annuity and Differentiated Payment Calculation")
parser.add_argument("--type", '-t', choices=["diff", 'annuity'])
args_parsed = sys.argv

parser.add_argument("--interest", '-i', type=float)
parser.add_argument("--principal", '-pr', type=float)
parser.add_argument("--payment", '-pa',  type=float)
parser.add_argument("--periods", '-pe', type=int)

args = parser.parse_args()

loan_principal = args.principal
annuity = args.payment
number_of_monthly_payments = args.periods
loan_interest = args.interest
interest_rate = loan_interest and loan_interest / 100 * 1 / 12

args_list = [loan_principal, annuity,
             number_of_monthly_payments, loan_interest]


def calculator():

    if not args.type or len(args_parsed) < 5 or any((type(i) is int or type(i) is float) and i < 0 for i in args_list):
        print('Incorrect Parameters')
        return

    if args.type == 'annuity':
        if annuity and number_of_monthly_payments and loan_interest:
            result = round(annuity / ((interest_rate * math.pow(1 + interest_rate, number_of_monthly_payments)
                                       ) / (math.pow(1 + interest_rate, number_of_monthly_payments) - 1)))
            print(f"Your loan principal = {result}!")
            print(
                f'Overpayment = {abs(math.ceil((annuity * number_of_monthly_payments) - result))}')

        elif loan_interest and number_of_monthly_payments and loan_principal:
            result = math.ceil(loan_principal * (interest_rate * math.pow(1 + interest_rate, number_of_monthly_payments)
                                                 ) / (math.pow(1 + interest_rate, number_of_monthly_payments) - 1))
            print(f"Your annuity payment = {result}!")
            print(
                f'Overpayment = {abs(math.ceil((result * number_of_monthly_payments) - loan_principal))}')
        else:
            result = math.ceil(math.log((annuity) / (annuity - interest_rate *
                                                     loan_principal), interest_rate + 1))
            years = result // 12
            months = result - (12 * years)
            print(
                f"It will take {str(result) + ' months' if result < 12 else str(years) + ' years, ' + str(months) + ' months'} to repay this loan!")
            print(
                f'Overpayment = {abs(math.ceil((annuity * result) - loan_principal))}')

    elif args.type == 'diff':
        if loan_principal and loan_interest and number_of_monthly_payments:
            total_payments = 0
            for m in range(number_of_monthly_payments):
                result = math.ceil((loan_principal / number_of_monthly_payments) + (interest_rate * (
                    loan_principal - ((loan_principal * (m + 1 - 1)) / number_of_monthly_payments))))
                total_payments += result
                print(f"Month {m + 1}: payment is {result}")
            print(
                f'Overpayment = {abs(math.ceil(total_payments - loan_principal))}')


calculator()
