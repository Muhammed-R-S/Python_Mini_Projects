class Category:
    def __init__(self, item):
        self.item = item
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total_balance = sum(item["amount"] for item in self.ledger)
        return total_balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.item}")
            category.deposit(amount, f"Transfer from {self.item}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.item:*^30}\n"
        items = ""
        for item in self.ledger:
            description = f"{item['description'][:23]:23}"
            amount = f"{item['amount']:>7.2f}"
            items += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    expenditure = []
    total_spent = 0
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        expenditure.append(spent)
        total_spent += spent

    spend_percentages = [int((spent / total_spent) * 100) for spent in expenditure]

    chart = title
    for i in range(100, -10, -10):
        chart += f"{i:>3}| "
        for percent in spend_percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length = max(len(category.item) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.item):
                chart += f"{category.item[i]}  "
            else:
                chart += "   "
        chart += "\n"

    return chart.strip("\n")


# Example usage
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

entertainment = Category('Entertainment')
entertainment.deposit(1000, 'initial deposit')
entertainment.withdraw(200, 'movies')
entertainment.withdraw(100, 'concert')

categories = [food, clothing, entertainment]
print(create_spend_chart(categories))
