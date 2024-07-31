# In customer_utils.py
def get_preferred_customers(customers):
    preferred_customers = []
    for customer in customers:
        if customer.total_spent > 1000 or customer.membership_length >= 2:
            preferred_customers.append(customer)
    return preferred_customers

# In main.py
from customer_management.customer import Customer
from customer_management.customer_utils import get_preferred_customers

customers = [
    Customer("customer1@example.com", 1200, 1),
    Customer("customer2@example.com", 800, 3),
    Customer("customer3@example.com", 900, 1),
    Customer("customer4@example.com", 1100, 2)
]

preferred_customers = get_preferred_customers(customers)
for customer in preferred_customers:
    print(customer.get_customer_info())