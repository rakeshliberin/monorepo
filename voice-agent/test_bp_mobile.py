import asyncio
import os
from dotenv import load_dotenv
from src.main import SystemAgent, SessionState, TTSLanguageCodes
from livekit.agents import RunContext

async def test_get_bp_from_mobile(mobile_number: str):
    # Load environment variables
    load_dotenv()
    
    # Create a mock context
    class MockContext:
        def __init__(self):
            self.userdata = SessionState()
            self.userdata.tts_language_code = TTSLanguageCodes.ENGLISH
            
        async def say(self, message, allow_interruptions=True):
            print(f"Agent says: {message}")
    
    context = MockContext()
    
    # Create agent instance
    agent = SystemAgent()
    
    # Call the function
    print(f"\n🔍 Testing get_bp_from_mobile with number: {mobile_number}")
    result = await agent.get_bp_from_mobile(context, mobile_number)
    print("\n📋 Result:")
    print(result)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python test_bp_mobile.py <mobile_number>")
        print("Example: python test_bp_mobile.py 8750272155")
        sys.exit(1)
    
    mobile_number = sys.argv[1]
    asyncio.run(test_get_bp_from_mobile(mobile_number)) 