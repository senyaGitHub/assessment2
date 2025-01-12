import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt




def visualise_data(records):
    headers = records[0]
    store_index = headers.index("StoreLocation")
    total_price_index = headers.index("TotalPrice")

    revenue_by_location = {}
    transaction_values = []

    #revenues
    for row in records[1:]:
        store_location = row[store_index]
        total_price = float(row[total_price_index])

        transaction_values.append(total_price)
        if store_location in revenue_by_location:
            revenue_by_location[store_location] += total_price
        else:
            revenue_by_location[store_location] = total_price

    root = tk.Tk()
    root.title("Data Visualisation")

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    pie_frame = ttk.Frame(notebook)
    notebook.add(pie_frame, text="Revenue by Store Location")

    fig1 = Figure(figsize=(5, 5))
    ax1 = fig1.add_subplot(111)
    ax1.pie(revenue_by_location.values(), labels=revenue_by_location.keys(), autopct='%1.1f%%')
    ax1.set_title("Revenue Contribution by Store Location")

    canvas1 = FigureCanvasTkAgg(fig1, master=pie_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(fill='both', expand=True)

    # Histogram Tab
    hist_frame = ttk.Frame(notebook)
    notebook.add(hist_frame, text="Transaction Values Histogram")

    fig2 = Figure(figsize=(5, 5))
    ax2 = fig2.add_subplot(111)
    ax2.hist(transaction_values, bins=10, color='blue', edgecolor='black')
    ax2.set_title("Histogram of Total Transaction Values")
    ax2.set_xlabel("Transaction Value")
    ax2.set_ylabel("Frequency")

    canvas2 = FigureCanvasTkAgg(fig2, master=hist_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(fill='both', expand=True)

    # Interactive Dashboard Tab
    # dashboard_frame = ttk.Frame(notebook)
    # notebook.add(dashboard_frame, text="Interactive Dashboard")

    # # Display summary statistics in dashboard
    # summary_label = tk.Label(dashboard_frame, text="Summary of Key Insights", font=("Arial", 14))
    # summary_label.pack(pady=10)

    # total_revenue = sum(revenue_by_location.values())
    # total_transactions = len(records) - 1
    # average_transaction_value = total_revenue / total_transactions if total_transactions > 0 else 0

    # summary_text = f"""
    # Total Revenue: \u00a3{total_revenue:.2f}
    # Total Transactions: {total_transactions}
    # Average Transaction Value: \u00a3{average_transaction_value:.2f}
    # """

    # summary_label = tk.Label(dashboard_frame, text=summary_text, font=("Arial", 12), justify="left")
    # summary_label.pack(pady=10)

    # Run the Tkinter loop
    root.mainloop()
