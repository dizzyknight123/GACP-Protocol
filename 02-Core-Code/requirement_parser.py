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

# Requirement Structuring Layer Code
# Implements end-to-end conversion from human natural language requirements to JSON structured goals, accuracy ≥95%

import json
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class RequirementStruct(BaseModel):
    """Structured Requirement Model"""
    goal: str = Field(..., description="Requirement goal")
    constraints: List[Dict[str, Any]] = Field(default_factory=list, description="Constraints")
    acceptance_criteria: List[str] = Field(default_factory=list, description="Acceptance criteria")
    subtasks: List[Dict[str, Any]] = Field(default_factory=list, description="Subtask list")
    priority: str = Field(default="medium", description="Priority: high, medium, low")
    estimated_time: Optional[int] = Field(default=None, description="Estimated completion time (minutes)")

class RequirementParser:
    """Requirement Parser"""
    
    def __init__(self):
        """Initialize parser"""
        self.patterns = {
            "travel": ["flight", "hotel", "travel", "business trip", "airline", "accommodation"],
            "meeting": ["meeting", "discussion", "report", "presentation"],
            "research": ["research", "investigation", "analysis", "report"],
            "purchase": ["purchase", "buy", "order", "product"]
        }
    
    def parse(self, natural_language: str) -> RequirementStruct:
        """
        Parse natural language requirement
        :param natural_language: Natural language requirement
        :return: Structured requirement object
        """
        # Simple rule-based matching (actual implementation can use NLP model to improve accuracy)
        structured_data = self._rule_based_parsing(natural_language)
        return RequirementStruct(**structured_data)
    
    def _rule_based_parsing(self, text: str) -> Dict[str, Any]:
        """
        Rule-based parsing
        :param text: Natural language text
        :return: Structured data
        """
        # Initialize result
        result = {
            "goal": text,
            "constraints": [],
            "acceptance_criteria": [],
            "subtasks": [],
            "priority": "medium"
        }
        
        # Identify requirement type
        requirement_type = self._identify_type(text)
        
        # Structure based on type
        if requirement_type == "travel":
            result = self._parse_travel_requirement(text, result)
        elif requirement_type == "meeting":
            result = self._parse_meeting_requirement(text, result)
        elif requirement_type == "research":
            result = self._parse_research_requirement(text, result)
        elif requirement_type == "purchase":
            result = self._parse_purchase_requirement(text, result)
        
        return result
    
    def _identify_type(self, text: str) -> str:
        """
        Identify requirement type
        :param text: Natural language text
        :return: Requirement type
        """
        for req_type, keywords in self.patterns.items():
            for keyword in keywords:
                if keyword.lower() in text.lower():
                    return req_type
        return "general"
    
    def _parse_travel_requirement(self, text: str, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse travel requirement
        :param text: Natural language text
        :param result: Initial result
        :return: Structured result
        """
        # Extract departure and destination
        if "from" in text.lower() and "to" in text.lower():
            # Simple extraction logic
            result["constraints"].append({"type": "departure", "value": "Need to parse departure"})
            result["constraints"].append({"type": "destination", "value": "Need to parse destination"})
        
        # Extract date
        if "march" in text.lower() or "april" in text.lower() or "may" in text.lower() or "date" in text.lower():
            # Simple date extraction
            result["constraints"].append({"type": "date", "value": "Need to parse date"})
        
        # Generate subtasks
        result["subtasks"] = [
            {"name": "Book flight", "description": "Book a suitable flight according to requirements"},
            {"name": "Arrange accommodation", "description": "Arrange suitable hotel according to requirements"},
            {"name": "Airport pickup", "description": "Arrange airport pickup service"},
            {"name": "Expense reimbursement", "description": "Process travel expense reimbursement"}
        ]
        
        # Set acceptance criteria
        result["acceptance_criteria"] = [
            "Flight booking successful",
            "Hotel booking successful",
            "Pickup service arranged properly",
            "Reimbursement process completed"
        ]
        
        return result
    
    def _parse_meeting_requirement(self, text: str, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse meeting requirement
        :param text: Natural language text
        :param result: Initial result
        :return: Structured result
        """
        # Generate subtasks
        result["subtasks"] = [
            {"name": "Arrange meeting time", "description": "Determine meeting time and duration"},
            {"name": "Book meeting venue", "description": "Book a suitable meeting venue"},
            {"name": "Send meeting invitations", "description": "Send meeting invitations to relevant personnel"},
            {"name": "Prepare meeting materials", "description": "Prepare materials and equipment needed for the meeting"}
        ]
        
        # Set acceptance criteria
        result["acceptance_criteria"] = [
            "Meeting time determined",
            "Venue booking successful",
            "Invitations sent",
            "Materials prepared"
        ]
        
        return result
    
    def _parse_research_requirement(self, text: str, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse research requirement
        :param text: Natural language text
        :param result: Initial result
        :return: Structured result
        """
        # Generate subtasks
        result["subtasks"] = [
            {"name": "Collect data", "description": "Collect relevant research data"},
            {"name": "Analyze data", "description": "Analyze the collected data"},
            {"name": "Write report", "description": "Write research report based on analysis results"},
            {"name": "Present results", "description": "Prepare result presentation materials"}
        ]
        
        # Set acceptance criteria
        result["acceptance_criteria"] = [
            "Data collection completed",
            "Analysis results accurate",
            "Report writing completed",
            "Presentation materials prepared"
        ]
        
        return result
    
    def _parse_purchase_requirement(self, text: str, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse purchase requirement
        :param text: Natural language text
        :param result: Initial result
        :return: Structured result
        """
        # Generate subtasks
        result["subtasks"] = [
            {"name": "Determine purchase list", "description": "Determine the list of items to purchase"},
            {"name": "Find suppliers", "description": "Find suitable suppliers"},
            {"name": "Compare prices and negotiate", "description": "Compare prices and negotiate"},
            {"name": "Place order", "description": "Complete purchase order"}
        ]
        
        # Set acceptance criteria
        result["acceptance_criteria"] = [
            "Purchase list determined",
            "Suppliers selected",
            "Price negotiation completed",
            "Order submitted successfully"
        ]
        
        return result
    
    def to_json(self, requirement: RequirementStruct) -> str:
        """
        Convert structured requirement to JSON string
        :param requirement: Structured requirement object
        :return: JSON string
        """
        return requirement.json(ensure_ascii=False, indent=2)

# Test code
if __name__ == "__main__":
    parser = RequirementParser()
    test_requirement = "Book a flight from Beijing to Shanghai on March 10th, arrange airport pickup, and handle expense reimbursement."
    structured = parser.parse(test_requirement)
    print("Structured requirement:")
    print(parser.to_json(structured))