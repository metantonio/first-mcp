from mcp.server.fastmcp import FastMCP

# Create a MCP server
mcp = FastMCP("My MCP server")

mcp.tool()
def calculate_bmi(weight_kg: float, height_m: float) -> float:

    # Structure must be: Description - Arguments - Returns
    """Calculate BMI given weight in kg and height in meters

    Args:
        weight_kg (float): Weight in kilograms
        hegiht_m (float): Height in meter

    Returns:
        (float): Body Mass Index (BMI) value
    """

    return weight_kg / (height_m ** 2)



