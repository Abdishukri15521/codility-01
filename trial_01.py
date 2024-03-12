def solution(A, D):
    # Initiazation of the account balance which is zero
    balance = 0
    # Initialization of a dictionary for it to trace transactions for each date
    transactions = {}
    # Initialization of a dictionary to trace the card payments for each month
    card_payments = {month: 0 for month in range(1, 13)}
    # Looping through each transaction amount and date
    for i in range(len(A)):
        # Get the transaction amount
        amount = A[i]
        # Get the transaction date
        date = D[i]
        # Update transactions dictionary with the total amount for each date
        transactions[date] = transactions.get(date, 0) + amount
    # Iterate through each transaction date and amount
    for date, amount in transactions.items():
        # Split the date to extract the month
        year, month, _ = date.split('-')
        # Convert month to integer
        month = int(month)
        # Update balance based on transaction type (income or expenditure)
        if amount >= 0:
            # Add the amount to balance for incoming transfers
            balance += amount
        else:
            # Subtract the amount from balance for card payments
            balance += amount
            # Check if the amount is less than -5 (indicating a card payment)
            if amount < -5:
                # Increment the count of card payments for that month
                card_payments[month] += 1
    # Iterate through each month to deduct fees if necessary
    for month, count in card_payments.items():
        # If there are at least three card payments in the month
        if count >= 3:
            # Skip to the next month
            continue
        # Deduct a fee of 5 from the balance for months with less than three card payments
        balance -= 5
    # Return the final balance
    return balance

# Example 001
A1 = [100, 100, 100, -10]
D1 = ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]
print(solution(A1, D1))  # Output: 230