def get_top_customers(customers, n):
    sorted_customers = sorted(customers, key=lambda c: c.total_spent, reverse=True)
    return sorted_customers[:n]