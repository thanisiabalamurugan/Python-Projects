'''from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Step 1: Create a ChatBot instance
bot = ChatBot('SimpleBot')

# Step 2: Create and set up a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# Step 3: Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Step 4: Run a loop to get user input and get the bot's response
print("ChatBot: Hi, I am a simple chatbot. You can start chatting with me. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = bot.get_response(user_input)
    print("ChatBot:", response)'''

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y
    
    

def calculator():
    print("Yooo! It's a calculator")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
 

    while True:
        print("What to do with numbers bruh?")
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator....Bye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please try again.")
            continue

        

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}\n simple bruh\n")

        elif choice == '2':
            print(f"Result: {num1} + {num2} = {subtract(num1, num2)}\n simple bruh\n")
        elif choice == '3':
            print(f"Result: {num1} + {num2} = {multiply(num1, num2)}\n simple bruh\n")
        elif choice == '4':
            print(f"Result: {num1} + {num2} = {divide(num1, num2)}\n simple bruh\n")
        else:
            print("Invalid input. Please try again.\n")

if __name__ == "__main__":
    calculator()

