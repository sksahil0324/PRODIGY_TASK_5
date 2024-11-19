# PRODIGY_TASK_5

# E-Commerce Product Scraper

This program allows you to scrape product information such as product names, prices, and ratings from an e-commerce website and save the data to a CSV file. It comes with a simple Graphical User Interface (GUI) built using **Tkinter**. The user inputs the URL of the e-commerce website, and the program fetches the product details from the site.

## Features:
- Scrapes product name, price, and rating from the provided e-commerce website.
- Saves the scraped data in a CSV file (`products.csv`).
- Simple and user-friendly GUI for easy URL input.
- Allows the user to scrape data from any URL that provides product details.

## Requirements:
To run this program, you will need the following Python libraries:
- `requests`: For sending HTTP requests to the website.
- `beautifulsoup4`: For parsing HTML and extracting product data.
- `tkinter`: For creating the graphical user interface.
- `csv`: For saving the scraped data to a CSV file.

### You can install the required libraries using pip:
```bash
pip install requests beautifulsoup4
```

## Usage:
1. **Run the program** by executing the script in Python. A GUI window will open.
2. **Enter the e-commerce website URL** in the provided input box.
3. **Click the "Start Scraping" button** to begin scraping the website for product information.
4. After the data is scraped, it will be saved to a file named `products.csv` in the same directory as the script.
5. The program will display a success message with the filename where the data is saved.

### Example of a CSV output:
The CSV file will contain the following columns:
- **Product Name**
- **Product Price**
- **Product Rating**

Sample CSV output:
```
Product Name, Product Price, Product Rating
"Product 1", "$199.99", "4.5"
"Product 2", "$249.99", "4.0"
"Product 3", "$349.99", "4.8"
```

## Troubleshooting:
- **403 Forbidden Error**: If you encounter a 403 error (forbidden access), it is likely due to anti-scraping measures. You can try adding a `User-Agent` header to your requests (as done in the code) to mimic a real browser request. Alternatively, using proxies or rotating IP addresses might help bypass this restriction.
- **CAPTCHA**: Some websites may require CAPTCHA solving. In such cases, you can try using **Selenium** for browser automation or use services like **2Captcha** to handle the CAPTCHA.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
