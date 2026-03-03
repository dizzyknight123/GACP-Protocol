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

# Contract Generation Layer Code
# Implements automatic generation of cross-agent collaboration contracts based on structured goals, including responsibility definition, collaboration process, and breach accountability rules

import json
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class ContractTerm(BaseModel):
    """Contract Term"""
    term_id: str = Field(..., description="Term ID")
    description: str = Field(..., description="Term description")
    responsible_agent: str = Field(..., description="Responsible agent")
    deadline: Optional[str] = Field(default=None, description="Deadline")
    penalties: List[str] = Field(default_factory=list, description="Breach penalties")

class CollaborationContract(BaseModel):
    """Collaboration Contract"""
    contract_id: str = Field(..., description="Contract ID")
    creation_time: str = Field(..., description="Creation time")
    goal: str = Field(..., description="Contract goal")
    participating_agents: List[str] = Field(..., description="Participating agents list")
    terms: List[ContractTerm] = Field(..., description="Contract terms")
    collaboration_flow: List[Dict[str, Any]] = Field(..., description="Collaboration flow")
    dispute_resolution: str = Field(..., description="Dispute resolution mechanism")
    termination_conditions: List[str] = Field(..., description="Termination conditions")

class ContractGenerator:
    """Contract Generator"""
    
    def __init__(self):
        """Initialize generator"""
        self.agent_capabilities = {
            "booking_agent": ["book flight", "book hotel", "book meeting venue"],
            "transportation_agent": ["airport pickup", "city transportation", "logistics delivery"],
            "reimbursement_agent": ["expense reimbursement", "financial processing", "invoice management"],
            "research_agent": ["data collection", "data analysis", "report writing"],
            "meeting_agent": ["meeting arrangement", "material preparation", "meeting minutes"]
        }
    
    def generate_contract(self, structured_requirement: Dict[str, Any]) -> CollaborationContract:
        """
        Generate collaboration contract
        :param structured_requirement: Structured requirement
        :return: Collaboration contract object
        """
        # Generate contract ID
        contract_id = f"contract_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Extract goal and subtasks
        goal = structured_requirement.get("goal", "")
        subtasks = structured_requirement.get("subtasks", [])
        
        # Match agents
        participating_agents = self._match_agents(subtasks)
        
        # Generate contract terms
        terms = self._generate_terms(subtasks, participating_agents)
        
        # Generate collaboration flow
        collaboration_flow = self._generate_collaboration_flow(subtasks)
        
        # Generate contract
        contract = CollaborationContract(
            contract_id=contract_id,
            creation_time=datetime.now().isoformat(),
            goal=goal,
            participating_agents=participating_agents,
            terms=terms,
            collaboration_flow=collaboration_flow,
            dispute_resolution="Dispute resolution through multi-node consensus mechanism, resolution agreed by more than 2/3 nodes is final",
            termination_conditions=[
                "All tasks completed and verified",
                "Unrepairable technical failure occurred",
                "Contract terms violated and cannot be corrected",
                "User actively terminates"
            ]
        )
        
        return contract
    
    def _match_agents(self, subtasks: List[Dict[str, Any]]) -> List[str]:
        """
        Match agents
        :param subtasks: Subtask list
        :return: Participating agents list
        """
        agents = set()
        
        for subtask in subtasks:
            subtask_name = subtask.get("name", "")
            for agent, capabilities in self.agent_capabilities.items():
                for capability in capabilities:
                    if capability in subtask_name.lower():
                        agents.add(agent)
                        break
        
        # If no agent matched, add default agent
        if not agents:
            agents.add("general_agent")
        
        return list(agents)
    
    def _generate_terms(self, subtasks: List[Dict[str, Any]], agents: List[str]) -> List[ContractTerm]:
        """
        Generate contract terms
        :param subtasks: Subtask list
        :param agents: Participating agents list
        :return: Contract terms list
        """
        terms = []
        
        for i, subtask in enumerate(subtasks):
            # Match responsible agent
            responsible_agent = self._find_responsible_agent(subtask.get("name", ""), agents)
            
            # Generate term
            term = ContractTerm(
                term_id=f"term_{i+1}",
                description=subtask.get("description", ""),
                responsible_agent=responsible_agent,
                deadline="Within 24 hours after task starts",
                penalties=[
                    "Deduct reputation points",
                    "Suspend participation in new contracts",
                    "Permanent disablement for serious breaches"
                ]
            )
            terms.append(term)
        
        return terms
    
    def _find_responsible_agent(self, task_name: str, agents: List[str]) -> str:
        """
        Find responsible agent
        :param task_name: Task name
        :param agents: Participating agents list
        :return: Responsible agent
        """
        for agent in agents:
            capabilities = self.agent_capabilities.get(agent, [])
            for capability in capabilities:
                if capability in task_name.lower():
                    return agent
        
        # Return first agent as default
        return agents[0] if agents else "general_agent"
    
    def _generate_collaboration_flow(self, subtasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Generate collaboration flow
        :param subtasks: Subtask list
        :return: Collaboration flow
        """
        flow = []
        
        for i, subtask in enumerate(subtasks):
            flow_item = {
                "step": i + 1,
                "task": subtask.get("name", ""),
                "description": subtask.get("description", ""),
                "dependencies": [i] if i > 0 else []  # Simply depend on previous task
            }
            flow.append(flow_item)
        
        return flow
    
    def to_json(self, contract: CollaborationContract) -> str:
        """
        Convert contract to JSON string
        :param contract: Collaboration contract object
        :return: JSON string
        """
        return contract.json(ensure_ascii=False, indent=2)

# Test code
if __name__ == "__main__":
    # Simulate structured requirement
    structured_requirement = {
        "goal": "Book a flight from Beijing to Shanghai on March 10th, arrange airport pickup, and handle expense reimbursement.",
        "constraints": [
            {"type": "departure", "value": "Beijing"},
            {"type": "destination", "value": "Shanghai"},
            {"type": "date", "value": "2026-03-10"}
        ],
        "acceptance_criteria": [
            "Flight booking successful",
            "Hotel booking successful",
            "Pickup service arranged properly",
            "Reimbursement process completed"
        ],
        "subtasks": [
            {"name": "Book flight", "description": "Book a suitable flight according to requirements"},
            {"name": "Arrange accommodation", "description": "Arrange suitable hotel according to requirements"},
            {"name": "Airport pickup", "description": "Arrange airport pickup service"},
            {"name": "Expense reimbursement", "description": "Process travel expense reimbursement"}
        ],
        "priority": "medium"
    }
    
    generator = ContractGenerator()
    contract = generator.generate_contract(structured_requirement)
    print("Generated contract:")
    print(generator.to_json(contract))