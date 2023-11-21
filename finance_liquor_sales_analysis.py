#import modules
import pandas as pd
import matplotlib.pyplot as plt

#load the dataset
sales_data = pd.read_csv("finance_liquor_sales_from_2016_to_2019.csv")

#check for missing data
print("Missing Data:\n",sales_data.isna().sum())

#filling missing values using fillna()
sales_data["category_name"].fillna("Unknown Category", inplace=True)
sales_data["store_location"].fillna("Unknown Location", inplace=True)

#convert date column to datetime format
sales_data["date"] = pd.to_datetime(sales_data["date"])

#Find the most popular item per zip_code in the period 2016-2019
#Group by zipcode and calculate item sold
sales_per_zipcode = sales_data.groupby(["zip_code","item_description"])["bottles_sold"].sum().reset_index()

#sort the item sold by zip_code in descending order
sales_per_zipcode = sales_per_zipcode.sort_values(by="bottles_sold" ,ascending= False)

#display the most popular item
print("\nThe most popular item is the following:\n",sales_per_zipcode.head(1))

#Find the percentage of sales per store in the period 2016-2019
#Group by store name and calculate the item sold
sales_per_store = sales_data.groupby("store_name").agg({"bottles_sold":"sum"})

#calculate the percentage per store
sales_percent = round((sales_per_store["bottles_sold"]/sum(sales_data["bottles_sold"])*100),2)
print("\nSales per store in %\n")
print(sales_percent)

#Plot the items sold per zipcode
plt.scatter(sales_per_zipcode["zip_code"],sales_per_zipcode["bottles_sold"])
plt.xlabel("Zip code")
plt.ylabel("Bottles sold")
plt.title("Bottles sold per zip code")
plt.show()
