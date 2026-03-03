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

# CrewAI multi-agent integration code
# Implements 2 agents: transportation booking and expense reimbursement, integrated with GACP protocol

from typing import Dict, Any, Optional, List

# Try to import CrewAI dependencies
try:
    from crewai import Agent, Task, Crew, Process
    from langchain.llms import OpenAI
    CREWAI_AVAILABLE = True
except ImportError:
    CREWAI_AVAILABLE = False

class CrewAIAgents:
    """CrewAI multi-agent"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize CrewAI agents
        :param api_key: OpenAI API Key (optional, not needed for mock mode)
        """
        self.api_key = api_key
        self.is_mock = not api_key
        self.transportation_agent = self._create_transportation_agent()
        self.reimbursement_agent = self._create_reimbursement_agent()
    
    def _create_transportation_agent(self):
        """
        Create transportation booking agent
        :return: Transportation booking agent
        """
        if self.is_mock or not CREWAI_AVAILABLE:
            return None
        
        try:
            return Agent(
                role="Transportation Coordinator",
                goal="Arrange airport pickup services to ensure clients arrive at and depart from the airport on time",
                backstory="You are a professional transportation coordinator skilled at arranging various transportation services to ensure clients' smooth travel",
                llm=OpenAI(api_key=self.api_key, temperature=0)
            )
        except Exception:
            return None
    
    def _create_reimbursement_agent(self):
        """
        Create expense reimbursement agent
        :return: Expense reimbursement agent
        """
        if self.is_mock or not CREWAI_AVAILABLE:
            return None
        
        try:
            return Agent(
                role="Expense Reimbursement Specialist",
                goal="Process travel expense reimbursements to ensure all expenses are reimbursed timely and accurately",
                backstory="You are a professional financial reimbursement expert familiar with various reimbursement processes and regulations",
                llm=OpenAI(api_key=self.api_key, temperature=0)
            )
        except Exception:
            return None
    
    def arrange_airport_pickup(self, pickup_location: str, dropoff_location: str, date: str, time: str) -> Dict[str, Any]:
        """
        Arrange airport pickup
        :param pickup_location: Pickup location
        :param dropoff_location: Dropoff location
        :param date: Date
        :param time: Time
        :return: Booking result
        """
        if self.is_mock or not CREWAI_AVAILABLE or not self.transportation_agent:
            # Mock booking result
            return {
                "status": "success",
                "service_type": "airport pickup",
                "pickup_location": pickup_location,
                "dropoff_location": dropoff_location,
                "date": date,
                "time": time,
                "driver_name": "Mr. Zhang",
                "vehicle_type": "sedan",
                "license_plate": "沪A12345",
                "booking_reference": "TRANS67890"
            }
        
        # Use real CrewAI agent
        try:
            task = Task(
                description=f"Arrange airport pickup service from {pickup_location} to {dropoff_location} on {date} at {time}",
                agent=self.transportation_agent
            )
            
            crew = Crew(
                agents=[self.transportation_agent],
                tasks=[task],
                process=Process.sequential
            )
            
            result = crew.kickoff()
            return {
                "status": "success",
                "result": str(result)
            }
        except Exception as e:
            return {
                "status": "failed",
                "error": str(e)
            }
    
    def process_expense_reimbursement(self, expenses: List[Dict[str, Any]], trip_id: str) -> Dict[str, Any]:
        """
        Process expense reimbursement
        :param expenses: Expense list
        :param trip_id: Trip ID
        :return: Reimbursement result
        """
        if self.is_mock or not CREWAI_AVAILABLE or not self.reimbursement_agent:
            # Mock reimbursement result
            total_amount = sum(float(expense.get("amount", "0").replace("¥", "")) for expense in expenses)
            return {
                "status": "success",
                "trip_id": trip_id,
                "expenses": expenses,
                "total_amount": f"¥{total_amount}",
                "reimbursement_status": "approved",
                "processing_time": "within 24 hours",
                "reference_number": "REIMB12345"
            }
        
        # Use real CrewAI agent
        try:
            task = Task(
                description=f"Process expense reimbursement for trip ID {trip_id} with expense details: {expenses}",
                agent=self.reimbursement_agent
            )
            
            crew = Crew(
                agents=[self.reimbursement_agent],
                tasks=[task],
                process=Process.sequential
            )
            
            result = crew.kickoff()
            return {
                "status": "success",
                "result": str(result)
            }
        except Exception as e:
            return {
                "status": "failed",
                "error": str(e)
            }
    
    def run_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run task
        :param task: Task information
        :return: Task execution result
        """
        task_name = task.get("name", "")
        task_description = task.get("description", "")
        
        if "Airport pickup" in task_name or "airport pickup" in task_name:
            # Extract parameters
            pickup_location = "Shanghai Pudong International Airport"
            dropoff_location = "The Waldorf Astoria Shanghai on the Bund"
            date = "2026-03-10"
            time = "11:30"
            
            # Execute pickup arrangement
            return self.arrange_airport_pickup(pickup_location, dropoff_location, date, time)
        elif "Expense reimbursement" in task_name or "expense reimbursement" in task_name:
            # Extract parameters
            expenses = [
                {"category": "flight", "amount": "¥1200", "date": "2026-03-10"},
                {"category": "hotel", "amount": "¥3000", "date": "2026-03-10"},
                {"category": "transportation", "amount": "¥200", "date": "2026-03-10"}
            ]
            trip_id = "TRIP12345"
            
            # Execute reimbursement
            return self.process_expense_reimbursement(expenses, trip_id)
        else:
            return {
                "status": "failed",
                "error": f"Unsupported task type: {task_name}"
            }

# Test code
if __name__ == "__main__":
    # Create agents (using mock mode)
    agents = CrewAIAgents()
    
    # Test arranging airport pickup
    print("Testing airport pickup arrangement:")
    pickup_result = agents.arrange_airport_pickup(
        "Shanghai Pudong International Airport", 
        "The Waldorf Astoria Shanghai on the Bund", 
        "2026-03-10", 
        "11:30"
    )
    print(pickup_result)
    
    # Test processing expense reimbursement
    print("\nTesting expense reimbursement processing:")
    expenses = [
        {"category": "flight", "amount": "¥1200", "date": "2026-03-10"},
        {"category": "hotel", "amount": "¥3000", "date": "2026-03-10"},
        {"category": "transportation", "amount": "¥200", "date": "2026-03-10"}
    ]
    reimbursement_result = agents.process_expense_reimbursement(expenses, "TRIP12345")
    print(reimbursement_result)
    
    # Test running task
    print("\nTesting task running:")
    task = {"name": "Airport pickup", "description": "Arrange airport pickup service"}
    task_result = agents.run_task(task)
    print(task_result)