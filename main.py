import datetime

class SimpleAI:
    def __init__(self):
        self.greetings = ["P", "PPP", "PPPP!", "PPPPP!", "PP!"]

    def greet(self):
        import random
        return random.choice(self.greetings)

    def add_numbers(self, a, b):
        return a + b

    def get_current_datetime(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    ai = SimpleAI()

    print(ai.greet())

    a, b = 5, 7
    print(f"The sum of {a} and {b} is: {ai.add_numbers(a, b)}")

    print(f"The current date and time is: {ai.get_current_datetime()}")