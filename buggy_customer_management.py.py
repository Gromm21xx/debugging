import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Customer:
    def __init__(self, name, email, total_spent):
        self.name = name
        self.email = email
        self.total_spent = total_spent

    def get_customer_info(self):
        return f"Name: {self.name}, Email: {self.email}, Total Spent: ${self.total_spent}"

def calculate_discount(customer):
    if customer.total_spent > 1000
        return 0.1
    elif customer.total_spent > 500:
        return 0.05
    else
        return 0

def apply_discount(customer):
    discount = calculate_discount(customer)
    discounted_total = customer.total_spent * (1 - discount)
    logging.info(f"Applied {discount * 100}% discount for {customer.name}")
    return discounted_total

def send_email(customer, message):
    # Simulating email sending
    print(f"Sending email to {customer.email}: {message}")

def process_customers(customers):
    for customer in customers
        discounted_total = apply_discount(customer)
        message = f"Your discounted total is ${discounted_total}"
        send_email(customer, message)

if __name__ == "__main__":
    customers = [
        Customer("Alice", "alice@example.com", 1200),
        Customer("Bob", "bob@example.com", 800),
        Customer("Charlie", "charlie@example.com", 300)
    ]
    process_customers(customers)