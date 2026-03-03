# GACP Project Startup Guide

## 1. Environment Requirements
- **Operating System**: Windows 10+, macOS 10.15+, Linux
- **Python**: 3.10 or higher
- **Memory**: 4GB or more
- **Storage**: 100MB or more

## 2. Installation Steps

### Step 1: Clone the Repository
```bash
# Clone the repository using Git
git clone https://github.com/gacp-protocol/GACP-Protocol.git

# Enter the project directory
cd GACP-Protocol
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables (Optional)
1. Copy `.env.example` file to `.env`
2. Fill in the corresponding API Key (can be skipped when using Mock mode)

## 3. Run MVP

### Method 1: Use Startup Script
```bash
# Windows
run_mvp.bat

# macOS/Linux
chmod +x run_mvp.sh
./run_mvp.sh
```

### Method 2: Run Manually
```bash
python 02-Core-Code/gacp_mvp.py
```

## 4. Expected Output
```
📋 Parsing requirement: Arrange a business trip
🤝 Generating collaboration contract: contract_20240101120000
🔄 Routing tasks to agents:
  - Task 1: Book flight -> LangChainBookingAgent
  - Task 2: Book hotel -> LangChainBookingAgent
  - Task 3: Arrange transportation -> CrewAITransportationAgent
✅ Validating results:
  - Flight booking: Valid
  - Hotel booking: Valid
  - Transportation arrangement: Valid
📊 Collaboration completed: All tasks executed successfully
```

## 5. Test Suite

### Run All Tests
```bash
python -m pytest 03-Test/
```

### Run Specific Tests
```bash
# Unit tests
python -m pytest 03-Test/test_unit.py

# End-to-end tests
python -m pytest 03-Test/test_e2e.py

# Security tests
python -m pytest 03-Test/test_red_team.py

# Performance tests
python -m pytest 03-Test/test_stress.py
```

## 6. Project Structure
```
GACP-Protocol/
├── 01-WhitePaper/       # Whitepaper and related documents
├── 02-Core-Code/        # Protocol core code
├── 03-Test/             # Test scripts and reports
├── 05-OpenSource/       # Open source release materials
├── docs/                # Developer documentation
├── requirements.txt      # Project dependency list
├── README.md             # Project overview
├── run_mvp.bat           # Windows startup script
└── run_mvp.sh            # macOS/Linux startup script
```

## 7. Frequently Asked Questions

### Q: What if I get an API Key missing error?
A: The system will automatically switch to Mock mode, using simulated data for testing, no API Key required.

### Q: What if tests fail?
A: Check if Python version is 3.10+, ensure all dependencies are properly installed.

### Q: How to integrate custom agents?
A: Refer to `docs/agents/agent_integration.md` document.

### Q: How to contribute code?
A: Refer to `CONTRIBUTING.md` document.

## 8. Resource Links
- **Project Documentation**: `docs/` directory
- **Whitepaper**: `01-WhitePaper/` directory
- **API Documentation**: `docs/api/api_reference.md`
- **GitHub Repository**: https://github.com/gacp-protocol/GACP-Protocol

---

**GACP Protocol** - Making AI agent collaboration simpler, more reliable, and more efficient!