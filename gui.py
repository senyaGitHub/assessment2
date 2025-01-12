import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


def display_pie_chart(transactions_by_location):
    locations = process.transactions_by_location().keys()
    revenues = process.transactions_by_location().values()

    # Plot pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(revenues, labels=locations, autopct="%1.1f%%", startangle=140)
    plt.title("Revenue Contribution by Store Location")
    plt.show()


def display_histogram(transaction_values):
    plt.figure(figsize=(10, 6))
    plt.hist(transaction_values, bins=10, edgecolor="black")
    plt.title("Histogram of Total Transaction Values")
    plt.xlabel("Transaction Value")
    plt.ylabel("Frequency")
    plt.show()
