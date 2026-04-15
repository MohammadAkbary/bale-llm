"""
Examples of using DeepSeek API with the Bale LLM Bot

DeepSeek Integration Examples
"""

from ai_handler import AIHandler
import asyncio

async def example_deepseek():
    """مثال استفاده از DeepSeek API"""
    
    ai = AIHandler()
    
    # Example 1: Using DeepSeek
    print("=" * 50)
    print("Example 1: Using DeepSeek API")
    print("=" * 50)
    
    response = await ai.get_response(
        "سلام! چطور می‌تونم از DeepSeek استفاده کنم؟",
        use_service='deepseek'
    )
    print(f"Response: {response}\n")
    
    # Example 2: English message
    print("=" * 50)
    print("Example 2: English Message via DeepSeek")
    print("=" * 50)
    
    response = await ai.get_response(
        "Hello! Tell me a short joke.",
        use_service='deepseek'
    )
    print(f"Response: {response}\n")
    
    # Example 3: Code generation
    print("=" * 50)
    print("Example 3: Code Generation with DeepSeek")
    print("=" * 50)
    
    response = await ai.get_response(
        "Write a Python function to check if a string is a palindrome",
        use_service='deepseek'
    )
    print(f"Response: {response}\n")

async def example_compare_services():
    """مقایسه سرویس‌های مختلف"""
    
    ai = AIHandler()
    question = "What is artificial intelligence?"
    
    print("=" * 50)
    print("Comparing Different AI Services")
    print("=" * 50)
    
    services = ['google', 'huggingface', 'deepseek']
    
    for service in services:
        print(f"\n📌 Using {service.upper()}")
        print("-" * 40)
        
        try:
            response = await ai.get_response(question, use_service=service)
            # Print first 200 chars
            print(f"Response: {response[:200]}...")
        except Exception as e:
            print(f"Error: {str(e)}")

async def main():
    """Run all examples"""
    print("\n🚀 Bale LLM Bot - AI Services Examples\n")
    
    # Run examples
    await example_deepseek()
    print("\n")
    # await example_compare_services()

if __name__ == '__main__':
    asyncio.run(main())
