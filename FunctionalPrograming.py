#Weather forecast using Python Visual Studio, adhering to functional programming principles:
# Functional aspect: Only final data structures

def generate_forecast(city, temperature, conditions):
    # Using a dictionary as a final data structure to represent the forecast
    return {'city': city, 'temperature': temperature, 'conditions': conditions}

# Functional aspect: (Mostly) side-effect-free functions

def print_forecast(forecast):
    # No side effects, just printing
    print(f"Weather forecast for {forecast['city']}:")
    print(f"Temperature: {forecast['temperature']}°C")
    print(f"Conditions: {forecast['conditions']}")

# Functional aspect: Use of higher-order functions

def adjust_temperature(forecast, adjustment_function):
    # Higher-order function taking a function as a parameter
    adjusted_temperature = adjustment_function(forecast['temperature'])
    return {**forecast, 'temperature': adjusted_temperature}

def double_temperature(temperature):
    return temperature * 2

# Functional aspect: Functions as parameters and return values

def combine_forecasts(forecast1, forecast2, combine_function):
    # Higher-order function combining two forecasts using a function as a parameter
    combined_forecast = combine_function(forecast1, forecast2)
    return combined_forecast

def average_temperatures(forecast1, forecast2):
    # Function as a parameter to calculate the average temperature
    average_temperature = (forecast1['temperature'] + forecast2['temperature']) / 2
    return {'city': 'Combined', 'temperature': average_temperature, 'conditions': 'Mixed'}

# Functional aspect: Use closures / anonymous functions

def create_adjustment_function(factor):
    # Closure to create a specific adjustment function
    return lambda x: x * factor

# Example usage:

initial_forecast = generate_forecast('New York', 25, 'Sunny')
adjusted_forecast = adjust_temperature(initial_forecast, create_adjustment_function(1.5))
combined_forecast = combine_forecasts(initial_forecast, adjusted_forecast, average_temperatures)

print_forecast(initial_forecast)
print("\nAfter Adjustment:")
print_forecast(adjusted_forecast)
print("\nCombined Forecast:")
print_forecast(combined_forecast)
