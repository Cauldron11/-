import os
import sys
from dotenv import load_dotenv
from core.agent import TutorAgent
from utils.logger import setup_logger

def main():
    load_dotenv()
    logger = setup_logger()
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logger.error("Missing GEMINI_API_KEY in .env file.")
        sys.exit(1)

    # Example student profile (could be loaded from data/profiles.json)
    student_profile = {
        "name": "Alex",
        "level": "High School / Tech Enthusiast",
        "interests": ["Android Modding", "Python", "Minecraft Architecture"],
        "learning_style": "Hands-on, technical, prefers CLI examples over theory."
    }

    tutor = TutorAgent(api_key, student_profile)
    
    print("\033[94m[ZenTutor] Connection established. Type 'exit' to quit.\033[0m")
    
    while True:
        try:
            user_input = input("\033[92mStudent >> \033[0m")
            if user_input.lower() in ['exit', 'quit']:
                break
            
            response = tutor.chat(user_input)
            print(f"\n\033[1mAI Tutor:\033[0m\n{response}\n")
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
