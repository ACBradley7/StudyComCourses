import pandas
import matplotlib.pyplot as plt
import re
import math
from sklearn.linear_model import LinearRegression as LinReg

def welcome():
    print("\nHello. Welcome to the price prediction based on house size module.")
    print("Enter a filename of housing data to see various statistical information.")

def get_data():
    df = get_CSV()

    if df is None:
        return

    print(f"\n{df.describe()}")
    return df

def get_CSV():
    try:
        filename = input("\nFile: ")
        return pandas.read_csv(filename)
    except FileNotFoundError:
        print("\nError: The specified file was not found.")
        print("\nQuitting...")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("\nQuitting...")

def plot_data(df, showRegLine=False, *model):
    plt.scatter(df["size"], df["price"])
    plt.xlabel("House Size (sq ft)")
    plt.ylabel("Price (USD)")
    plt.title("House Size vs. Price")
    plt.grid(True)

    if showRegLine:
        model = model[0]
        reg_line = model.coef_[0] * df["size"] + model.intercept_
        plt.plot(df["size"], reg_line, color='red', label='Regression Line')
    
    plt.show()

def train_model(df):
    model = LinReg()
    model.fit(df["size"].values.reshape(-1, 1), df["price"])
    return model

def show_model(df, model):
    coeff = model.coef_
    intercept = model.intercept_
    r_squared = model.score(df["size"].values.reshape(-1, 1), df["price"])
    print("\n----- Scikit-learn Model Summary -----")
    print(f"Coefficient(s): {coeff}")
    print(f"Intercept: {intercept}")
    print(f"R-Squared Score: {r_squared}")

def get_house_size(model):
    print("\nPlease enter a house size (in sq ft) to see a predicted price or press q to quit...")

    while True:
        choice = input("\nHouse Size: ")
        
        if choice == "q" or choice == "Q" or choice == "":
            break
        elif re.fullmatch(r'\d+', choice):
            price = calculate_price(choice, model)
            show_price(choice, price)
            break
        else:
            print("Enter a positive integer.")

    if choice == "q" or choice == "Q" or choice == "":
        return

    print("\nCalculate another price based on house size?")
    choice_2 = input("(Y)es/(N)o: ")

    if choice_2 == "Y" or choice_2 == "y" or choice_2 == "YES" or choice_2 == "yes":
        get_house_size(model)
    else:
        return

def calculate_price(choice, model):
    price = model.coef_ * int(choice) + model.intercept_
    return price

def show_price(choice, price):
    print(f"\nThe predicted price for a house size of {choice} sq ft is ${math.ceil(price[0])}.")

def main():
    welcome()

    df = get_data()
    if df is None:
        return
    
    plot_data(df)
    model = train_model(df)
    show_model(df, model)
    plot_data(df, True, model)
    get_house_size(model)

main()
