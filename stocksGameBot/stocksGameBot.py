import os
import discord
from stockGamePlayers import Player

import pickle
from dotenv import load_dotenv


apikey = "0SA2DHWSEJAM986Y"
dataFile = "data.pickle"

startingCash = 10000

players = []

intents = discord.Intents.all()
client = discord.Client(intents=intents)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


def main():
    '''
    player1 = Player(10000, {"aapl": 1, "googl": 2})
    player2 = Player(9000, {"aapl": 5, "googl": 4})
    players.append(player1)
    players.append(player2)

    save(players)

    
    players = load_object(dataFile)

    for player in players:
        print(player)
    
    '''
    pass



@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD: 
            curGuild = guild
            break
    print("bot starting")
    players = load_object(dataFile)
    for player in players:
        print(player.user)
    
@client.event
async def on_message(message):
    players = load_object(dataFile)
    userNum = int()
    for i in range(len(players)):
        if (players[i].user == str(message.author)):
            userNum = i
            break
    msg = str(message.content).strip()

    args = msg.split()
    stock, amount = str(), int()

    if(len(args)>2):
        stock = args[1]
        amount= (args[2])
    elif(len(args) == 2):
        stock = args[1]
        amount = 1

    #try:
    if (msg == "!leader"):
        if str(message.author).strip() == "IsaaMaster#9938":
            text = str()
            for player in players:
                text += player.user + "\t\t\tPortfolio Value:  $" + str(player.getPortfolioValue()) +  "\n"
    
            await message.channel.send(text)
    elif (msg[0:4] == "!buy"):
        players[userNum].buy(stock, int(amount))
        await message.channel.send(str(amount) + " shares of " + stock + " bought!")
    elif (msg[0:5] == "!sell"):
        players[userNum].sell(stock, int(amount))
        await message.channel.send(str(amount) + " shares of " + stock + " sold!")
    elif(msg[0:10] == "!port"):
        await message.channel.send(str(players[userNum]))
    elif(msg[0:6] == "!value"):
        await message.channel.send(str("$" + players[userNum].getPortfolioValue()) + "   " + str(players[userNum].getPercentage())+"%")
    #except:
    #    await message.channel.send("Invliad arguments. You probaly did not have enought money to spend or stocks to sell")
    save(players)

def save(obj):
    try:
        with open("stocksGameBot/data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

def load_object(filename):
    try:
        with open("stocksGameBot/"+filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


def reset(members):
    for member in members:
        if not member.bot:
            players.append(Player(startingCash, dict(), member.name + "#" + str(member.discriminator)))
    save(players)

main()
client.run(TOKEN)

