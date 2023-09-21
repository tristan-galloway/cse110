"""

student: tristan galloway
teacher: brother keers
file:
goal: implement a simplistic system to determine if a user can qualify for a loan.

"""

print("On a scale of 1-10:")
# How large is the loan?
loan = int(input("How large is the loan? "))
# How good is your credit history?
credit = int(input("How good is your credit history? "))
# How high is your income?
income = int(input("How high is your income? "))
# How large is your down payment?
payment = int(input("How large is your down payment? "))

decision = False

# check if the loan size is at least 5
if loan >= 5:
    # If the credit history and income are both at least 7, then the decision is "yes"
    if credit >= 7 and income >= 7:
        decision = True
     # If either the credit history or income is at least 7, then check if the down payment is at least 5, if it is, the decision is "yes"
    elif credit >= 7 or income >= 7:
        if payment >= 5:
            decision = True
        else:
            decision = False
    # Otherwise (if neither the credit history nor income is at least 7), the decision is "no"
    else:
        decision = False
# Otherwise (if the loan is not 5 or greater)
else:
    # If the credit is less than 4, then the decision is "no"
    if credit <= 4:
        decision = True
    # If the credit is more than 4  
    else:
        # If either the income or the down payment is at least 7, the decision is "yes"
        if income >= 7 or payment >= 7:
            decision = True
        # If both the income and the down payment are at least 4, then the answer is "yes"
        elif income >= 4 and payment >= 4:
            decision = True
        # Otherwise, the decision is "no"
        else:
            decision = False

# Display the decision to the user
if decision == True:
    print("\nCongradulations, you have been approved for you loan.")
else:
    print("\nSorry, you will not be receiving a loan this time around.")