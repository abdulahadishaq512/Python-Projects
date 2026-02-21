class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        # Fulfills User Story: Create specific object in ledger
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # Fulfills User Story: Check funds before withdrawal
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        # Calculates current balance from ledger
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        # Fulfills User Story: Withdraw from source, deposit to destination
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        # Returns False if amount > balance
        return amount <= self.get_balance()

    def __str__(self):
        # Title line centered with *
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            # Format description (23 chars) and amount (7 chars, 2 decimal places)
            desc = f"{item['description'][:23]:23}"
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    # 1. Calculate spending per category (withdrawals only)
    spendings = []
    for cat in categories:
        spent = sum(item["amount"] for item in cat.ledger if item["amount"] < 0)
        spendings.append(abs(spent))

    total_spent = sum(spendings)
    # Calculate percentages rounded down to the nearest 10
    percentages = [(s / total_spent * 100) // 10 * 10 for s in spendings]

    # 2. Build the chart top-down
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"

    # 3. Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 4. Vertical names
    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]
    
    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += name[i] + "  "
        if i < max_len - 1:
            chart += "\n"

    return chart