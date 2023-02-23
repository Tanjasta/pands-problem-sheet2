# $pythonaccounts.py
# This program reads in a 10 character account number
# Outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs)
# Author: Tatjana Staunton

# Please enter an 10 digit account number: 1234567890
# XXXXXX7890

account_number = input ("Please enter an 10 digit account number:") # we are geting input from the user to enter their acount number
print (account_number) # prints the number entered by the user
print (account_number [-4:]) # prints four last numbers