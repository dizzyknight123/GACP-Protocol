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

# GACP Agent SDK
# Implement quick agent integration in less than 10 lines of code

from typing import Dict, Any, Optional, Callable

class GACPSDK:
    """GACP Agent SDK"""
    
    def __init__(self, agent_id: str, capabilities: list):
        """
        Initialize SDK
        :param agent_id: Agent ID
        :param capabilities: Agent capabilities list
        """
        self.agent_id = agent_id
        self.capabilities = capabilities
        self.task_handler = None
    
    def register_task_handler(self, handler: Callable[[Dict[str, Any]], Dict[str, Any]]):
        """
        Register task handler
        :param handler: Task handling function
        """
        self.task_handler = handler
    
    def run_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run task
        :param task: Task information
        :return: Task execution result
        """
        if self.task_handler:
            try:
                return self.task_handler(task)
            except Exception as e:
                return {
                    "status": "failed",
                    "error": str(e)
                }
        else:
            return {
                "status": "failed",
                "error": "Task handler not registered"
            }
    
    def get_capabilities(self) -> list:
        """
        Get agent capabilities
        :return: Capabilities list
        """
        return self.capabilities
    
    def get_agent_info(self) -> Dict[str, Any]:
        """
        Get agent information
        :return: Agent information
        """
        return {
            "agent_id": self.agent_id,
            "capabilities": self.capabilities
        }

# Quick integration example
def create_gacp_agent(agent_id: str, capabilities: list, task_handler: Callable[[Dict[str, Any]], Dict[str, Any]]):
    """
    Quick create GACP agent
    :param agent_id: Agent ID
    :param capabilities: Agent capabilities list
    :param task_handler: Task handling function
    :return: GACP agent SDK instance
    """
    sdk = GACPSDK(agent_id, capabilities)
    sdk.register_task_handler(task_handler)
    return sdk

# Example usage
if __name__ == "__main__":
    # Example 1: Create a simple agent
    def simple_task_handler(task: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "status": "success",
            "result": f"Process task: {task.get('name', '')}"
        }
    
    # Agent integration in less than 10 lines of code
    agent = create_gacp_agent(
        agent_id="test_agent",
        capabilities=["test_task", "simple_processing"],
        task_handler=simple_task_handler
    )
    
    # Test running task
    test_task = {"name": "test_task", "description": "This is a test task"}
    result = agent.run_task(test_task)
    print("Test result:")
    print(result)
    
    # Example 2: Create a booking agent
    def booking_task_handler(task: Dict[str, Any]) -> Dict[str, Any]:
        if "book" in task.get("name", "").lower():
            return {
                "status": "success",
                "result": "Booking successful"
            }
        else:
            return {
                "status": "failed",
                "error": "Unsupported task type"
            }
    
    booking_agent = create_gacp_agent(
        agent_id="booking_agent",
        capabilities=["book_flight", "book_hotel"],
        task_handler=booking_task_handler
    )
    
    # Test booking task
    booking_task = {"name": "book_flight", "description": "Book a flight from Beijing to Shanghai"}
    booking_result = booking_agent.run_task(booking_task)
    print("\nBooking test result:")
    print(booking_result)