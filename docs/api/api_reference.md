# API Reference Documentation

## 1. Core Module APIs

### 1.1 Requirement Structuring Layer (`requirement_parser.py`)

#### Class: `RequirementParser`

**Function**: Parses natural language requirements and converts them to structured JSON format.

**Methods**:

- **`parse(natural_language: str) -> RequirementStruct`**
  - **Parameters**: `natural_language` - Natural language requirement string
  - **Returns**: Structured requirement object `RequirementStruct`
  - **Example**:
    ```python
    parser = RequirementParser()
    requirement = "Book a flight from Beijing to Shanghai on March 10th, arrange airport pickup, and handle expense reimbursement."
    structured = parser.parse(requirement)
    ```

- **`to_json(requirement: RequirementStruct) -> str`**
  - **Parameters**: `requirement` - Structured requirement object
  - **Returns**: JSON string
  - **Example**:
    ```python
    json_str = parser.to_json(structured)
    print(json_str)
    ```

#### Class: `RequirementStruct`

**Attributes**:
- `goal` - Requirement goal
- `constraints` - List of constraints
- `acceptance_criteria` - List of acceptance criteria
- `subtasks` - List of subtasks
- `priority` - Priority
- `estimated_time` - Estimated completion time

### 1.2 Contract Generation Layer (`contract_generator.py`)

#### Class: `ContractGenerator`

**Function**: Generates collaboration contracts based on structured requirements.

**Methods**:

- **`generate_contract(structured_requirement: Dict[str, Any]) -> CollaborationContract`**
  - **Parameters**: `structured_requirement` - Structured requirement dictionary
  - **Returns**: Collaboration contract object `CollaborationContract`
  - **Example**:
    ```python
    generator = ContractGenerator()
    contract = generator.generate_contract(structured_requirement)
    ```

- **`to_json(contract: CollaborationContract) -> str`**
  - **Parameters**: `contract` - Collaboration contract object
  - **Returns**: JSON string
  - **Example**:
    ```python
    json_str = generator.to_json(contract)
    print(json_str)
    ```

#### Class: `CollaborationContract`

**Attributes**:
- `contract_id` - Contract ID
- `creation_time` - Creation time
- `goal` - Contract goal
- `participating_agents` - List of participating agents
- `terms` - List of contract terms
- `collaboration_flow` - Collaboration flow
- `dispute_resolution` - Dispute resolution mechanism
- `termination_conditions` - Termination conditions

### 1.3 Task Routing Layer (`task_router.py`)

#### Class: `TaskRouter`

**Function**: Routes tasks to appropriate agents and schedules task execution.

**Methods**:

- **`route_tasks(subtasks: List[Dict[str, Any]]) -> List[Task]`**
  - **Parameters**: `subtasks` - List of subtasks
  - **Returns**: List of routed tasks
  - **Example**:
    ```python
    router = TaskRouter()
    tasks = router.route_tasks(subtasks)
    ```

- **`schedule_tasks(tasks: List[Task]) -> List[Dict[str, Any]]`**
  - **Parameters**: `tasks` - List of tasks
  - **Returns**: Schedule plan
  - **Example**:
    ```python
    schedule = router.schedule_tasks(tasks)
    ```

- **`update_task_status(task_id: str, status: str) -> bool`**
  - **Parameters**:
    - `task_id` - Task ID
    - `status` - New status
  - **Returns**: Whether update was successful
  - **Example**:
    ```python
    success = router.update_task_status("task_1", "completed")
    ```

- **`get_task_status(task_id: str) -> Optional[str]`**
  - **Parameters**: `task_id` - Task ID
  - **Returns**: Task status
  - **Example**:
    ```python
    status = router.get_task_status("task_1")
    ```

#### Class: `Task`

**Attributes**:
- `task_id` - Task ID
- `name` - Task name
- `description` - Task description
- `agent_id` - Responsible agent ID
- `priority` - Priority
- `status` - Status
- `dependencies` - List of dependent task IDs
- `estimated_time` - Estimated completion time
- `actual_time` - Actual completion time

### 1.4 Trust Validation Layer (`trust_validator.py`)

#### Class: `TrustValidator`

**Function**: Validates task results and identifies malicious behavior.

**Methods**:

- **`validate_result(task_id: str, agent_id: str, result: Any) -> ValidationResult`**
  - **Parameters**:
    - `task_id` - Task ID
    - `agent_id` - Agent ID
    - `result` - Task result
  - **Returns**: Validation result object `ValidationResult`
  - **Example**:
    ```python
    validator = TrustValidator()
    validation = validator.validate_result("task_1", "booking_agent", result)
    ```

- **`identify_malicious_behavior(agent_id: str) -> bool`**
  - **Parameters**: `agent_id` - Agent ID
  - **Returns**: Whether it's malicious behavior
  - **Example**:
    ```python
    is_malicious = validator.identify_malicious_behavior("booking_agent")
    ```

- **`get_agent_reputation(agent_id: str) -> Optional[int]`**
  - **Parameters**: `agent_id` - Agent ID
  - **Returns**: Reputation value
  - **Example**:
    ```python
    reputation = validator.get_agent_reputation("booking_agent")
    ```

- **`resolve_dispute(task_id: str) -> Dict[str, Any]`**
  - **Parameters**: `task_id` - Task ID
  - **Returns**: Dispute resolution result
  - **Example**:
    ```python
    resolution = validator.resolve_dispute("task_1")
    ```

#### Class: `ValidationResult`

**Attributes**:
- `task_id` - Task ID
- `agent_id` - Agent ID
- `result` - Task result
- `is_valid` - Whether valid
- `validation_reason` - Validation reason
- `validator_nodes` - List of validator nodes
- `consensus_rate` - Consensus rate

## 2. Agent APIs

### 2.1 LangChain Agent (`agent_langchain.py`)

#### Class: `LangChainBookingAgent`

**Methods**:

- **`book_flight(departure: str, destination: str, date: str) -> Dict[str, Any]`**
  - **Parameters**:
    - `departure` - Departure location
    - `destination` - Destination location
    - `date` - Date
  - **Returns**: Booking result
  - **Example**:
    ```python
    agent = LangChainBookingAgent()
    result = agent.book_flight("Beijing", "Shanghai", "2026-03-10")
    ```

- **`book_hotel(city: str, check_in: str, check_out: str, guests: int = 1) -> Dict[str, Any]`**
  - **Parameters**:
    - `city` - City
    - `check_in` - Check-in date
    - `check_out` - Check-out date
    - `guests` - Number of guests
  - **Returns**: Booking result
  - **Example**:
    ```python
    result = agent.book_hotel("Shanghai", "2026-03-10", "2026-03-12")
    ```

- **`run_task(task: Dict[str, Any]) -> Dict[str, Any]`**
  - **Parameters**: `task` - Task information
  - **Returns**: Task execution result
  - **Example**:
    ```python
    result = agent.run_task({"name": "Book flight"})
    ```

### 2.2 CrewAI Multi-agent (`agent_crewai.py`)

#### Class: `CrewAIAgents`

**Methods**:

- **`arrange_airport_pickup(pickup_location: str, dropoff_location: str, date: str, time: str) -> Dict[str, Any]`**
  - **Parameters**:
    - `pickup_location` - Pickup location
    - `dropoff_location` - Dropoff location
    - `date` - Date
    - `time` - Time
  - **Returns**: Reservation result
  - **Example**:
    ```python
    agents = CrewAIAgents()
    result = agents.arrange_airport_pickup("Airport", "Hotel", "2026-03-10", "11:30")
    ```

- **`process_expense_reimbursement(expenses: List[Dict[str, Any]], trip_id: str) -> Dict[str, Any]`**
  - **Parameters**:
    - `expenses` - List of expenses
    - `trip_id` - Trip ID
  - **Returns**: Reimbursement result
  - **Example**:
    ```python
    expenses = [{"category": "Flight", "amount": "¥1200"}]
    result = agents.process_expense_reimbursement(expenses, "TRIP123")
    ```

- **`run_task(task: Dict[str, Any]) -> Dict[str, Any]`**
  - **Parameters**: `task` - Task information
  - **Returns**: Task execution result
  - **Example**:
    ```python
    result = agents.run_task({"name": "Airport pickup"})
    ```

### 2.3 AutoGPT Adapter (`agent_autogpt.py`)

#### Class: `AutoGPTAdapter`

**Methods**:

- **`adapt_to_gacp_contract(contract: Dict[str, Any]) -> Dict[str, Any]`**
  - **Parameters**: `contract` - GACP contract
  - **Returns**: Adapted AutoGPT task
  - **Example**:
    ```python
    adapter = AutoGPTAdapter()
    autogpt_task = adapter.adapt_to_gacp_contract(contract)
    ```

- **`run_autogpt_task(task: Dict[str, Any]) -> Dict[str, Any]`**
  - **Parameters**: `task` - AutoGPT task
  - **Returns**: Execution result
  - **Example**:
    ```python
    result = adapter.run_autogpt_task(autogpt_task)
    ```

- **`integrate_with_gacp(contract: Dict[str, Any]) -> Dict[str, Any]`**
  - **Parameters**: `contract` - GACP contract
  - **Returns**: Integration result
  - **Example**:
    ```python
    result = adapter.integrate_with_gacp(contract)
    ```

### 2.4 Agent SDK (`gacp_agent_sdk.py`)

#### Function: `create_gacp_agent(agent_id: str, capabilities: list, task_handler: Callable[[Dict[str, Any]], Dict[str, Any]]) -> GACPSDK`

**Function**: Quickly creates a GACP agent.

**Parameters**:
- `agent_id` - Agent ID
- `capabilities` - List of agent capabilities
- `task_handler` - Task handling function

**Returns**: GACP agent SDK instance

**Example**:
```python
from gacp_agent_sdk import create_gacp_agent

def handler(task):
    return {"status": "success", "result": "Processing completed"}

agent = create_gacp_agent(
    agent_id="my_agent",
    capabilities=["task1", "task2"],
    task_handler=handler
)
```

#### Class: `GACPSDK`

**Methods**:

- **`register_task_handler(handler: Callable[[Dict[str, Any]], Dict[str, Any]])`**
  - **Parameters**: `handler` - Task handling function
  - **Example**:
    ```python
    agent.register_task_handler(handler)
    ```

- **`run_task(task: Dict[str, Any]) -> Dict[str, Any]`**
  - **Parameters**: `task` - Task information
  - **Returns**: Task execution result
  - **Example**:
    ```python
    result = agent.run_task({"name": "Test task"})
    ```

- **`get_capabilities() -> list`**
  - **Returns**: List of capabilities
  - **Example**:
    ```python
    capabilities = agent.get_capabilities()
    ```

- **`get_agent_info() -> Dict[str, Any]`**
  - **Returns**: Agent information
  - **Example**:
    ```python
    info = agent.get_agent_info()
    ```

## 3. MVP Main Program API

### 3.1 Class: `GACPMVP`

**Function**: Implements end-to-end operation of GACP protocol.

**Methods**:

- **`run(natural_language: str) -> Dict[str, Any]`**
  - **Parameters**: `natural_language` - Natural language requirement
  - **Returns**: Execution result
  - **Example**:
    ```python
    mvp = GACPMVP()
    result = mvp.run("Book a flight from Beijing to Shanghai on March 10th, arrange airport pickup, and handle expense reimbursement.")
    ```

## 4. Configuration API

### 4.1 Environment Variables

| Environment Variable | Description | Default Value |
|---------------------|-------------|---------------|
| `GACP_MODE` | Run mode (mock or real) | `mock` |
| `GACP_LOG_LEVEL` | Log level | `info` |
| `GACP_VALIDATION_NODES` | Number of validation nodes | `10` |
| `OPENAI_API_KEY` | OpenAI API Key | None |
| `DASHSCOPE_API_KEY` | Tongyi Qianwen API Key | None |

### 4.2 Configuration File

Example `.env` configuration file:

```
# Run mode
GACP_MODE=mock

# Log level
GACP_LOG_LEVEL=info

# Number of validation nodes
GACP_VALIDATION_NODES=10

# API Keys (optional)
# OPENAI_API_KEY=your_api_key
# DASHSCOPE_API_KEY=your_api_key
```

## 5. Error Handling

### 5.1 Error Types

| Error Type | Description | Solution |
|------------|-------------|----------|
| `ModuleNotFoundError` | Missing dependency module | Run `pip install -r requirements.txt` |
| `APIError` | API call failed | Check if API Key is correct |
| `ValidationError` | Validation failed | Check if input parameters meet requirements |
| `TimeoutError` | Task timeout | Increase timeout or optimize task processing logic |

### 5.2 Error Handling Example

```python
try:
    result = agent.run_task(task)
except Exception as e:
    print(f"Error: {str(e)}")
    # Handle error
```

## 6. Performance Optimization

### 6.1 Caching Mechanism

Use caching to reduce repeated calculations:

```python
import functools

@functools.lru_cache(maxsize=128)
def cached_task_handler(task):
    # Process task
    return result
```

### 6.2 Asynchronous Processing

Use async to improve concurrent performance:

```python
import asyncio

async def async_task_handler(task):
    # Async task processing
    return result

# Run async task
result = asyncio.run(async_task_handler(task))
```

### 6.3 Batch Processing

Batch process tasks to reduce network overhead:

```python
def batch_task_handler(tasks):
    results = []
    for task in tasks:
        # Process task
        results.append(result)
    return results
```