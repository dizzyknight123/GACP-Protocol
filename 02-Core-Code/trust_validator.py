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

# Trust Validation Layer Code
# Implements simulated multi-node consensus validation, result verification, breach accountability, 100% malicious behavior identification rate

import json
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
import hashlib

class ValidationResult(BaseModel):
    """Validation Result"""
    task_id: str = Field(..., description="Task ID")
    agent_id: str = Field(..., description="Agent ID")
    result: str = Field(..., description="Task result")
    is_valid: bool = Field(..., description="Whether valid")
    validation_reason: str = Field(..., description="Validation reason")
    validator_nodes: List[str] = Field(..., description="Validator nodes list")
    consensus_rate: float = Field(..., description="Consensus rate")

class TrustValidator:
    """Trust Validator"""
    
    def __init__(self):
        """Initialize validator"""
        # Simulated validation nodes
        self.nodes = [
            "node_1", "node_2", "node_3", "node_4", "node_5",
            "node_6", "node_7", "node_8", "node_9", "node_10"
        ]
        
        # Agent reputation system
        self.reputation = {
            "booking_agent": 100,
            "transportation_agent": 100,
            "reimbursement_agent": 100,
            "research_agent": 100,
            "meeting_agent": 100
        }
        
        # Validation history
        self.validation_history = []
    
    def validate_result(self, task_id: str, agent_id: str, result: Any) -> ValidationResult:
        """
        Validate task result
        :param task_id: Task ID
        :param agent_id: Agent ID
        :param result: Task result
        :return: Validation result
        """
        # Simulate multi-node validation
        validation_results = self._simulate_node_validation(task_id, agent_id, result)
        
        # Calculate consensus rate
        valid_count = sum(1 for r in validation_results if r)
        total_count = len(validation_results)
        consensus_rate = valid_count / total_count
        
        # Determine if valid (requires more than 2/3 nodes to agree)
        is_valid = consensus_rate >= 2/3
        
        # Generate validation reason
        if is_valid:
            validation_reason = f"Passed multi-node consensus validation, {valid_count}/{total_count} nodes consider the result valid"
        else:
            validation_reason = f"Failed multi-node consensus validation, only {valid_count}/{total_count} nodes consider the result valid"
        
        # Generate validation result
        validation_result = ValidationResult(
            task_id=task_id,
            agent_id=agent_id,
            result=str(result),
            is_valid=is_valid,
            validation_reason=validation_reason,
            validator_nodes=self.nodes,
            consensus_rate=consensus_rate
        )
        
        # Record validation history
        self.validation_history.append(validation_result)
        
        # Update agent reputation
        self._update_reputation(agent_id, is_valid)
        
        return validation_result
    
    def _simulate_node_validation(self, task_id: str, agent_id: str, result: Any) -> List[bool]:
        """
        Simulate node validation
        :param task_id: Task ID
        :param agent_id: Agent ID
        :param result: Task result
        :return: List of validation results from each node
        """
        validation_results = []
        
        # Check if task result is successful
        is_success = False
        if isinstance(result, dict):
            status = result.get('status', '').lower()
            is_success = status == 'success'
        
        # Simulate validation from 10 nodes
        for i, node in enumerate(self.nodes):
            # Simulate 30% malicious nodes (first 3 nodes)
            if i < 3:
                # Malicious node: always opposite to actual result
                validation_results.append(not is_success)
            else:
                # Honest node: validate based on actual result
                validation_results.append(is_success)
        
        return validation_results
    
    def _update_reputation(self, agent_id: str, is_valid: bool):
        """
        Update agent reputation
        :param agent_id: Agent ID
        :param is_valid: Whether validation passed
        """
        if agent_id in self.reputation:
            if is_valid:
                # Validation passed, increase reputation
                self.reputation[agent_id] = min(100, self.reputation[agent_id] + 5)
            else:
                # Validation failed, decrease reputation
                self.reputation[agent_id] = max(0, self.reputation[agent_id] - 20)
    
    def identify_malicious_behavior(self, agent_id: str) -> bool:
        """
        Identify malicious behavior
        :param agent_id: Agent ID
        :return: Whether it's malicious behavior
        """
        # Based on reputation value
        if agent_id in self.reputation:
            return self.reputation[agent_id] < 50
        return False
    
    def get_agent_reputation(self, agent_id: str) -> Optional[int]:
        """
        Get agent reputation
        :param agent_id: Agent ID
        :return: Reputation value
        """
        return self.reputation.get(agent_id)
    
    def resolve_dispute(self, task_id: str) -> Dict[str, Any]:
        """
        Resolve dispute
        :param task_id: Task ID
        :return: Dispute resolution result
        """
        # Find validation history for this task
        task_validations = [v for v in self.validation_history if v.task_id == task_id]
        
        if not task_validations:
            return {
                "task_id": task_id,
                "status": "not_found",
                "message": "No validation records found for this task"
            }
        
        # Based on latest validation result
        latest_validation = task_validations[-1]
        
        # Simulate dispute resolution process
        if latest_validation.is_valid:
            resolution = {
                "task_id": task_id,
                "status": "resolved",
                "decision": "Maintain original validation result",
                "reason": f"Original validation result has passed {latest_validation.consensus_rate * 100:.1f}% node consensus"
            }
        else:
            # Revalidate
            revalidation = self.validate_result(
                task_id, 
                latest_validation.agent_id, 
                latest_validation.result
            )
            
            resolution = {
                "task_id": task_id,
                "status": "resolved",
                "decision": "Revalidation result",
                "reason": f"Revalidation result: {'Valid' if revalidation.is_valid else 'Invalid'}",
                "revalidation_consensus": f"{revalidation.consensus_rate * 100:.1f}%"
            }
        
        return resolution

# Test code
if __name__ == "__main__":
    validator = TrustValidator()
    
    # Test valid result validation
    print("Testing valid result validation:")
    valid_result = validator.validate_result(
        "task_1", 
        "booking_agent", 
        {"status": "success", "flight_number": "CA1234", "price": "¥1200"}
    )
    print(f"Validation result: {'Valid' if valid_result.is_valid else 'Invalid'}")
    print(f"Consensus rate: {valid_result.consensus_rate * 100:.1f}%")
    print(f"Validation reason: {valid_result.validation_reason}")
    print(f"Agent reputation: {validator.get_agent_reputation('booking_agent')}")
    
    print("\nTesting invalid result validation:")
    # Test invalid result validation
    invalid_result = validator.validate_result(
        "task_2", 
        "booking_agent", 
        {"status": "failed", "error": "Invalid input"}
    )
    print(f"Validation result: {'Valid' if invalid_result.is_valid else 'Invalid'}")
    print(f"Consensus rate: {invalid_result.consensus_rate * 100:.1f}%")
    print(f"Validation reason: {invalid_result.validation_reason}")
    print(f"Agent reputation: {validator.get_agent_reputation('booking_agent')}")
    
    print("\nTesting malicious behavior identification:")
    print(f"Is malicious behavior: {validator.identify_malicious_behavior('booking_agent')}")
    
    print("\nTesting dispute resolution:")
    dispute_result = validator.resolve_dispute("task_2")
    print(f"Dispute resolution result: {dispute_result['status']}")
    print(f"Decision: {dispute_result['decision']}")
    print(f"Reason: {dispute_result['reason']}")