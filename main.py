from mcp.server.fastmcp import FastMCP

# Create a MCP server
mcp = FastMCP("My MCP server")

@mcp.tool()
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kg and height in meters

    Args:
        weight_kg (float): Weight in kilograms
        hegiht_m (float): Height in meter

    Returns:
        (float): Body Mass Index (BMI) value
    """
    return weight_kg / (height_m ** 2)

# Calculate BMI for the given measurements
weight_kg = 75.75  # converted from 167 lbs
height_m = 1.81
bmi = calculate_bmi(weight_kg, height_m)
print(f"\nBMI Calculation Results:")
print(f"Weight: {weight_kg:.2f} kg ({167} lbs)")
print(f"Height: {height_m:.2f} m")
print(f"Your BMI: {bmi:.1f}")

# BMI Categories
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")

if __name__ == "__main__":
    mcp.run()



