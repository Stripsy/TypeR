#! /usr/bin/env python3
#!/usr/bin/python
# -*- coding: utf-8 -*-

import discord
import random
import asyncio
import time
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = ''

service = build('sheets', 'v4', credentials=creds)

token = ''

running = "off"


class MyClient(discord.Client):
    async def on_ready(self):
        print('Connecté en tant que : ',  self.user.name,  self.user.id)
        print('--------------------------------------------------')

    async def on_message(self,  message):

        if message.author.id == self.user.id:
            return
        global running
        if message.content == '!start' and running == "off":

            running = "on"

            # Choix de la phrase depuis un gen

            url = "http://metaphorpsum.com/sentences/1"

            resp = requests.get(url)

            url = "https://enneagon.org/phrases"
            headers = {'nb':	"1"}

            x = requests.post(url, data = headers)

            soup = BeautifulSoup(x.text, "html.parser")

            for data in soup.find_all("div", class_= "main"):
                letexte = data.find('p').text



            # Choix aléatoire de la phrase depuis une liste perso > comptage du nombre de mots

            rand = random.randrange(len(line))



            # Choix aléatoire de la phrase depuis un sheet

            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range="A1:A9999").execute()
            values = result.get('values', [])

            # Choix aléatoire de la phrase depuis une liste perso > comptage du nombre de mots

            rands = random.randrange(len(values))

            parse = (','.join(values[rands]))

            # Sheet
            phrase = parse


            count_word = phrase.split()
            numb_word = len(count_word)

            # Nombre d'espaces
            
            space = phrase.count(' ')
            
            # Affichage décompte

            decompte3 = discord.Embed(title="Démarrage du test : 3️⃣", color=0xff0000)
            decompte2 = discord.Embed(title="Démarrage du test : 2️⃣", color=0xfeff00)
            decompte1 = discord.Embed(title="Démarrage du test : 1️⃣", color=0xfe7d00)
            decompte0 = discord.Embed(title="Go ! 🏁", color=0x00ff00)
            laphrase = discord.Embed(title="Blabla", description=phrase, color=0x000000)

            state = await message.channel.send(embed=decompte3)
            await asyncio.sleep(1)
            await state.edit(embed=decompte2)
            await asyncio.sleep(1)
            await state.edit(embed=decompte1)
            await asyncio.sleep(1)
            await state.edit(embed=decompte0)
            await state.edit(embed=laphrase)
            


            # Lancement du chrono

            start_time = time.time()

            
            def is_correct(msg):
                return msg.author == message.author

            # Vérification de la réponse utilisateur

            guess = await self.wait_for('message',  check=is_correct)
            print(len(guess.content))

            if guess.content == phrase:
                    
                # Temps passé
                temps = time.time() - start_time

                # WPM
                text_length = len(phrase)

                words_per_m = text_length/5/(temps/60)

                # Affichage fin de test

                embed=discord.Embed(title=" ")
                embed.set_author(name=message.author.name+" votre test est terminé !", icon_url=message.author.avatar_url)
                embed.add_field(name="WPM", value=round(words_per_m,2), inline=True)
                embed.add_field(name="Faute", value="**0**", inline=True)
                embed.add_field(name="Temps", value=str(round(temps,3))+"s", inline=True)
                await message.channel.send(embed=embed)
                running = "off"
                

                
            else:
                # Liste des mots
                detail = guess.content.split()

                # Temps passé

                temps = time.time() - start_time

                # S'il y a moins de mots qu'attendu perdu
                
                if len(detail) < len(count_word):
                    if space != guess.content.count(' '):
                        inc = discord.Embed(title="Refusé !", color=0xff0000)
                        await message.channel.send(embed=inc)
                        running = "off"

                else:
                    i = 0
                    incorrect = []
                    for m in count_word:

                        if m == detail[i]:
                            i +=1
                        else:
                            incorrect.insert(i,str(detail[i]))
                            i +=1

                    # WPM

                    text_length = len(phrase)
                    words_per_m = text_length/5/(temps/60) 

                    err = "**"+str(len(incorrect))+"**"+" "+str(incorrect)        
                    embed=discord.Embed(title=" ")
                    embed.set_author(name=message.author.name+" votre test est terminé !", icon_url=message.author.avatar_url)
                    embed.add_field(name="WPM", value=round(words_per_m,2), inline=True)
                    embed.add_field(name="Fautes", value=err, inline=True)
                    embed.add_field(name="Temps", value=str(round(temps,3))+"s", inline=True)
                    await message.channel.send(embed=embed)
                    running = "off" 
        if message.content == '!start' and running == "on":
            run = discord.Embed(title="Test déjà en cours !", color=0xff0000)
            await message.channel.send(embed=run)              
                

client = MyClient()
client.run(token)