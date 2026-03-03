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

# End-to-end test script
# Generate 100 different natural language travel requirement test cases, covering different cities, dates, budgets, and task combinations

import random
import sys
import os

# Add core code directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '02-Core-Code'))

from gacp_mvp import GACPMVP

class E2ETest:
    """End-to-end test"""
    
    def __init__(self):
        self.mvp = GACPMVP()
        self.cities = [
            "Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Hangzhou", "Nanjing", "Chengdu", "Chongqing",
            "Wuhan", "Xi'an", "Xiamen", "Qingdao", "Dalian", "Changsha", "Tianjin"
        ]
        self.tasks = [
            "book flight", "arrange accommodation", "airport pickup", "expense reimbursement",
            "book meeting venue", "arrange catering", "itinerary planning", "visa application"
        ]
    
    def generate_test_cases(self, count: int = 100) -> list:
        """
        Generate test cases
        :param count: Number of test cases
        :return: List of test cases
        """
        test_cases = []
        
        for i in range(count):
            # Randomly select departure and destination
            departure = random.choice(self.cities)
            destination = random.choice([city for city in self.cities if city != departure])
            
            # Randomly generate date
            month = random.randint(3, 12)
            day = random.randint(1, 28)
            date = f"{month}/{day}"
            
            # Randomly select task combination
            task_count = random.randint(2, 4)
            selected_tasks = random.sample(self.tasks, task_count)
            task_description = ", ".join(selected_tasks)
            
            # Randomly add budget information
            budget = random.choice(["", "budget under 5000 yuan", "budget under 10000 yuan", "high-end business travel"])
            
            # Build natural language requirement
            requirement = f"{task_description} for {date} from {departure} to {destination}."
            if budget:
                requirement += f" {budget}."
            
            test_cases.append({
                "id": f"test_{i+1}",
                "requirement": requirement,
                "departure": departure,
                "destination": destination,
                "date": date,
                "tasks": selected_tasks,
                "budget": budget
            })
        
        return test_cases
    
    def run_test_cases(self, test_cases: list) -> dict:
        """
        Run test cases
        :param test_cases: List of test cases
        :return: Test results
        """
        results = {
            "total": len(test_cases),
            "passed": 0,
            "failed": 0,
            "details": []
        }
        
        for test_case in test_cases:
            print(f"Running test case: {test_case['id']}")
            print(f"Requirement: {test_case['requirement']}")
            
            try:
                result = self.mvp.run(test_case['requirement'])
                status = "passed" if result['overall_status'] == "success" else "failed"
                
                if status == "passed":
                    results["passed"] += 1
                else:
                    results["failed"] += 1
                
                results["details"].append({
                    "test_id": test_case['id'],
                    "requirement": test_case['requirement'],
                    "status": status,
                    "result": result
                })
                
                print(f"Test result: {status}")
            except Exception as e:
                results["failed"] += 1
                results["details"].append({
                    "test_id": test_case['id'],
                    "requirement": test_case['requirement'],
                    "status": "error",
                    "error": str(e)
                })
                print(f"Test result: error - {str(e)}")
            
            print("=" * 50)
        
        return results
    
    def generate_report(self, results: dict):
        """
        Generate test report
        :param results: Test results
        """
        print("=" * 100)
        print("GACP Protocol End-to-End Test Report")
        print("=" * 100)
        print(f"Total test cases: {results['total']}")
        print(f"Passed: {results['passed']}")
        print(f"Failed: {results['failed']}")
        print(f"Pass rate: {(results['passed'] / results['total']) * 100:.2f}%")
        print("=" * 100)
        
        # Analyze failure reasons
        failed_cases = [d for d in results['details'] if d['status'] != 'passed']
        if failed_cases:
            print("Failed test case analysis:")
            for case in failed_cases[:5]:  # Only show first 5 failed cases
                print(f"Test ID: {case['test_id']}")
                print(f"Requirement: {case['requirement']}")
                print(f"Status: {case['status']}")
                if 'error' in case:
                    print(f"Error: {case['error']}")
                print()

if __name__ == "__main__":
    # Create test instance
    tester = E2ETest()
    
    # Generate 10 test cases (can be set to 100 for actual run)
    test_cases = tester.generate_test_cases(10)
    
    # Run test cases
    results = tester.run_test_cases(test_cases)
    
    # Generate test report
    tester.generate_report(results)