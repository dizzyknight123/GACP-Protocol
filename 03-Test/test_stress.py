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

# Stress test script
# Simulate 10000+ concurrent collaboration tasks to test protocol throughput, latency, and failure rate

import time
import concurrent.futures
import sys
import os

# Add core code directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '02-Core-Code'))

from gacp_mvp import GACPMVP

class StressTest:
    """Stress test"""
    
    def __init__(self):
        self.mvp = GACPMVP()
    
    def test_single_task(self, task_id: int) -> dict:
        """
        Test single task
        :param task_id: Task ID
        :return: Task execution result
        """
        # Generate test requirement
        requirement = f"Stress test task {task_id}: Book flight from Beijing to Shanghai"
        
        start_time = time.time()
        try:
            result = self.mvp.run(requirement)
            end_time = time.time()
            return {
                "task_id": task_id,
                "status": "success" if result['overall_status'] == "success" else "failed",
                "latency": end_time - start_time,
                "result": result
            }
        except Exception as e:
            end_time = time.time()
            return {
                "task_id": task_id,
                "status": "error",
                "latency": end_time - start_time,
                "error": str(e)
            }
    
    def run_concurrent_tasks(self, task_count: int, max_workers: int = 10) -> dict:
        """
        Run concurrent tasks
        :param task_count: Number of tasks
        :param max_workers: Maximum number of worker threads
        :return: Test results
        """
        results = {
            "total": task_count,
            "success": 0,
            "failed": 0,
            "error": 0,
            "latencies": [],
            "start_time": time.time()
        }
        
        print(f"Starting execution of {task_count} concurrent tasks...")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit tasks
            future_to_task = {executor.submit(self.test_single_task, i): i for i in range(task_count)}
            
            # Collect results
            for future in concurrent.futures.as_completed(future_to_task):
                task_id = future_to_task[future]
                try:
                    result = future.result()
                    results["latencies"].append(result["latency"])
                    
                    if result["status"] == "success":
                        results["success"] += 1
                    elif result["status"] == "failed":
                        results["failed"] += 1
                    else:
                        results["error"] += 1
                except Exception as e:
                    results["error"] += 1
                    print(f"Task {task_id} execution exception: {str(e)}")
        
        results["end_time"] = time.time()
        results["total_time"] = results["end_time"] - results["start_time"]
        
        return results
    
    def analyze_results(self, results: dict):
        """
        Analyze test results
        :param results: Test results
        """
        print("=" * 100)
        print("GACP Protocol Stress Test Report")
        print("=" * 100)
        
        # Calculate statistics
        total_time = results["total_time"]
        throughput = results["total"] / total_time if total_time > 0 else 0
        avg_latency = sum(results["latencies"]) / len(results["latencies"]) if results["latencies"] else 0
        max_latency = max(results["latencies"]) if results["latencies"] else 0
        min_latency = min(results["latencies"]) if results["latencies"] else 0
        
        # Print results
        print(f"Total tasks: {results['total']}")
        print(f"Success: {results['success']}")
        print(f"Failed: {results['failed']}")
        print(f"Error: {results['error']}")
        print(f"Success rate: {(results['success'] / results['total']) * 100:.2f}%")
        print(f"Total execution time: {total_time:.2f} seconds")
        print(f"Throughput: {throughput:.2f} tasks/second")
        print(f"Average latency: {avg_latency:.2f} seconds")
        print(f"Maximum latency: {max_latency:.2f} seconds")
        print(f"Minimum latency: {min_latency:.2f} seconds")
        print("=" * 100)
    
    def run_scalability_test(self):
        """
        Run scalability test
        """
        print("Starting scalability test...")
        
        # Test different concurrency levels
        test_sizes = [10, 100, 500, 1000]
        
        for size in test_sizes:
            print(f"\nTesting concurrency level: {size}")
            results = self.run_concurrent_tasks(size, max_workers=min(size, 50))
            self.analyze_results(results)

if __name__ == "__main__":
    # Create stress test instance
    stress_test = StressTest()
    
    # Run scalability test
    stress_test.run_scalability_test()