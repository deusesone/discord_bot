import discord
import random
import requests
import lxml
from bs4 import BeautifulSoup
from lxml import html
from lxml import etree
from lxml import html
import os
import re
from discord.ext import commands
import config
import youtube_dl
from discord.voice_client import VoiceClient
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import urllib
import urllib.request
import urllib.parse, urllib.request, re
import yt_search
import discord
from discord.ext import tasks
import aiohttp


video_names = []
video_ids = []
len_video_names = 0
list_play_by_name = []

#создание класса
client = commands.Bot(command_prefix = '!', intents = discord.Intents.all())






#для работы с openweatherapi

list_of_nicknames = []

@tasks.loop(hours=12)
async def test():
	channel = client.get_channel(434110578798362627)
	await channel.send(file=discord.File("/home/pi/nastya/delete.png"))
@client.event




@client.event
async def on_ready():
	test.start()
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('бравл старс'))
	print('We have logged in as {0.user}'.format(client))
	print('version 0.0.1')



@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(f'Приветствую {member.name} на нашем сервере!')
	role = discord.utils.get(member.guild.roles, id=int(688128825112264746))
	await member.add_roles(role)
	await client.process_commands(message)



@client.command(pass_context=True)
async def meme(ctx):
	embed = discord.Embed(title="", description="")

	async with aiohttp.ClientSession() as cs:
		async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot/') as r:
			res = await r.json(content_type=None)

			url=res['data']['children'] [random.randint(0, 30)]['data']['url']
			channel = client.get_channel(434110578798362627)
			await channel.send(url)

@client.command(pass_context=True)
async def cat(ctx):
	embed = discord.Embed(title="", description="")

	async with aiohttp.ClientSession() as cs:
		async with cs.get('https://www.reddit.com/r/cats/new.json?sort=hot/') as r:
			res = await r.json()

			url=res['data']['children'] [random.randint(0, 30)]['data']['url']
			channel = client.get_channel(434110578798362627)
			await channel.send(url)


@client.command(pass_context=True)
async def trap(ctx):
	embed = discord.Embed(title="", description="")

	async with aiohttp.ClientSession() as cs:
		async with cs.get('https://www.reddit.com/r/traps/new.json?sort=hot/') as r:
			res = await r.json()

			url=res['data']['children'] [random.randint(0, 20)]['data']['url']
			channel = client.get_channel(434110578798362627)
			await channel.send(url)




@client.command(pass_context=True)
async def r6(ctx, arg1, arg2):
	if arg1 == "stats":
		try:
			nick_name = arg2
			url_stat = 'https://r6.tracker.network/profile/pc/' + nick_name
			r = requests.get(url_stat)
			with open('stat.html', 'wt', encoding="utf-8") as output_file:
				output_file.write(r.text)
			with open('stat.html', 'r', encoding="utf-8") as f:
				contents = f.read()
			#os.remove("stat.html")
			mmr_general = 1
			count_classes = 0
			soup = BeautifulSoup(contents, 'html.parser')
			l = 0
			best_mmr = "-"
			for name_box in soup.find_all('div', {'class': 'trn-text--dimmed'}):
				count_classes = count_classes + 1
				name = name_box.text.strip()
				if count_classes == 3:
					mmr_general = name
			count_classes = 0
			mmr_general_rank = "-"
			mmr_general_kd = 0
			mmr_general_wl = "-"
			matсhes_played = 0
			time_played = "-"
			level = "-"
			wins = 0
			losses = 0
			headshots = "-"
			headshots_percent = "-"
			deaths = "-"
			rank_icon = "-"
			melee_kills = "-"
			for name_box in soup.find_all('div', {'class': 'trn-defstat__value'}):
				name = name_box.text.strip()
				count_classes = count_classes + 1
				if count_classes == 3:
					best_mmr = name
				if count_classes == 1:
					level = name
				if count_classes == 8:
					kills = name
				if count_classes == 19:
					deaths = name
				if count_classes == 20:
					headshots = name
				if count_classes == 17:
					headshots_percent = name
				if count_classes == 68:
					mmr_general_rank = name
				if count_classes == 18:
					mmr_general_kd = name
				if count_classes == 24:
					time_played = name
				if count_classes == 21:
					wins = name
				if count_classes == 22:
					losses = name
				if count_classes == 27:
					melee_kills = name
			count_classes = 0
			headshots_percent = headshots_percent[0:-1]
			headshots = headshots.replace(",","")
			kills = float(headshots)/float(headshots_percent)
			for name_box in soup.find_all('div', {'class': 'trn-defstat__value'}):
				name = name_box.text.strip()
				count_classes = count_classes + 1
				name = name_box.text.strip()
				if count_classes == 25:
					matсhes_played = name
				if count_classes == 23:
					mmr_general_wl = name


			image_tags = soup.find_all('img')
			count_classes = 0
			avatar = "-"
			for image_tag in image_tags:
				count_classes = count_classes + 1
				if count_classes == 2:
					avatar = image_tag.get('src')
				if count_classes == 8:
					rank_icon = image_tag.get('src')

			image_tags = soup.find_all('img')
			count_classes = 0
			operator1 = "-"
			operator2 = "-"
			operator3 = "-"
			for image_tag in image_tags:
				count_classes = count_classes + 1
				if count_classes == 3:
					operator1 = image_tag.get('title')
				if count_classes == 4:
					operator2 = image_tag.get('title')
				if count_classes == 5:
					operator3 = image_tag.get('title')
			print(best_mmr)
			if mmr_general_rank.startswith("COPPER"):
				embed=discord.Embed(title="Статистика", url="https://r6.tracker.network/profile/pc/" + nick_name, description='Матчей сыграно: ' + matсhes_played, color=0xd24b2d)
			if mmr_general_rank.startswith("BRONZE"):
				embed=discord.Embed(title="Статистика", url="https://r6.tracker.network/profile/pc/" + nick_name, description='Матчей сыграно: ' + matсhes_played, color=0xdd9c3e)
			if mmr_general_rank.startswith("SILVER"):
				embed=discord.Embed(title="Статистика", url="https://r6.tracker.network/profile/pc/" + nick_name, description='Матчей сыграно: ' + matсhes_played, color=0xcccccc)
			if mmr_general_rank.startswith("GOLD"):
				embed=discord.Embed(title="Статистика", url="https://r6.tracker.network/profile/pc/" + nick_name, description='Матчей сыграно: ' + matсhes_played, color=0xf5e95f)
			if mmr_general_rank.startswith("PLATINUM"):
				embed=discord.Embed(title="Статистика", url="https://r6.tracker.network/profile/pc/" + nick_name, description='Матчей сыграно: ' + matсhes_played, color=0x47d7d8)
			if mmr_general_rank.startswith("DIAMOND"):
				embed=discord.Embed(title="Статистика", url="https://r6.tracker.network/profile/pc/" + nick_name, description='Матчей сыграно: ' + matсhes_played, color=0xc1a6f7)
			if mmr_general.startswith("Un"):
				embed=discord.Embed(title="Статистика", url="https://r6.tracker.network/profile/pc/" + nick_name, description='Матчей сыграно: ' + matсhes_played, color=0x272525)
			embed.set_author(name=nick_name, icon_url=avatar)
			embed.set_thumbnail(url=avatar)
			embed.add_field(name="Текущий ранг", value=mmr_general + " , " + mmr_general_rank, inline=False)
			###if mmr_general_rank != " ":
			###	embed.add_field(name="Лучший ранг в текущем сезоне", value=best_mmr + " MMR", inline=False)
			embed.add_field(name="K/D", value=mmr_general_kd, inline=True)
			embed.add_field(name="W/L", value=mmr_general_wl, inline=True)
			embed.add_field(name="Время", value=time_played[0:-1]+" ч.", inline=False)
			embed.add_field(name="Побед", value=wins, inline=True)
			embed.add_field(name="Поражений", value=losses, inline=True)
			embed.add_field(name="Любимые оперативники", value=operator1 + "   " + operator2 + "   " + operator3, inline=False)
			#embed.add_field(name="Level", value=level, inline=True)
			embed.add_field(name="Убийства", value=int(kills*100), inline=False)
			embed.add_field(name="Убийства в голову", value=headshots + " (" + headshots_percent + "%)", inline=False)
			embed.add_field(name="Убийства в рукопашную", value=melee_kills, inline=False)
			embed.add_field(name="Смерти", value=deaths.replace(",",""), inline=False)
			embed.set_footer(text="by deusesone ^_^")
			await ctx.send(embed=embed)

		except TypeError:
			await ctx.send("```css\n Ошибка :(```")
	else:
		if(arg1 == "start"):
			nick_name = arg2
			url_stat = 'https://r6.tracker.network/profile/pc/' + nick_name
			r = requests.get(url_stat)
			with open('stat.html', 'wt', encoding="utf-8") as output_file:
				output_file.write(r.text)
			with open('stat.html', 'r', encoding="utf-8") as f:
				contents = f.read()
			mmr_general = 1
			count_classes = 0
			soup = BeautifulSoup(contents, 'lxml')
			for name_box in soup.find_all('div', {'class': 'trn-text--dimmed'}):
				name = name_box.text.strip()
				count_classes = count_classes + 1
				name = name_box.text.strip()
				if count_classes == 2:
					mmr_general = name
			j = 0
			n = 0
			flag = 0
			for i in list_of_nicknames:
				if i == nick_name:
					j = 1
				if i == nick_name and list_of_nicknames[n+1] != mmr_general:
					flag = n + 1
					j = 1
				n += 1
			if j == 0:
				list_of_nicknames.append(nick_name)
				list_of_nicknames.append(mmr_general)
			if flag != 0:
				list_of_nicknames[flag] = mmr_general
			await ctx.send("```python\n\'" + nick_name + "\', твои данные записаны```")

			print(list_of_nicknames)
		else:
			if(arg1 == "check"):
				try:
					print("checking...")
					nick_name = arg2
					url_stat = 'https://r6.tracker.network/profile/pc/' + nick_name
					r = requests.get(url_stat)
					with open('stat.html', 'wt', encoding="utf-8") as output_file:
						output_file.write(r.text)
					with open('stat.html', 'r', encoding="utf-8") as f:
						contents = f.read()
					mmr_general_new = 1
					count_classes = 0
					soup = BeautifulSoup(contents, 'lxml')
					for name_box in soup.find_all('div', {'class': 'trn-text--dimmed'}):
						name = name_box.text.strip()
						count_classes = count_classes + 1
						name = name_box.text.strip()
						if count_classes == 2:
							mmr_general_new = name
					mmr_general_int_new = []
					dekitek = 1000
					number_new = 0
					for i in mmr_general_new:
						try:
							num = int(i)
							mmr_general_int_new.append(num)
						except ValueError:
							continue
					for i in mmr_general_int_new:
						number_new = number_new + i * dekitek
						dekitek /= 10

					j = 0
					mmr_general_old = 0
					for i in list_of_nicknames:
						if i == nick_name:
							mmr_general_old = list_of_nicknames[j+1]
						j += 1
					mmr_general_int_old = []
					for i in mmr_general_old:
						try:
							num = int(i)
							mmr_general_int_old.append(num)
						except ValueError:
							continue
					number_old = 0
					dekitek = 1000
					for i in mmr_general_int_old:
						number_old = number_old + i * dekitek
						dekitek /= 10
					print(int(number_old))
					print(int(number_new))
					number_change = 0
					if (int(number_old) > int(number_new)):
						number_change = number_old - number_new
						await ctx.send("```python\n\'" + nick_name + "\': MMR уменьшился на "  + str(number_change) + "```")
					if (int(number_old) < int(number_new)):
						number_change = number_new - number_old
						await ctx.send("```python\n\'" + nick_name + "\': MMR увеличился на " + str(number_change) + "```")
					if (int(number_old) == int(number_new)):
						await ctx.send("```python\n\'" + nick_name + "\': MMR не изменился" + "```")
				except Exception:
					await ctx.send('```css\n Ошибка :( ```')
			else:
				await ctx.send("```css\n Ошибка :(```")


players = {}

@client.command(pass_context=True)
async def join(ctx):
	channel = ctx.message.author.voice.channel
	if not channel:
		await ctx.send("You are not connected to a voice channel")
		return
	voice = get(client.voice_clients, guild=ctx.guild)
	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()



@client.command()
async def search(ctx, *, search):
	video_names.clear()
	video_ids.clear()
	yt = yt_search.build(config.yt_key)
	len_noNone = 0
	try:
		search_result = yt.search(search, sMax=25, sType=["video"])
		i = 0
		for indexes in search_result.title:
			if search_result.videoId[i] != None:
				if len_noNone < 20:
					len_noNone+=1
					video_names.append(search_result.title[i])
					video_ids.append(search_result.videoId[i])
			i+=1
		embed=discord.Embed(description="Результаты поиска:")
		j = 0
		len_video_names = len(video_names)
		for j in range(len_video_names):
			embed.add_field(name=str(j+1), value=video_names[j], inline=False)
		embed.set_footer(text="by deusesone ^_^")
		await ctx.send(embed=embed)
	except Exception as e:
		print(e)
		await ctx.send('```css\n Ошибка :( ```')



@client.command(pass_context=True)
async def play(ctx, *, request):
	try:
		if int(request) > 0 and int(request) < len(video_names) + 1:
			i = 0
			for i in range(len(video_names)):
				if int(request) - 1 == i:
					url = video_ids[i]
			YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
			FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
			voice = get(client.voice_clients, guild=ctx.guild)
			if not voice.is_playing():
				with YoutubeDL(YDL_OPTIONS) as ydl:
					info = ydl.extract_info(url, download=False)
					video_title = info.get('title')
					icon = info.get('thumbnail')
					URL = info['formats'][0]['url']
					voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
					voice.is_playing()
				embed=discord.Embed(title=video_title, url = "https://www.youtube.com/watch?v=" + url, description=f"Предложено {ctx.author}")
				embed.set_thumbnail(url=icon)
				embed.set_author(name="Сейчас играет:")
				embed.set_footer(text="by deusesone ^_^")
				await ctx.send(embed=embed)
			else:
				await ctx.send("Already playing song")
				return
		else:
			await ctx.send('```css\n Ошибка :( ```')
	except Exception:
		if request.startswith("https://www.youtube.com/watch?v="):
			url = request
			YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
			FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
			voice = get(client.voice_clients, guild=ctx.guild)
			if not voice.is_playing():
				with YoutubeDL(YDL_OPTIONS) as ydl:
					info = ydl.extract_info(url, download=False)
					video_title = info.get('title')
					icon = info.get('thumbnail')
					URL = info['formats'][0]['url']
					voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
					voice.is_playing()
				embed=discord.Embed(title=video_title, url = url, description=f"Предложено {ctx.author}")
				embed.set_thumbnail(url=icon)
				embed.set_author(name="Сейчас играет:")
				embed.set_footer(text="by deusesone ^_^")
				await ctx.send(embed=embed)
			else:
				await ctx.send("Already playing song")
				return
		else:
			yt = yt_search.build(config.yt_key)
			try:
				play_by_name = yt.search(request, sMax=10, sType=["video"])
				i = 0
				for indexes in play_by_name.title:
					if play_by_name.videoId[i] != None:
						list_play_by_name.append(play_by_name.videoId[i])
					i+=1
				url = list_play_by_name[0]
				YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
				FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
				voice = get(client.voice_clients, guild=ctx.guild)
				if not voice.is_playing():
					with YoutubeDL(YDL_OPTIONS) as ydl:
						info = ydl.extract_info(url, download=False)
						video_title = info.get('title')
						icon = info.get('thumbnail')
						URL = info['formats'][0]['url']
						voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
						voice.is_playing()
					embed=discord.Embed(title=video_title, url = "https://www.youtube.com/watch?v=" + url, description=f"Предложено {ctx.author}")
					embed.set_thumbnail(url=icon)
					embed.set_author(name="Сейчас играет:")
					embed.set_footer(text="by deusesone ^_^")
					await ctx.send(embed=embed)
				else:
					await ctx.send("Already playing song")
					return
			except Exception as e:
				print(e)
				await ctx.send('```css\n Ошибка :( ```')



@client.command(pass_context=True)
async def pause(ctx):
	voice = get(client.voice_clients, guild=ctx.guild)
	voice.pause()



@client.command(pass_context=True)
async def stop(ctx):
	voice = get(client.voice_clients, guild=ctx.guild)
	voice.stop()



@client.command(pass_context=True)
async def resume(ctx):
	voice = get(client.voice_clients, guild=ctx.guild)
	voice.resume()



@client.command(pass_context=True)
async def leave(ctx):
	await ctx.voice_client.disconnect()



#ожидание ивента
@client.event
async def on_message(message):

    if message.author == client.user:
        return


    if "Настя.кинь трапа" in message.content:
        await message.channel.send(file=discord.File("/home/deusesone/bot/trap/" + random.choice(os.listdir("trap/"))))

#простой ответ на оскорбление
    if 'аст' in message.content and 'шлюха' in message.content:
    	await message.channel.send('ты ебать спермобак я твой рот ебала')



#приветствие
    if 'Настя.привет' in message.content:
        await message.channel.send('Прив всем в этом чатике :3', tts = True)
        await message.channel.send('Чтобы посмотреть, что я умею, напишите ```fix\nНастя.команды```')



#список функций
    if message.content.startswith('Настя.команды'):
    	await message.channel.send('```python\n>>> Список команд:\n[1] Настя.музыка\n[2] Настя.анекдот\n[3] Настя.курс валюты\n[4] Настя.коронавирус\n[5] Настя.погода <Город> (на английском языке)\n[6] Настя.радуга\n[7] Настя.перевод <выражение на русском или английском> ```')



#отправка рандомной фотки трапа из папки
    if 'Настя.музыка' in message.content:
    	await message.channel.send("```python\n>>> О команде Настя.музыка \n[1] !join - пригласить в голосовой канал \n[2] !play <ссылка видео youtube> -  включить трек \n[3] !pause  -  пауза \n[4] !resume - продолжить \n[5] !stop - остановить \n[6] !leave - отсоединить```")



#отправка сисек дарины из трапа
    if 'Настя.сиськи дарины' in message.content:
    	image = random.choice(os.listdir("darina/"))
    	await message.channel.send(file=discord.File("darina/" + image))



#ответ на спасибо
    if message.content.startswith('спасибо') or message.content.startswith('Cпасибо'):#исправить для большего кол-ва реакций
    	await message.channel.send('^_^')



#да -> пизда
    if (message.content == 'да' or message.content == 'Да'):
    	await message.channel.send('пизда')



#отправка анекдота с сайта anektod-z.ru
    if 'Настя.анекдот' in message.content:
    	url = 'https://anekdot-z.ru/index?sort_by=RAND()'
    	r = requests.get(url)
    	with open('test.html', 'wt', encoding="utf-8") as output_file:
    		output_file.write(r.text)
    	with open('test.html', 'r', encoding="utf-8") as f:
    		contents = f.read()
    		soup = BeautifulSoup(contents, 'lxml')
    		items = soup.find_all('div', {'class': 'anekdot-content'})
    		for item in items:
    			joke = soup.find('div', {'class': 'anekdot-content'}).text
    			await message.channel.send('```' + joke + '```')
    			break
    	os.remove("test.html")


    if message.content == "Настя.радуга":
    	await message.channel.send("```python\n>>> О команде Настя.радуга \n[1] !r6 stats <никнейм> - подробности об игроке \n[2] !r6 start <никнейм> - отсчет ммр с текущего момента \n[3] !r6 check <никнейм> - подсчет проебанного ммр```")



#показывает статистику коронавируса
    if 'Настя.коронавирус' in message.content:
    	url_covid = 'https://стопкоронавирус.рф'
    	r = requests.get(url_covid)
    	with open('covid.html', 'wt', encoding="utf-8") as output_file:
    		output_file.write(r.text)
    	with open('covid.html', 'r', encoding="utf-8") as f:
    		contents = f.read()
    		covid_general = '-'
    		covid_death = '-'
    		covid_last_day = '-'
    		covid_recovered = '-'
    		covid_tests = '-'
    		soup = BeautifulSoup(contents, 'lxml')
    		count_classes = 0
    		#поиск по всем классам веб страницы с указанным именем
    		for name_box in soup.find_all('div', {'class': 'cv-countdown__item-value'}):
    			name = name_box.text.strip()
    			count_classes = count_classes + 1
    			if count_classes == 1:
    				covid_tests = name
    			if count_classes == 2:
    				covid_general = name
    			if count_classes == 3:
    				covid_last_day = name
    			if count_classes == 4:
    				covid_recovered = name
    			if count_classes == 5:
    				covid_death = name

    		for actual in soup.find_all('div', {'class': 'cv-banner__description'}):
    			name_actual = actual.text.strip()

    		embed=discord.Embed(title="стопкоронавирус.рф", url="https://стопкоронавирус.рф", description=name_actual, color=0x387580)
    		embed.set_author(name="Оперативные данные")
    		embed.set_thumbnail(url="https://dalee.cdnvideo.ru/stopcoronavirus.rf/img/logo.svg")
    		embed.add_field(name="Проведено тестов", value=covid_tests, inline=False)
    		embed.add_field(name="Общее число случаев", value=covid_general, inline=False)
    		embed.add_field(name="Человек умерло", value=covid_death, inline=False)
    		embed.add_field(name="Человек выздоровело", value=covid_recovered, inline=False)
    		embed.add_field(name="Случая заболевания за последние сутки", value=covid_last_day, inline=False)
    		await message.channel.send(embed=embed)
    		#await message.channel.send("```css\n[" + name_actual + "]\nПроведено тестов " + covid_tests + "\nОбщее число случаев - " + covid_general + "\nЧеловек умерло - " + covid_death + "\nЧеловек выздоровело - " + covid_recovered + "\nСлучая заболевания за последние сутки - " + covid_last_day +'```')
    	os.remove("covid.html")


#отправка погоды в зависимости от указанного в сообщении города
    if message.content.startswith("Настя.погода"):
    	number_of_letters = 0
    	space = False
    	for letter in message.content:
    		number_of_letters = number_of_letters + 1
    	city_name = message.content[12:number_of_letters]
    	try:
    		res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city_name, 'units': 'metric', 'lang': 'ru', 'APPID': config.appid})
    		data = res.json()
    		weather_temperature = data['main']['temp']
    		weather_conditions = data['weather'][0]['description']
    		weather_wind = data['wind']['speed']
    		city_id = data['name']
    		weather_sum = str(city_id) + ": " + str(weather_temperature) + "°C" + ", " + str(weather_conditions) + ", ветер: " + str(weather_wind) + " м/с"
    		await message.channel.send('```' + weather_sum + '```')
    	except Exception:
    		await message.channel.send('```css\n Ошибка :( ```')



    #отправка курса валюты
    if 'Настя.курс валюты' in message.content:
    	res_usd = requests.get("https://api.exchangeratesapi.io/latest?base=USD")
    	data_usd = res_usd.json()
    	dollar = data_usd['rates']['RUB']
    	print(dollar)
    	res_eur = requests.get("https://api.exchangeratesapi.io/latest?base=EUR")
    	data_eur = res_eur.json()
    	euro = data_eur['rates']['RUB']
    	res_bitc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    	data_bitc = res_bitc.json()
    	bitc_to_usd = data_bitc['bpi']['USD']['rate_float']
    	bitc_to_rub = int(bitc_to_usd) * int(dollar)
    	print(dollar)
    	print(euro)
    	print(bitc_to_rub)
    	await message.channel.send('```python\nКурс евро - ' + str(euro) + " Российский рубль" + '\nКурс доллара - ' + str(dollar) + " Российский рубль" + '\nКурс биткоина - ' + str(bitc_to_rub) + " Российский рубль" +'```')



    if message.content.startswith("Настя.перевод"):
    	word = message.content[14:len(message.content)]
    	if re.search(r'[A-Za-z]', word):
    		lang = 'en-ru'
    	else:
    		lang = 'ru-en'
    	url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    	key = 'trnsl.1.1.20200504T134707Z.8fb25d75dfc780fd.a9c32b6ee59a580b7e042d13884e348fe0b95783'
    	text = word
    	res = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
    	data = res.json()
    	translate = data['text']
    	if lang == 'en-ru':
    		await message.channel.send("```" + "English: " + str(word) + "\nРусский: " + str(data['text']) + "```")
    	else:
    		await message.channel.send("```" + "Русский: " + str(word) + "\nEnglish: " + str(data['text']) + "```")

    await client.process_commands(message)


client.run(config.TOKEN)
