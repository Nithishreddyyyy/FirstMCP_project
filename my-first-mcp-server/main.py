from mcp.server.fastmcp import FastMCP
from datetime import date
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Leave Management MCP Server
mcp = FastMCP("LeaveManagement")

# Your existing code...
leave_data = {
    "E001": {
        "balance": 10,
        "leaves": 2,
        "history": [{"date": "2025-06-01", "days": 2}]
    },
    "E002": {
        "balance": 5,
        "leaves": 0,
        "history": []
    }
}

# Your existing functions...
@mcp.resource("leave://status/{employee_id}")
def get_leave_status(employee_id: str) -> dict:
    logger.info(f"Getting leave status for {employee_id}")
    if employee_id in leave_data:
        return leave_data[employee_id]
    return {"error": "Employee not found"}

@mcp.resource("leave://greeting/{employee_id}")
def leave_greeting(employee_id: str) -> str:
    logger.info(f"Getting greeting for {employee_id}")
    if employee_id in leave_data:
        record = leave_data[employee_id]
        return (
            f"Hello {employee_id}, you have {record['balance']} days of leave left "
            f"and have taken {record['leaves']} day(s) off."
        )
    return "Employee not found."

@mcp.tool()
def apply_leave(employee_id: str, days: int) -> str:
    logger.info(f"Applying {days} days leave for {employee_id}")
    if employee_id not in leave_data:
        return "Employee not found"
    
    record = leave_data[employee_id]
    if record["balance"] >= days:
        record["balance"] -= days
        record["leaves"] += days
        record["history"].append({
            "date": str(date.today()),
            "days": days
        })
        return f"Leave approved for {days} day(s)."
    else:
        return "Insufficient leave balance."

if __name__ == "__main__":
    logger.info("Starting Leave Management MCP Server...")
    mcp.run()