from chatterbot import ChatBot
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
    print("ChatBot:", response)
