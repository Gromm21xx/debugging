def get_preferred_customers(customers):
    preferred_customers = []
    for customer in customers:
        if customer.total_spent > 1000 or customer.membership_length > 2:
            preferred_customers.append(customer)
    return preferred_customers

def get_customer_emails(customers):
    return [customer.email for customer in customers]