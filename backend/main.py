from profile_analyzer import ProfileAnalyzer
from conversation_generator import ConversationGenerator
from history_logger import HistoryLogger

def main():
    print("=== Personalized Networking Assistant ===")

    name = input("Enter your name: ")
    interests = input("Enter your interests: ")
    event = input("Enter the event name: ")

    analyzer = ProfileAnalyzer()
    profile = analyzer.analyze_profile(name, interests, event)

    generator = ConversationGenerator()
    conversation = generator.generate_conversation(profile)

    print("\nGenerated Conversation:\n")
    print(conversation)

    logger = HistoryLogger()
    logger.save_history(profile, conversation)

    print("\nConversation saved successfully!")

if __name__ == "__main__":
    main()