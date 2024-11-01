
# Inventory Management System

An inventory management system to track and manage stock of items. This project was created to showcase set-based inventory management in Python.

## Features

- Stores each unique item type in a set.
- Users can add or remove items from the inventory.
- Provides operations to check item stock status, find out-of-stock items, and list all available items.
- Displays a summary of the current inventory.

## Project Structure

- `main.py`: The main file where the inventory management system is run. Users interact with this file.
- `inventory_operations.py`: Contains functions for adding, removing, checking stock, listing items, and exiting the system.
- `inventory_analysis.py`: Includes functions for finding out-of-stock items and summarizing inventory.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/inventory-management-system.git
   ```
2. Run the main file to start the system:
   ```bash
   python main.py
   ```

## Usage

1. Choose an option to add or remove items, check stock status, or view inventory summary.
2. To exit the system, select the exit option.

## Future Improvements

- Add item quantities for more detailed inventory tracking.
- Implement file handling to save and load inventory data.

## License

This project is open-source and available under the [MIT License](LICENSE).
