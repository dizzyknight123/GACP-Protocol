# Agent Integration Guide

## 1. Overview

GACP protocol supports the integration of multiple agent frameworks, including LangChain, CrewAI, and AutoGPT. This document will detail how to integrate different types of agents.

## 2. Integration Methods

### 2.1 Using GACP SDK

GACP provides a unified SDK interface to simplify agent integration:

```python
from gacp_agent_sdk import create_gacp_agent

# Define task handling function
def task_handler(task):
    # Task processing logic
    return {
        "status": "success",
        "result": "Task processing result"
    }

# Create agent
agent = create_gacp_agent(
    agent_id="my_agent",
    capabilities=["capability1", "capability2"],
    task_handler=task_handler
)

# Run task
result = agent.run_task({"name": "Test task"})
```

### 2.2 Direct Integration with Core Modules

For more complex scenarios, you can directly integrate with core modules:

1. **Requirement Structuring Layer**: Use `RequirementParser` to parse natural language requirements
2. **Contract Generation Layer**: Use `ContractGenerator` to generate collaboration contracts
3. **Task Routing Layer**: Use `TaskRouter` for task routing
4. **Trust Validation Layer**: Use `TrustValidator` to validate task results

## 3. Agent Types

### 3.1 LangChain Agent

#### Integration Steps

1. **Install dependencies**:
   ```bash
   pip install langchain openai
   ```

2. **Create agent**:
   ```python
   from agent_langchain import LangChainBookingAgent

   # Create agent (using mock mode)
   agent = LangChainBookingAgent()

   # Test flight booking
   result = agent.book_flight("Beijing", "Shanghai", "2026-03-10")
   print(result)
   ```

### 3.2 CrewAI Multi-agent

#### Integration Steps

1. **Install dependencies**:
   ```bash
   pip install crewai langchain openai
   ```

2. **Create agent**:
   ```python
   from agent_crewai import CrewAIAgents

   # Create agent (using mock mode)
   agents = CrewAIAgents()

   # Test airport pickup arrangement
   result = agents.arrange_airport_pickup(
       "Shanghai Pudong International Airport", 
       "Waldorf Astoria Shanghai on the Bund", 
       "2026-03-10", 
       "11:30"
   )
   print(result)
   ```

### 3.3 AutoGPT Agent

#### Integration Steps

1. **Install dependencies**:
   ```bash
   pip install autogpt
   ```

2. **Create adapter**:
   ```python
   from agent_autogpt import AutoGPTAdapter

   # Create adapter (using mock mode)
   adapter = AutoGPTAdapter()

   # Adapt GACP contract
   contract = {
       "goal": "Test task",
       "terms": [
           {"description": "Test task 1", "responsible_agent": "test_agent"}
       ],
       "participating_agents": ["test_agent"]
   }

   # Integrate with GACP
   result = adapter.integrate_with_gacp(contract)
   print(result)
   ```

## 4. Agent Capability Declaration

Agents need to declare their capabilities so that GACP protocol can route tasks correctly:

```python
# Capability declaration example
capabilities = [
    "book flight",
    "book hotel",
    "airport pickup",
    "expense reimbursement",
    "meeting arrangement",
    "research analysis",
    "procurement process"
]
```

## 5. Agent Best Practices

### 5.1 Error Handling

Agents should have good error handling capabilities:

```python
def task_handler(task):
    try:
        # Process task
        return {"status": "success", "result": "Task result"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}
```

### 5.2 Result Validation

Agents should ensure that returned results can be verified:

```python
def task_handler(task):
    # Process task
    result = {"status": "success", "data": "Task data"}
    
    # Add validation information
    result["validation_info"] = {
        "timestamp": "2026-03-02T10:00:00",
        "agent_id": "my_agent",
        "signature": "..."  # Optional: digital signature
    }
    
    return result
```

### 5.3 Performance Optimization

- **Caching**: Cache common results to reduce repeated calculations
- **Asynchrony**: Use asynchronous processing to improve concurrent performance
- **Batch processing**: Support batch task processing to reduce network overhead

## 6. Agent Testing

### 6.1 Unit Tests

Write unit tests for agents to ensure functionality:

```python
import unittest
from my_agent import MyAgent

class TestMyAgent(unittest.TestCase):
    def test_task_execution(self):
        agent = MyAgent()
        result = agent.run_task({"name": "Test task"})
        self.assertEqual(result["status"], "success")

if __name__ == "__main__":
    unittest.main()
```

### 6.2 Integration Tests

Test agent integration with GACP protocol:

```python
from gacp_mvp import GACPMVP

mvp = GACPMVP()
requirement = "Test agent functionality"
result = mvp.run(requirement)
print(f"Integration test result: {result['overall_status']}")
```

## 7. Common Questions

### 7.1 Agent Registration

**Question**: How to register an agent with GACP protocol?

**Solution**: Agents do not need explicit registration. GACP protocol automatically matches agents based on task type.

### 7.2 Task Priority

**Question**: How to set task priority?

**Solution**: Specify priority in the task description or set it through task parameters:

```python
task = {
    "name": "Urgent task",
    "description": "Needs urgent processing",
    "priority": "high"
}
```

### 7.3 Agent Communication

**Question**: How do agents communicate with each other?

**Solution**: Through the GACP protocol's contract mechanism, agents can communicate through shared contracts and task statuses.

## 8. Example Agents

### 8.1 Booking Agent

```python
from gacp_agent_sdk import create_gacp_agent

def booking_handler(task):
    if "book flight" in task.get("name", ""):
        return {
            "status": "success",
            "result": "Flight booking successful"
        }
    elif "book hotel" in task.get("name", ""):
        return {
            "status": "success",
            "result": "Hotel booking successful"
        }
    else:
        return {
            "status": "failed",
            "error": "Unsupported task type"
        }

booking_agent = create_gacp_agent(
    agent_id="booking_agent",
    capabilities=["book flight", "book hotel"],
    task_handler=booking_handler
)
```

### 8.2 Reimbursement Agent

```python
from gacp_agent_sdk import create_gacp_agent

def reimbursement_handler(task):
    if "expense reimbursement" in task.get("name", ""):
        return {
            "status": "success",
            "result": "Expense reimbursement processed"
        }
    else:
        return {
            "status": "failed",
            "error": "Unsupported task type"
        }

reimbursement_agent = create_gacp_agent(
    agent_id="reimbursement_agent",
    capabilities=["expense reimbursement"],
    task_handler=reimbursement_handler
)
```