# Cursor MCP Server Example

This project demonstrates a simple MCP (Model Control Protocol) server implementation using the Cursor FastMCP framework. The server includes a BMI calculation tool as an example functionality.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

2. Install the required dependencies:
```bash
pip install cursor-mcp
```

## Project Structure

- `main.py`: Contains the MCP server implementation with a sample BMI calculator tool
- Other project files...

## Configuration

The MCP server is configured in `main.py`. The current implementation:

1. Creates a FastMCP server instance with a custom name
2. Implements a BMI calculation tool
3. Exposes the tool through the MCP protocol

## Usage

1. Start the MCP server:
```bash
python main.py
```

2. The server will start and expose the BMI calculation tool through the MCP protocol.

3. You can interact with the server using Cursor's MCP client interface.

## Available Tools

### BMI Calculator
Calculates Body Mass Index (BMI) given weight and height.

- Input:
  - `weight_kg` (float): Weight in kilograms
  - `height_m` (float): Height in meters
- Output:
  - Returns the calculated BMI value as a float

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

[Add your chosen license here]
