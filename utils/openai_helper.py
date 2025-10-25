import openai
from typing import Dict, Any

def chat_helper(message: str) -> Dict[str, Any]:
    """
    Helper function to interact with OpenAI's chat API
    """
    try:
        client = openai.OpenAI()
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        
        return {
            "success": True,
            "response": response.choices[0].message.content
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
