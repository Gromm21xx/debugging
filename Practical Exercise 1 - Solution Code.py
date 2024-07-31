import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Customer:
    def __init__(self, email, total_spent, membership_length):
        self.email = email
        self.total_spent = total_spent
        self.membership_length = membership_length

    def get_reward_points(self):
        try:
            logging.info(f"Fetching reward rate for customer: {self.email}")
            response = requests.get("https://api.example.com/reward-rate")
            rate = response.json()["rate"]
            points = int(self.total_spent * rate)
            logging.info(f"Calculated {points} reward points for {self.email}")
            return points
        except Exception as e:
            logging.error(f"Failed to calculate reward points for {self.email}: {str(e)}")
            return 0

if __name__ == "__main__":
    customer = Customer("test@example.com", 1000, 1)
    points = customer.get_reward_points()
    print(f"Reward points: {points}")