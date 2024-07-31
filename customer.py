class Customer:
    def __init__(self, email, total_spent, membership_length):
        self.email = email
        self.total_spent = total_spent
        self.membership_length = membership_length

    def get_customer_info(self):
        membership_level = self.get_membership_level()
        return f"Email: {self.email}, Total Spent: £{self.total_spent}, Membership Level: {membership_level}"

    def get_membership_level(self):
        if self.membership_length >= 5:
            return "Gold"
        elif self.membership_length >= 2:
            return "Silver"
        else:
            return "Bronze"