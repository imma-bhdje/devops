from locust import User, task, between, events
import random
import secrets
import subprocess

class CalculatorUser(User):
    host = "http://localhost"  # Placeholder URL

    wait_time = between(1, 2)

    @task
    def perform_calculation(self):
        # Generate random calculation parameters or use predefined values
        choice = secrets.choice([1, 2, 3, 4])
        num1 = random.uniform(0.1, 10.0)
        num2 = random.uniform(0.1, 10.0)

        # Execute the calculator script as a subprocess
        command = ["python3", "application/calculator.py", str(choice), str(num1), str(num2)]
        output = subprocess.check_output(command, text=True)

        # Calculate response time
        response_time = 0  # Set response time to 0 for CLI calculations

        # Log the request success using the custom event
        events.request.fire(
            request_type="cli_calculation",
            name="calculator",
            response_time=response_time,
            response_length=len(output),
            exception=None,  # No exception in CLI calculations
        )

        # Print the output
        print(output)

