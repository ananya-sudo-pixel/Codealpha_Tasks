import random
import datetime

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_current_date():
    today = datetime.date.today()
    return today.strftime("%d %B %Y")

# Motivational lines
motivation_quotes = [
    "Believe in yourself ✨ You’re doing great!",
    "Every big step starts with a small move 🚀",
    "Don’t stop until you’re proud 💪",
    "You’re stronger than you think 💜",
]

# Jokes list
jokes = [
    "Why don’t programmers like nature? Too many bugs 🐛😂",
    "I would tell you a UDP joke, but you might not get it 😌",
    "Why did the computer get angry? Someone left it on CAPS LOCK 🔒😭",
]

def get_bot_response(user_input: str) -> str:
    """Return a response based on simple keyword matching."""
    text = user_input.lower().strip()

    # 1. Exit / goodbye
    if text in ["bye", "exit", "quit", "see you", "goodbye"]:
        return "It was great talking to you 😊 Bye! Have a wonderful day 💜"

    # 2. Greetings
    if any(word in text for word in ["hi", "hello", "hey"]):
        return random.choice([
            "Heyy! 😊 How can I help you today?",
            "Hello! 👋 Ask me something.",
            "Hi there! Ready to chat?"
        ])

    # 3. Compliments / appreciation
    if any(phrase in text for phrase in [
        "you are good",
        "you are nice",
        "you are awesome",
        "you are amazing",
        "you are great",
        "love you",
        "i like you"
    ]):
        return random.choice([
            "Aww thank you 🥺💜 That means a lot!",
            "Thank youuu! 😊 You're really sweet!",
            "Stop it, I'm blushing 🥹",
        ])

    # 4. Emotions / mood
    if any(word in text for word in ["sad", "upset", "not good", "tired", "bored", "lonely"]):
        return random.choice([
            "I’m here for you 💜 Do you want to talk about it?",
            "It’s okay to feel like that sometimes 🥺 You’ll be fine 💪",
            "Sending you virtual hugs 🤗💜 You are not alone.",
        ])

    # 5. How are you
    if "how are you" in text:
        return "I’m doing great 😄 just here being a helpful chatbot! How are you?"

    # 6. Name / identity
    if "who are you" in text or "your name" in text:
        return "I’m a simple Python chatbot created as a CodeAlpha project 🤖."

    # 7. Time
    if "time" in text:
        return f"The current time is {get_current_time()} ⏰"

    # 8. Date / day
    if "date" in text or "day" in text:
        return f"Today’s date is {get_current_date()} 📅"

    # 9. CodeAlpha info
    if "codealpha" in text:
        return ("CodeAlpha is an internship and learning platform where I was "
                "created as part of a Python development project 💻.")

    # 10. Motivation
    if any(word in text for word in ["motivate", "motivation", "inspire", "inspiration"]):
        return random.choice(motivation_quotes)

    # 11. Jokes
    if "joke" in text:
        return random.choice(jokes)

    # 12. Help / capabilities
    if "help" in text or "what can you do" in text:
        return (
            "I am a simple rule-based chatbot. I can respond to:\n"
            "- Greetings (hi, hello, hey)\n"
            "- How are you\n"
            "- Time / Date\n"
            "- Tell me a joke\n"
            "- Motivate me\n"
            "- Tell me about CodeAlpha\n"
            "- Simple emotional support (sad, bored, tired)\n"
            "- Appreciation messages (you are good, nice, awesome)\n"
            "- Type 'bye' to exit\n"
        )

    # 13. Default fallback
    return (
        "Hmm, I didn’t understand that 😅\n"
        "Try typing 'help' to see what I can do 💜"
    )

def main():
    print("=" * 60)
    print("          SIMPLE PYTHON CHATBOT - CODEALPHA PROJECT")
    print("=" * 60)
    print("Type your message and press Enter. Type 'bye' to end the chat.\n")

    while True:
        try:
            user_input = input("You: ")
            bot_reply = get_bot_response(user_input)
            print(f"Bot: {bot_reply}\n")
        except KeyboardInterrupt:
            print("\n\nBot: Oh, you pressed Ctrl+C. Bye! 👋")
            break

if __name__ == "__main__":
    main()
