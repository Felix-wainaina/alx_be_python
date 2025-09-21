# weather_advice.py
# Program to give clothing recommendations based on the weather

# Ask the user for the weather
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide clothing recommendation
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
