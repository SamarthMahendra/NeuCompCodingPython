# Step 1: Helper functions for conversion
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def kelvin_to_celsius(k):
    return k - 273.15

# Step 2: Old APIs (providing temperature in different units)
class FahrenheitAPI:
    def get_temperature(self):
        return 100  # Returns temperature in Fahrenheit

class KelvinAPI:
    def get_temperature(self):
        return 300  # Returns temperature in Kelvin

# Step 3: New API that expects temperature in Celsius
class NewTemperatureAPI:
    def display_temperature(self, temp_celsius):
        print(f"Temperature: {temp_celsius:.2f}°C")

# Step 4: Generalized Adapter to handle multiple formats
class TemperatureAdapter:
    def __init__(self, old_api, scale="fahrenheit"):
        self.old_api = old_api  # Store the old API instance
        self.scale = scale.lower()  # Store the temperature scale

    def get_temperature(self):
        temp = self.old_api.get_temperature()  # Get raw temperature

        # Convert to Celsius based on scale
        if self.scale == "fahrenheit":
            return fahrenheit_to_celsius(temp)
        elif self.scale == "kelvin":
            return kelvin_to_celsius(temp)
        elif self.scale == "celsius":
            return temp  # No conversion needed
        else:
            raise ValueError("Unsupported scale! Use 'fahrenheit', 'kelvin', or 'celsius'.")

# Step 5: Test cases
fahrenheit_api = FahrenheitAPI()  # Old Fahrenheit API
kelvin_api = KelvinAPI()  # Old Kelvin API
new_api = NewTemperatureAPI()  # New API expecting Celsius

# Wrapping old APIs with the adapter
fahrenheit_adapter = TemperatureAdapter(fahrenheit_api, "fahrenheit")
kelvin_adapter = TemperatureAdapter(kelvin_api, "kelvin")

# Using the new API with adapted temperature data
new_api.display_temperature(fahrenheit_adapter.get_temperature())  # Should print converted °C
new_api.display_temperature(kelvin_adapter.get_temperature())  # Should print converted °C
