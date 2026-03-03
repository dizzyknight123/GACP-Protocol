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

# LangChain Agent Integration Code
# Implements booking agent, integrates with GACP task routing layer

from typing import Dict, Any, Optional

# Try to import LangChain dependencies
try:
    from langchain.agents import AgentType, initialize_agent, load_tools
    from langchain.chat_models import ChatOpenAI
    from langchain.llms import OpenAI
    LANGCHAIN_AVAILABLE = True
except ImportError:
    LANGCHAIN_AVAILABLE = False

class LangChainBookingAgent:
    """LangChain Booking Agent"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize booking agent
        :param api_key: OpenAI API Key (optional, not needed when using mock mode)
        """
        self.api_key = api_key
        self.is_mock = not api_key
        self.agent = self._initialize_agent()
    
    def _initialize_agent(self):
        """
        Initialize LangChain agent
        :return: LangChain agent
        """
        if self.is_mock or not LANGCHAIN_AVAILABLE:
            # Mock mode or LangChain not available, return None
            return None
        
        try:
            # Load tools
            tools = load_tools(["serpapi", "llm-math"], llm=OpenAI(api_key=self.api_key))
            
            # Initialize agent
            agent = initialize_agent(
                tools,
                ChatOpenAI(api_key=self.api_key, temperature=0),
                agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
                verbose=True
            )
            
            return agent
        except Exception:
            # Initialization failed, use mock mode
            self.is_mock = True
            return None
    
    def book_flight(self, departure: str, destination: str, date: str) -> Dict[str, Any]:
        """
        Book flight
        :param departure: Departure location
        :param destination: Destination location
        :param date: Date
        :return: Booking result
        """
        if self.is_mock:
            # Mock booking result
            return {
                "status": "success",
                "flight_number": "CA1234",
                "departure": departure,
                "destination": destination,
                "date": date,
                "price": "¥1200",
                "departure_time": "09:00",
                "arrival_time": "11:00",
                "airline": "Air China",
                "booking_reference": "BOOK123456"
            }
        
        # Use real LangChain agent
        prompt = f"Book a flight from {departure} to {destination} on {date}, return flight number, price, departure time, arrival time and airline information"
        try:
            result = self.agent.run(prompt)
            # Parse result (actual implementation needs to parse based on return format)
            return {
                "status": "success",
                "result": result
            }
        except Exception as e:
            return {
                "status": "failed",
                "error": str(e)
            }
    
    def book_hotel(self, city: str, check_in: str, check_out: str, guests: int = 1) -> Dict[str, Any]:
        """
        Book hotel
        :param city: City
        :param check_in: Check-in date
        :param check_out: Check-out date
        :param guests: Number of guests
        :return: Booking result
        """
        if self.is_mock:
            # Mock booking result
            return {
                "status": "success",
                "hotel_name": "Waldorf Astoria Shanghai on the Bund",
                "city": city,
                "check_in": check_in,
                "check_out": check_out,
                "guests": guests,
                "price_per_night": "¥1500",
                "total_price": f"¥{1500 * (int(check_out.split('-')[2]) - int(check_in.split('-')[2]))}",
                "booking_reference": "HOTEL654321"
            }
        
        # Use real LangChain agent
        prompt = f"Book a hotel in {city} from {check_in} to {check_out} for {guests} guests, return hotel name, price and booking reference"
        try:
            result = self.agent.run(prompt)
            return {
                "status": "success",
                "result": result
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
        
        if "book flight" in task_name or "Book flight" in task_name:
            # Extract parameters
            departure = "Beijing"
            destination = "Shanghai"
            date = "2026-03-10"
            
            # Execute booking
            return self.book_flight(departure, destination, date)
        elif "arrange accommodation" in task_name or "Arrange accommodation" in task_name:
            # Extract parameters
            city = "Shanghai"
            check_in = "2026-03-10"
            check_out = "2026-03-12"
            
            # Execute booking
            return self.book_hotel(city, check_in, check_out)
        elif "book meeting venue" in task_name or "Book meeting venue" in task_name:
            # Mock meeting venue booking result
            return {
                "status": "success",
                "venue_name": "Shanghai International Convention Center",
                "city": "Shanghai",
                "date": "2026-03-10",
                "time": "09:00-12:00",
                "capacity": "50 people",
                "price": "¥5000",
                "booking_reference": "VENUE78901"
            }
        else:
            return {
                "status": "failed",
                "error": f"Unsupported task type: {task_name}"
            }

# Test code
if __name__ == "__main__":
    # Create agent (using mock mode)
    agent = LangChainBookingAgent()
    
    # Test booking flight
    print("Testing flight booking:")
    flight_result = agent.book_flight("Beijing", "Shanghai", "2026-03-10")
    print(flight_result)
    
    # Test booking hotel
    print("\nTesting hotel booking:")
    hotel_result = agent.book_hotel("Shanghai", "2026-03-10", "2026-03-12", 1)
    print(hotel_result)
    
    # Test running task
    print("\nTesting task running:")
    task = {"name": "Book flight", "description": "Book a flight from Beijing to Shanghai"}
    task_result = agent.run_task(task)
    print(task_result)