
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')
conversation = [
    "Oi",
    "Olá tudo bem?",
    "O que você está fazendo?",
    "Eu estou estudando, e você?",
    "Legal ouvir isso!",
    "Obrigado.",
    "Seja bem vindo!",
    'Estou estudando também!',
    'Neymar jogador de futebol',
    'Gosto de formula 1'
]
trainer = ListTrainer(bot)
trainer.train(conversation)

while True:
    quest = input('Você: ')
    response = bot.get_response(quest)
    #if float(response.confidence) > 0.0:
    print('Bot: ',response)