```markdown
# 🧾 Leave Management MCP App

This is a simple **Model Context Protocol (MCP)** app built using `FastMCP`, designed to manage employee leave data with in-memory storage. 
It exposes **structured resources and tools** that can be accessed by Claude or other MCP-compliant agents to query or modify state.

---

## 🚀 Setup Instructions

### 1. 📦 Install Requirements

Install the required tools:

```bash
pip install mcp
pip install uv

```

> ✅ mcp – Framework to define structured tools and resources for Claude
> 
> 
> ✅ `uv` – Fast Python runner used to initialize and run MCP apps
> 

---

### 2. ⚙️ Initialize Project

Use `uv` to bootstrap a new MCP project:

```bash
uv init my-first-mcp-server

```

This creates the following structure:

```
my-first-mcp-server/
├── main.py             # Your MCP server code
├── pyproject.toml      # Project metadata
└── README.md           # (You are here!)

```

---

## 💼 App Overview

The Leave Management MCP app provides the following endpoints and tools:

- 📊 **Leave Status Resource** – Returns balance, leaves taken, and leave history
- 💬 **Greeting Resource** – Provides personalized leave summaries
- 📝 **Apply Leave Tool** – Updates balance and logs history dynamically

All employee data is stored in memory and can be extended for persistence if needed.

---

## ▶️ Run the MCP Server

Inside your project directory, run:

```bash
uv run mcp install main.py

```

> This registers and runs your MCP app, making it available to Claude via your local environment or Claude Desktop.
> 

---

## 🤖 Using with Claude

Once installed and running, open **Claude Desktop**, and interact using:

- `leave://status/E001` → View leave status
- `leave://greeting/E002` → Get a greeting
- `apply_leave("E002", 2)` → Apply leave using the tool interface

Claude understands these structured calls and responds accordingly.

---

## 🛑 Stopping the Server

- In the terminal: Press `Ctrl + C`
- In Claude Desktop: Go to the **Apps tab** → Stop or Eject the app

---

## 🧼 Uninstall (Optional)

To remove the app from Claude or your environment:

```bash
uv run mcp uninstall .

```

---

## ✅ Summary

| Feature | Endpoint |
| --- | --- |
| View leave status | `leave://status/{employee_id}` |
| Get greeting | `leave://greeting/{employee_id}` |
| Apply leave | `apply_leave(employee_id, days)` |

---

### 👤 Author

**Nithish Reddy**
