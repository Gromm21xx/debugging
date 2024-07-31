import concurrent.futures
import requests
import logging
import time
import random
from customer import Customer

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConcurrentCustomer(Customer):
    def __init__(self, email, total_spent, membership_length):
        super().__init__(email, total_spent, membership_length)

    def _get_reward_points_with_delay(self):
        try:
            delay = random.uniform(0.1, 0.5)  # Random delay between 0.1 and 0.5 seconds
            time.sleep(delay)
            logging.info(f"Fetching reward rate for customer: {self.email} with delay: {delay:.2f}s")
            response = requests.get("https://api.example.com/reward-rate")
            rate = response.json()["rate"]
            points = int(self.total_spent * rate)
            logging.info(f"Calculated {points} reward points for {self.email}")
            return points
        except Exception as e:
            logging.error(f"Failed to calculate reward points for {self.email}: {str(e)}")
            return 0

    def get_bulk_reward_points(self, num_calls):
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(self._get_reward_points_with_delay) for _ in range(num_calls)]
            results = []
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())
        return results

if __name__ == "__main__":
    customer = ConcurrentCustomer("test@example.com", 1000, 1)
    points = customer.get_bulk_reward_points(10)
    print(f"Reward points from bulk calls: {points}")