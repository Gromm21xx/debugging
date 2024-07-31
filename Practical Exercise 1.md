
# Debugging

## Practical Exercise 1: Debugging with Error Logging

## Exercise instructions:

1. Create a new file named customer.py in your working directory.
2. Copy the following base code into customer.py:

        import requests

        class Customer:
            def __init__(self, email, total_spent, membership_length):
                self.email = email
                self.total_spent = total_spent
                self.membership_length = membership_length

            def get_reward_points(self):
                try:
                    response = requests.get("https://api.example.com/reward-rate")
                    rate = response.json()["rate"]
                 return int(self.total_spent * rate)
            except:
                return 0

3. Import the logging module at the top of the file.
4. Add the following logging configuration immediately after the imports:

        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

5. In the get_reward_points method of the Customer class:
    a. Add a log message before the API call:

        logging.info(f"Fetching reward rate for customer: {self.email}")

    b. Add a log message after successfully calculating points:

        logging.info(f"Calculated {points} reward points for {self.email}")

    c. In the except block, add an error log:

        logging.error(f"Failed to calculate reward points for {self.email}: {str(e)}")

6. At the end of the file, add a test section:

        if __name__ == "__main__":
            customer = Customer("test@example.com", 1000, 1)
            points = customer.get_reward_points()
            print(f"Reward points: {points}")

7. Run the script and observe the log output.

