import pandas
import matplotlib.pyplot as plt
import re

def get_CSV():
    filename = "housing_data.csv"
    return pandas.read_csv(filename)

def calculate_price():
    return

def get_house_size():
    print("\nHello. Welcome to the price prediction based on house size module.")
    print("\nPlease enter a house size (in sq ft) or press q to quit...")

    while True:
        choice = input("\nHouse Size: ")
        
        if choice == "q" or choice == "Q":
            break
        elif re.fullmatch(r'\d+', choice):
            calculate_price()
            
            print("\nCalculate another price based on house size?")
            choice_2 = input("(Y)es/(N)o: ")

            if choice_2 == "Y" or choice_2 == "y" or choice_2 == "YES" or choice_2 == "yes":
                None
            else:
                break
        else:
            print("Enter a positive integer.")



def main():
    # df = get_CSV()

    get_house_size()

main()
