# Copyright 2024 GACP Protocol Team
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

# Automated red team attack test script
# Covers attack scenarios including malicious agent default, fake validation results, rule bypass, node malicious behavior, process deadlock, etc.

import sys
import os

# Add core code directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '02-Core-Code'))

from trust_validator import TrustValidator
from contract_generator import ContractGenerator
from task_router import TaskRouter

class RedTeamTest:
    """Red team attack test"""
    
    def __init__(self):
        self.validator = TrustValidator()
        self.generator = ContractGenerator()
        self.router = TaskRouter()
    
    def test_malicious_agent_default(self):
        """Test malicious agent default"""
        print("Test scenario 1: Malicious agent default")
        
        # Simulate malicious agent submitting fake results
        for i in range(5):
            result = self.validator.validate_result(
                f"task_malicious_{i}", 
                "booking_agent", 
                {"status": "failed", "error": "Intentional failure"}
            )
            print(f"Validation result {i+1}: {'Valid' if result.is_valid else 'Invalid'}")
        
        # Check malicious behavior identification
        is_malicious = self.validator.identify_malicious_behavior("booking_agent")
        print(f"Malicious behavior identification result: {'Malicious' if is_malicious else 'Normal'}")
        print(f"Agent reputation: {self.validator.get_agent_reputation('booking_agent')}")
        print()
    
    def test_fake_validation_results(self):
        """Test fake validation results"""
        print("Test scenario 2: Fake validation results")
        
        # Simulate multiple nodes submitting different validation results
        results = []
        for i in range(10):
            result = self.validator.validate_result(
                f"task_fake_{i}", 
                "transportation_agent", 
                {"status": "success", "fake": True}
            )
            results.append(result.is_valid)
            print(f"Node {i+1} validation result: {'Valid' if result.is_valid else 'Invalid'}")
        
        # Analyze consensus results
        valid_count = sum(results)
        print(f"Valid validation count: {valid_count}/10")
        print()
    
    def test_rule_bypass(self):
        """Test rule bypass"""
        print("Test scenario 3: Rule bypass")
        
        # Simulate structured requirement
        structured_requirement = {
            "goal": "Test rule bypass",
            "subtasks": [
                {"name": "Test task", "description": "Intentionally vague description to bypass rules"}
            ]
        }
        
        # Generate contract
        contract = self.generator.generate_contract(structured_requirement)
        print(f"Generated contract ID: {contract.contract_id}")
        print(f"Number of contract terms: {len(contract.terms)}")
        print()
    
    def test_node_malicious(self):
        """Test node malicious behavior"""
        print("Test scenario 4: Node malicious behavior")
        
        # Simulate 30% node malicious behavior scenario
        print("Simulating 30% node malicious behavior scenario...")
        
        # Run multiple validations to observe consensus results
        consensus_results = []
        for i in range(10):
            result = self.validator.validate_result(
                f"task_node_{i}", 
                "reimbursement_agent", 
                {"status": "success", "value": i}
            )
            consensus_results.append(result.consensus_rate)
            print(f"Validation {i+1} consensus rate: {result.consensus_rate * 100:.1f}%")
        
        # Analyze consensus rate
        avg_consensus = sum(consensus_results) / len(consensus_results)
        print(f"Average consensus rate: {avg_consensus * 100:.1f}%")
        print()
    
    def test_process_deadlock(self):
        """Test process deadlock"""
        print("Test scenario 5: Process deadlock")
        
        # Simulate tasks with circular dependencies
        subtasks = [
            {"name": "Task A", "description": "Depends on Task B"},
            {"name": "Task B", "description": "Depends on Task A"}
        ]
        
        try:
            tasks = self.router.route_tasks(subtasks)
            schedule = self.router.schedule_tasks(tasks)
            print(f"Schedule length: {len(schedule)}")
            print("Process not deadlocked, scheduling successful")
        except Exception as e:
            print(f"Process deadlocked: {str(e)}")
        print()
    
    def run_all_tests(self):
        """Run all red team tests"""
        print("=" * 100)
        print("GACP Protocol Red Team Attack Test")
        print("=" * 100)
        
        self.test_malicious_agent_default()
        self.test_fake_validation_results()
        self.test_rule_bypass()
        self.test_node_malicious()
        self.test_process_deadlock()
        
        print("=" * 100)
        print("Red team attack test completed")
        print("=" * 100)

if __name__ == "__main__":
    # Create red team test instance
    red_team = RedTeamTest()
    
    # Run all tests
    red_team.run_all_tests()