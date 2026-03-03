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

# MVP Main Program
# Implements end-to-end one-click operation for travel scenario

from requirement_parser import RequirementParser
from contract_generator import ContractGenerator
from task_router import TaskRouter
from trust_validator import TrustValidator
from agent_langchain import LangChainBookingAgent
from agent_crewai import CrewAIAgents
from agent_autogpt import AutoGPTAdapter
from typing import Dict, Any

class GACPMVP:
    """GACP Protocol MVP Main Program"""
    
    def __init__(self):
        """Initialize MVP main program"""
        self.parser = RequirementParser()
        self.generator = ContractGenerator()
        self.router = TaskRouter()
        self.validator = TrustValidator()
        self.booking_agent = LangChainBookingAgent()
        self.crewai_agents = CrewAIAgents()
        self.autogpt_adapter = AutoGPTAdapter()
    
    def run(self, natural_language: str) -> Dict[str, Any]:
        """
        Run end-to-end process
        :param natural_language: Natural language requirement
        :return: Execution result
        """
        # Step 1: Requirement structuring parsing
        print("Step 1: Requirement structuring parsing")
        structured_requirement = self.parser.parse(natural_language)
        structured_data = structured_requirement.dict()
        print(f"Structured requirement: {structured_data}")
        
        # Step 2: Automatic collaboration contract generation
        print("\nStep 2: Automatic collaboration contract generation")
        contract = self.generator.generate_contract(structured_data)
        contract_data = contract.dict()
        print(f"Generated contract: {contract_data}")
        
        # Step 3: Task routing and multi-agent calling
        print("\nStep 3: Task routing and multi-agent calling")
        subtasks = structured_data.get("subtasks", [])
        tasks = self.router.route_tasks(subtasks)
        schedule = self.router.schedule_tasks(tasks)
        
        # Execute tasks
        task_results = []
        for task_info in schedule:
            task_id = task_info["task_id"]
            task_name = task_info["task_name"]
            agent_id = task_info["agent_id"]
            
            print(f"Executing task: {task_name} (Agent: {agent_id})")
            
            # Select corresponding executor based on agent type
            if agent_id == "booking_agent":
                result = self.booking_agent.run_task({"name": task_name})
            elif agent_id in ["transportation_agent", "reimbursement_agent"]:
                result = self.crewai_agents.run_task({"name": task_name})
            else:
                # Use AutoGPT adapter for other tasks
                result = self.autogpt_adapter.integrate_with_gacp(contract_data)
            
            task_results.append({
                "task_id": task_id,
                "task_name": task_name,
                "agent_id": agent_id,
                "result": result
            })
            
            # Update task status
            self.router.update_task_status(task_id, "completed" if result.get("status") == "success" else "failed")
        
        # Step 4: Result consensus validation and output
        print("\nStep 4: Result consensus validation and output")
        validation_results = []
        for task_result in task_results:
            task_id = task_result["task_id"]
            agent_id = task_result["agent_id"]
            result = task_result["result"]
            
            # Validate task result
            validation = self.validator.validate_result(task_id, agent_id, result)
            validation_results.append(validation.dict())
            
            print(f"Task validation result: {task_result['task_name']} - {'Valid' if validation.is_valid else 'Invalid'}")
        
        # Generate final result
        final_result = {
            "input": natural_language,
            "structured_requirement": structured_data,
            "contract": contract_data,
            "task_results": task_results,
            "validation_results": validation_results,
            "overall_status": "success" if all(v["is_valid"] for v in validation_results) else "failed"
        }
        
        return final_result

# Test code
if __name__ == "__main__":
    # Create MVP instance
    mvp = GACPMVP()
    
    # Test travel scenario
    test_requirement = "Book a flight from Beijing to Shanghai on March 10th, arrange airport pickup, and handle expense reimbursement."
    print(f"Input requirement: {test_requirement}")
    
    # Run end-to-end process
    result = mvp.run(test_requirement)
    
    # Output result
    print("\nFinal result:")
    print(f"Overall status: {result['overall_status']}")
    print(f"Number of tasks executed: {len(result['task_results'])}")
    print(f"Number of validations passed: {sum(1 for v in result['validation_results'] if v['is_valid'])}")
    
    # Detailed output of each task result
    print("\nDetailed task results:")
    for task_result in result['task_results']:
        print(f"Task: {task_result['task_name']}")
        print(f"Agent: {task_result['agent_id']}")
        print(f"Result: {task_result['result']}")
        print()