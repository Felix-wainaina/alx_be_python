#!/usr/bin/env python3
"""
bank_account.py

Defines the BankAccount class to demonstrate Object-Oriented Programming concepts.
"""

class BankAccount:
    """A simple Bank Account class for deposit, withdraw, and balance display."""

    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional starting balance (stored as float)."""
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit money into the account."""
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            print("Deposit amount must be a number.")
            return

        if amt > 0:
            self.account_balance += amt
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds are available."""
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            print("Withdrawal amount must be a number.")
            return False

        if amt <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amt <= self.account_balance:
            self.account_balance -= amt
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance formatted with two decimal places."""
        print(f"Current Balance: ${self.account_balance:.2f}")
