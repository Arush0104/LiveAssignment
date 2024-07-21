def calculate_total_expenses(file_path):
    try:
        with open(file_path, 'r') as file:
            total = 0.0  # Initialize total to 0.0
            for line in file:
                try:
                    expense = float(line.strip())  # Convert line to float
                    total += expense  # Add expense to total
                except ValueError:
                    print(f"Ignoring non-numeric line: {line}")
            return total  # Return the total expenses
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading file: {str(e)}")

# File path to expenses.txt
file_path = 'Q18/item.txt'

# Calculate total expenses
total_expenses = calculate_total_expenses(file_path)

if total_expenses is not None:
    print(f"Total expenses: ${total_expenses:.2f}")
