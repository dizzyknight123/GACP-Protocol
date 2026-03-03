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

# Task Routing Layer Code
# Implements automatic task decomposition, agent matching, dynamic routing scheduling, supports multi-agent serial/parallel collaboration

import json
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class Task(BaseModel):
    """Task Model"""
    task_id: str = Field(..., description="Task ID")
    name: str = Field(..., description="Task name")
    description: str = Field(..., description="Task description")
    agent_id: str = Field(..., description="Responsible agent ID")
    priority: str = Field(default="medium", description="Priority: high, medium, low")
    status: str = Field(default="pending", description="Status: pending, in_progress, completed, failed")
    dependencies: List[str] = Field(default_factory=list, description="Dependency task ID list")
    estimated_time: Optional[int] = Field(default=None, description="Estimated completion time (minutes)")
    actual_time: Optional[int] = Field(default=None, description="Actual completion time (minutes)")

class TaskRouter:
    """Task Router"""
    
    def __init__(self):
        """Initialize router"""
        self.agents = {
            "booking_agent": {
                "capabilities": ["book flight", "book hotel", "book meeting venue"],
                "availability": True,
                "performance_score": 0.95
            },
            "transportation_agent": {
                "capabilities": ["airport pickup", "city transportation", "logistics delivery"],
                "availability": True,
                "performance_score": 0.92
            },
            "reimbursement_agent": {
                "capabilities": ["expense reimbursement", "financial processing", "invoice management"],
                "availability": True,
                "performance_score": 0.98
            },
            "research_agent": {
                "capabilities": ["data collection", "data analysis", "report writing"],
                "availability": True,
                "performance_score": 0.90
            },
            "meeting_agent": {
                "capabilities": ["meeting arrangement", "material preparation", "meeting minutes"],
                "availability": True,
                "performance_score": 0.93
            }
        }
        
        self.tasks = {}
    
    def route_tasks(self, subtasks: List[Dict[str, Any]]) -> List[Task]:
        """
        Route tasks
        :param subtasks: Subtask list
        :return: Routed task list
        """
        routed_tasks = []
        
        for i, subtask in enumerate(subtasks):
            # Generate task ID
            task_id = f"task_{datetime.now().strftime('%Y%m%d%H%M%S')}_{i}"
            
            # Match agent
            agent_id = self._match_agent(subtask.get("name", ""))
            
            # Create task
            task = Task(
                task_id=task_id,
                name=subtask.get("name", ""),
                description=subtask.get("description", ""),
                agent_id=agent_id,
                dependencies=[f"task_{datetime.now().strftime('%Y%m%d%H%M%S')}_{i-1}"] if i > 0 else [],
                estimated_time=30  # Default estimated time
            )
            
            routed_tasks.append(task)
            self.tasks[task_id] = task
        
        return routed_tasks
    
    def _match_agent(self, task_name: str) -> str:
        """
        Match agent
        :param task_name: Task name
        :return: Agent ID
        """
        best_agent = "general_agent"
        best_score = 0
        
        for agent_id, agent_info in self.agents.items():
            if not agent_info.get("availability", False):
                continue
            
            # Calculate matching score
            score = 0
            for capability in agent_info.get("capabilities", []):
                if capability in task_name.lower():
                    score += 1
            
            # Combine with performance score
            total_score = score * agent_info.get("performance_score", 0)
            
            if total_score > best_score:
                best_score = total_score
                best_agent = agent_id
        
        return best_agent
    
    def schedule_tasks(self, tasks: List[Task]) -> List[Dict[str, Any]]:
        """
        Schedule tasks
        :param tasks: Task list
        :return: Schedule plan
        """
        # Build dependency graph
        dependency_graph = {}
        for task in tasks:
            dependency_graph[task.task_id] = task.dependencies
        
        # Topological sort
        schedule = self._topological_sort(dependency_graph)
        
        # Generate schedule plan
        schedule_plan = []
        for task_id in schedule:
            task = self.tasks.get(task_id)
            if task:
                schedule_plan.append({
                    "task_id": task.task_id,
                    "task_name": task.name,
                    "agent_id": task.agent_id,
                    "status": task.status,
                    "dependencies": task.dependencies
                })
        
        return schedule_plan
    
    def _topological_sort(self, graph: Dict[str, List[str]]) -> List[str]:
        """
        Topological sort
        :param graph: Dependency graph
        :return: Sorted task ID list
        """
        # Calculate in-degree
        in_degree = {}
        for node in graph:
            in_degree[node] = 0
        
        for node in graph:
            for neighbor in graph[node]:
                if neighbor in in_degree:
                    in_degree[neighbor] += 1
        
        # Initialize queue
        queue = []
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)
        
        # Topological sort
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node)
            
            for neighbor in graph.get(node, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result
    
    def update_task_status(self, task_id: str, status: str) -> bool:
        """
        Update task status
        :param task_id: Task ID
        :param status: New status
        :return: Whether update was successful
        """
        if task_id in self.tasks:
            self.tasks[task_id].status = status
            return True
        return False
    
    def get_task_status(self, task_id: str) -> Optional[str]:
        """
        Get task status
        :param task_id: Task ID
        :return: Task status
        """
        if task_id in self.tasks:
            return self.tasks[task_id].status
        return None

# Test code
if __name__ == "__main__":
    # Simulate subtasks
    subtasks = [
        {"name": "Book flight", "description": "Book a suitable flight according to requirements"},
        {"name": "Arrange accommodation", "description": "Arrange suitable hotel according to requirements"},
        {"name": "Airport pickup", "description": "Arrange airport pickup service"},
        {"name": "Expense reimbursement", "description": "Process travel expense reimbursement"}
    ]
    
    router = TaskRouter()
    tasks = router.route_tasks(subtasks)
    
    print("Routed tasks:")
    for task in tasks:
        print(f"Task ID: {task.task_id}, Name: {task.name}, Agent: {task.agent_id}, Dependencies: {task.dependencies}")
    
    print("\nSchedule plan:")
    schedule = router.schedule_tasks(tasks)
    for item in schedule:
        print(f"Step: {schedule.index(item) + 1}, Task: {item['task_name']}, Agent: {item['agent_id']}")