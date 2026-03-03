# Copyright shiQi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# GACP = General AI Collaboration Protocol

# AutoGPT Adapter Code
# Implement compatibility adaptation between AutoGPT and GACP contracts

from typing import Dict, Any, Optional

class AutoGPTAdapter:
    """AutoGPT Adapter"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize AutoGPT adapter
        :param api_key: API Key (optional, not needed for mock mode)
        """
        self.api_key = api_key
        self.is_mock = not api_key
    
    def adapt_to_gacp_contract(self, contract: Dict[str, Any]) -> Dict[str, Any]:
        """
        Adapt GACP contract to AutoGPT
        :param contract: GACP contract
        :return: Adapted AutoGPT task
        """
        # Extract contract information
        goal = contract.get("goal", "")
        terms = contract.get("terms", [])
        participating_agents = contract.get("participating_agents", [])
        
        # Build AutoGPT task
        autogpt_task = {
            "goal": goal,
            "tasks": [],
            "agents": participating_agents,
            "constraints": [],
            "resources": []
        }
        
        # Convert contract terms to AutoGPT tasks
        for term in terms:
            task = {
                "name": term.get("description", ""),
                "agent": term.get("responsible_agent", ""),
                "deadline": term.get("deadline", ""),
                "priority": "high"
            }
            autogpt_task["tasks"].append(task)
        
        return autogpt_task
    
    def run_autogpt_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run AutoGPT task
        :param task: AutoGPT task
        :return: Execution result
        """
        if self.is_mock:
            # Mock execution result
            return {
                "status": "success",
                "goal": task.get("goal", ""),
                "tasks_completed": len(task.get("tasks", [])),
                "result": "AutoGPT task executed successfully",
                "completion_time": "2 minutes"
            }
        
        # Actual AutoGPT integration code (placeholder)
        # Actual implementation needs to be adjusted based on AutoGPT's API
        try:
            # Should call AutoGPT's API or run AutoGPT locally here
            # Since AutoGPT's implementation varies, this is just an example
            return {
                "status": "success",
                "goal": task.get("goal", ""),
                "result": "AutoGPT task executed successfully (real mode)"
            }
        except Exception as e:
            return {
                "status": "failed",
                "error": str(e)
            }
    
    def integrate_with_gacp(self, contract: Dict[str, Any]) -> Dict[str, Any]:
        """
        Integrate with GACP protocol
        :param contract: GACP contract
        :return: Integration result
        """
        # Adapt contract
        autogpt_task = self.adapt_to_gacp_contract(contract)
        
        # Run task
        result = self.run_autogpt_task(autogpt_task)
        
        # Convert result to GACP compatible format
        gacp_result = {
            "status": result.get("status", "failed"),
            "contract_id": contract.get("contract_id", ""),
            "result": result.get("result", ""),
            "completion_time": result.get("completion_time", ""),
            "tasks_completed": result.get("tasks_completed", 0)
        }
        
        return gacp_result

# Test code
if __name__ == "__main__":
    # Create adapter (using mock mode)
    adapter = AutoGPTAdapter()
    
    # Mock GACP contract
    mock_contract = {
        "contract_id": "contract_20260302123456",
        "goal": "Book a flight from Beijing to Shanghai on March 10th, arrange airport pickup, and handle expense reimbursement.",
        "participating_agents": ["booking_agent", "transportation_agent", "reimbursement_agent"],
        "terms": [
            {
                "term_id": "term_1",
                "description": "Book a suitable flight according to requirements",
                "responsible_agent": "booking_agent",
                "deadline": "Within 24 hours after task start"
            },
            {
                "term_id": "term_2",
                "description": "Arrange a suitable hotel according to requirements",
                "responsible_agent": "booking_agent",
                "deadline": "Within 24 hours after task start"
            },
            {
                "term_id": "term_3",
                "description": "Arrange airport pickup service",
                "responsible_agent": "transportation_agent",
                "deadline": "Within 24 hours after task start"
            },
            {
                "term_id": "term_4",
                "description": "Handle travel expense reimbursement",
                "responsible_agent": "reimbursement_agent",
                "deadline": "Within 24 hours after task start"
            }
        ]
    }
    
    # Test adapting contract
    print("Testing GACP contract adaptation:")
    autogpt_task = adapter.adapt_to_gacp_contract(mock_contract)
    print(autogpt_task)
    
    # Test running task
    print("\nTesting AutoGPT task execution:")
    task_result = adapter.run_autogpt_task(autogpt_task)
    print(task_result)
    
    # Test GACP integration
    print("\nTesting GACP integration:")
    integration_result = adapter.integrate_with_gacp(mock_contract)
    print(integration_result)