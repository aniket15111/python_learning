import logging

# Setup basic logging config
logging.basicConfig(
    level=logging.DEBUG,  # Show everything from DEBUG and above
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',  # Log to file
    filemode='w'          # Overwrite on each run
)

def load_numbers(filename):
    logging.info("Starting to load numbers from file: %s", filename)
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        logging.critical("File not found: %s", filename)
        return []

    numbers = []
    for line in lines:
        try:
            num = float(line.strip())
            logging.debug("Parsed number: %f", num)
            numbers.append(num)
        except ValueError:
            logging.warning("Invalid number skipped: %s", line.strip())
    return numbers

def calculate_average(numbers):
    if not numbers:
        logging.error("No valid numbers to calculate average.")
        return None
    avg = sum(numbers) / len(numbers)
    logging.info("Average calculated successfully.")
    return avg

# Main execution
filename = "numbers.txt"
data = load_numbers(filename)
average = calculate_average(data)

if average is not None:
    print(f"Average: {average:.2f}")
else:
    print("No average calculated.")
