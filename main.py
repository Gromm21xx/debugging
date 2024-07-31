import pandas as pd
from customer_management.customer import Customer
from customer_management.customer_utils import get_preferred_customers, get_customer_emails

# Load the dataset
data = pd.read_csv("Ecommerce Customers.csv")

# Create instances of the Customer class based on the dataset
customers = []
for _, row in data.iterrows():
    email = row['Email']
    total_spent = row['Yearly Amount Spent']
    membership_length = row['Length of Membership']
    customer = Customer(email, total_spent, membership_length)
    customers.append(customer)

# Get preferred customers
preferred_customers = get_preferred_customers(customers)
print("Preferred Customers:")
for customer in preferred_customers:
    print(customer.get_customer_info())

# Get customer emails
customer_emails = get_customer_emails(customers)
print("\nCustomer Emails:")
print(customer_emails)