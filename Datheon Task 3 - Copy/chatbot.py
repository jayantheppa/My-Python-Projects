
import re

faq = {
    "hours": (
        r"\b(hours|open|close|opening|closing)\b",
        "Our business hours are Monday to Saturday, 9 AM to 6 PM."
    ),
    "delivery": (
        r"\b(delivery|shipping|deliver)\b",
        "Standard delivery usually takes 3-5 business days."
    ),
    "returns": (
        r"\b(return|refund|exchange)\b",
        "Products can be returned within 7 days of delivery, subject to our return policy."
    ),
    "payment": (
        r"\b(payment|pay|upi|card)\b",
        "We accept UPI, debit cards, credit cards, and online payments."
    ),
    "products": (
        r"\b(product|products|catalog|items)\b",
        "We offer a range of products. Which product are you interested in?"
    )
}

def chatbot():
    print("=" * 45)
    print("RULE-BASED CUSTOMER SUPPORT CHATBOT")
    print("=" * 45)
    print("Bot: Hello! How can I help you today?")
    print("Bot: Type bye, exit, or quit to stop.")

    while True:
        user_input = input("\nYou: ").strip().lower()

        if re.fullmatch(r"(bye|exit|quit)", user_input):
            print("Bot: Thank you for chatting. Goodbye!")
            break

        if not user_input:
            print("Bot: Please enter a question.")
            continue

        if re.search(r"\b(hi|hello|hey)\b", user_input):
            print("Bot: Hello! How can I help you?")
            continue

        if re.search(r"\b(thanks|thank you)\b", user_input):
            print("Bot: You're welcome!")
            continue

        found = False

        for pattern, response in faq.values():
            if re.search(pattern, user_input):
                print("Bot:", response)
                found = True
                break

        if not found:
            print(
                "Bot: Sorry, I didn't understand. Ask about "
                "business hours, delivery, returns, payments, or products."
            )

if __name__ == "__main__":
    chatbot()
