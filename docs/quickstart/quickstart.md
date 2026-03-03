# Quick Start Guide

## 1. Environment Preparation

### 1.1 System Requirements
- Python 3.10+
- Operating System: Windows, MacOS, Linux

### 1.2 Install Dependencies

```bash
# Clone the repository
git clone https://github.com/yourusername/GACP-Protocol.git
cd GACP-Protocol

# Install dependencies
pip install -r requirements.txt
```

### 1.3 Configure Environment Variables

Copy the `.env.example` file to `.env` and fill in the API Key if needed (optional, not required when using mock mode):

```bash
# Windows
copy .env.example .env

# Mac/Linux
cp .env.example .env
```

## 2. Run MVP

### 2.1 One-click Run

Use the provided script to quickly run the MVP:

```bash
# Windows
run_mvp.bat

# Mac/Linux
chmod +x run_mvp.sh
./run_mvp.sh
```

### 2.2 Manual Run

```bash
# Enter core code directory
cd 02-Core-Code

# Run MVP main program
python gacp_mvp.py
```

## 3. Test Travel Scenario

### 3.1 Input Example

When the program starts, it will prompt for natural language requirements, for example:

```
Book a flight from Beijing to Shanghai on March 10th, arrange airport pickup, and handle expense reimbursement.
```

### 3.2 Output Result

The program will automatically execute the following steps:
1. Requirement structuring parsing
2. Automatic collaboration contract generation
3. Task routing and multi-agent calling
4. Result consensus validation and output

The final output will include the complete execution results, including flight booking, hotel booking, pickup service, and reimbursement information.

## 4. Custom Agents

### 4.1 Use SDK to Quickly Create Agents

```python
from gacp_agent_sdk import create_gacp_agent

# Define task handling function
def my_task_handler(task):
    return {
        "status": "success",
        "result": f"Processing task: {task.get('name', '')}"
    }

# Create agent
agent = create_gacp_agent(
    agent_id="my_custom_agent",
    capabilities=["custom task", "specific function"],
    task_handler=my_task_handler
)

# Test agent
test_task = {"name": "Test task", "description": "This is a test task"}
result = agent.run_task(test_task)
print(result)
```

## 5. Extended Scenarios

### 5.1 Supported Scenarios

- Travel planning (default scenario)
- Meeting arrangement
- Research analysis
- Procurement process

### 5.2 Custom Scenarios

1. Add new requirement type identification in `requirement_parser.py`
2. Add corresponding contract generation logic in `contract_generator.py`
3. Add new task processing logic in agent integration code

## 6. Troubleshooting

### 6.1 Common Errors

- **Missing dependencies**: Run `pip install -r requirements.txt` to install all dependencies
- **API Key error**: Use mock mode (do not fill in API Key)
- **Port occupation**: Check if other programs are occupying ports

### 6.2 Log Viewing

The program will output detailed log information during operation, which can be used to locate problems.

## 7. Next Steps

- Check [Agent Integration Guide](../agents/agent_integration.md) to learn how to integrate custom agents
- Check [API Documentation](../api/api_reference.md) to understand how to use core APIs
- Check [FAQ](../faq/faq.md) to learn more usage details