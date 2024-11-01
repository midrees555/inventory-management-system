# inventory_analysis.py

from inventory_operations import inventory

def find_out_of_stock(catalog):
    """Return items that are in the catalog but not in inventory (out of stock)"""
    return catalog - inventory


def inventory_summary():
    """Provide a summary of the inventory."""
    return {
        "total_items" : len(inventory),
        "in_stock_items" : list(inventory)
    }