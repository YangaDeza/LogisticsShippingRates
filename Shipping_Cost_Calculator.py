#Shipping Cost Calc

##Input package weight & shipping rate
weight = float(input("Enter the package weight in Kilograms: "))
rate = float(input("Enter the shipping rate per Kilogram: "))

#Calc Shipping cost
shipping_cost = weight * rate

##Display the result
print(f"Shipping Cost: {shipping_cost} USD""
