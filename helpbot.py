from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

def reset (usuario):
    os.system('sudo passwd ' + usuario) 
    print("Bot: Você já pode usar a nova senha!")

bot = ChatBot('helpdesk')

conversa = ['oi', 
	        'olá',
	        'preciso de ajuda', 
	        'em que posso ajudar?', 
	        'bom dia', 
            'bom dia para voce',
            'quem e voce',
            'sou um bot para ajudar',
            'obrigado',
            'de nada',
            'até logo', 
            'tchau']

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    quest = input('Humano: ')
    if quest.find('senha') != -1:
        print('Bot: Certo, qual usuário?')
        usuario = input('Humano: ')
        reset(usuario)
    else:     
        resposta = bot.get_response(quest)
        print('Bot: ', resposta)
