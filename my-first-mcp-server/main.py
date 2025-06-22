from mcp.server.fastmcp import FastMCP
from datetime import date

# Create Leave Management MCP Server
mcp = FastMCP("LeaveManagement")

# In-memory employee leave database
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

# Resource: Get current leave status + history
@mcp.resource("leave://status/{employee_id}")
def get_leave_status(employee_id: str) -> dict:
    """Return leave balance, total leaves taken, and history"""
    if employee_id in leave_data:
        return leave_data[employee_id]
    return {"error": "Employee not found"}

# Resource: Personalized greeting for an employee
@mcp.resource("leave://greeting/{employee_id}")
def leave_greeting(employee_id: str) -> str:
    """Return a personalized greeting with leave info"""
    if employee_id in leave_data:
        record = leave_data[employee_id]
        return (
            f"Hello {employee_id}, you have {record['balance']} days of leave left "
            f"and have taken {record['leaves']} day(s) off."
        )
    return "Employee not found."


# Tool: Apply for leave and update history
@mcp.tool()
def apply_leave(employee_id: str, days: int) -> str:
    """Apply leave for an employee"""
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
