import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import messagebox

# Function to extract and scrape product data
def scrape_data():
    url = url_entry.get()  # Get URL input from user
    if not url:
        messagebox.showwarning("Input Error", "Please enter a valid URL.")
        return

    # Adding headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    try:
        # Send the request with the headers
        r = requests.get(url, headers=headers)
        r.raise_for_status()  # Check if the request was successful

        soup = BeautifulSoup(r.text, "html.parser")  # Use default HTML parser

        # Find product names, prices, and ratings
        names = soup.find_all("a", class_="title")
        prices = soup.find_all("h4", class_="pull-right price")
        ratings = soup.find_all("p", class_="pull-right")

        # Initialize list to store product data
        product_data = []

        # Extract and store product details
        for name, price, rating in zip(names, prices, ratings):
            product_name = name.text.strip()
            product_price = price.text.strip()
            product_rating = rating.text.strip()
            product_data.append([product_name, product_price, product_rating])

        # Specify the filename for the CSV file
        csv_filename = "products.csv"

        # Save data to CSV
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Product Name", "Product Price", "Product Rating"])

            for data in product_data:
                csv_writer.writerow(data)

        messagebox.showinfo("Success", f"Data successfully scraped and saved to {csv_filename}")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# GUI setup
def create_gui():
    # Setup the main window
    root = tk.Tk()
    root.title("E-Commerce Product Scraper")

    # Create and place widgets
    tk.Label(root, text="Enter E-Commerce URL:").grid(row=0, column=0, padx=10, pady=10)
    global url_entry
    url_entry = tk.Entry(root, width=50)
    url_entry.grid(row=0, column=1, padx=10, pady=10)

    scrape_button = tk.Button(root, text="Start Scraping", font=("Arial", 14), command=scrape_data)
    scrape_button.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

# Run the GUI
create_gui()
