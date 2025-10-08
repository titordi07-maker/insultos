from flask import Flask
from threading import Thread
import discord
import random
import os

# Health check para Render (OBLIGATORIO)
app = Flask('')

@app.route('/')
def home():
    return "🤖 Bot Discord funcionando 24/7!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

# Iniciar health check
keep_alive()

# Configuración del bot de Discord
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# LISTA DE INSULTOS
INSULTOS = [
    "Eres mas inutil que un condon en un convento",
    "Tienes menos futuro que un sordo en un concurso de beatbox",
    "Eres mas falso que el orgasmo de una prostituta",
    "Tienes mas cara que un bombero con hipo",
    "Eres mas pesado que una vaca en brazos",
    "Tienes menos luces que la furgoneta del Equipo A",
    "Eres mas soso que un gazpacho sin sal",
    "Tienes mas peligro que un mechero en una gasolinera",
    "Eres mas lento que un funeral en cuesta",
    "Tienes menos gracia que una monja en un puticlub",
    "Eres mas basto que un culo con botas",
    "Tienes mas mala leche que una vaca con colicos",
    "Eres mas feo que pegarle a un padre",
    "Tienes mas morro que un huron con paperas",
    "Eres mas pesado que los impuestos",
    "Tienes menos arreglo que un ordenador en una banera",
    "Eres mas corto que las mangas de un chaleco",
    "Tienes mas mala uva que un vinedo con hongos",
    "Eres mas predecible que el final de un porno",
    "Tienes menos futuro que un caracol en una carrera de F1",
    "Eres mas patetico que un mimo ahogandose",
    "Tienes mas cara que un politico corrupto",
    "Eres mas simple que un chiste de Lepe",
    "Tienes menos sentido del humor que un cementerio",
    "Eres mas pesado que la factura de la luz",
    "Eres mas inutil que un submarino con puertas",
    "Tienes mas mala pata que un perro en una pista de baile",
    "Eres mas triste que un payaso en un tanatorio",
    "Tienes menos salida que un callejon sin salida",
    "Eres mas cansino que un mosquito en la oreja"
    "Tus muertos"
    "Eres tan ingenioso que cada vez que hablas, el universo hace una pausa para preguntarse cómo llegaste tan lejos sin un manual de instrucciones para existir"
    "Tu presencia es como una obra maestra del caos: un desastre tan perfecto que hasta los huracanes te piden consejos de destrucción"
    "No digo que seas un inútil, pero si la mediocridad tuviera un rey, tú estarías ocupado puliendo el trono con tu talento para lo absurdo"
    "Eres la prueba de que Dios a veces juega a los dados y tira un cero crítico, creando un glitch humano con patas"
    "Si el fracaso fuera una moneda, tú serías la Casa de la Moneda trabajando horas extras para acuñar tu legado"
]

]

# LISTA DE CHISTES NEGROS
CHISTES = [
    "Que le dice un negro a otro negro en la piscina? - Cuidado, no te vayas a oxidar!",
    "Por que los negros no usan condon? - Porque no quieren perder el 10% de placer",
    "Como se llama un negro que vuela un avion? - Piloto, que coño iba a ser!",
    "Que hace un negro en un club de jazz? - Lo mismo que tu en la carcel: nada",
    "Van dos negros por la calle y uno le dice al otro: Oye, has visto mi camiseta? Y el otro: Cual?",
    "Por que los negros no juegan al escondite? - Porque nadie los busca",
    "Que hace un negro en Harvard? - Lo mismo que en cualquier sitio: limpiar",
    "Como sabes que tu novia es negra? - Cuando le dices 'te quiero' y te contesta 'yo tambien, jefe'",
    "Por que los negros no pueden ser bombero? - Porque no saben subir la escalera sin que suene musica",
    "Que es lo primero que hace un negro cuando se levanta? - Volver a la carcel",
    "Como haces que un negro se suicide? - Le pegas una pegatina en la suela del zapato que diga 'quitame'",
    "Por que los negros tienen la nariz tan plana? - De tanto dar portazos cuando la policia los persigue",
    "Que hace un negro con MBA? - Preguntar si quieres menu o a la carta",
    "Cual es el colmo de un negro? - Tener SIDA y cancer a la vez",
    "Por que los negros no usan reloj? - Porque ya saben la hora a la que anochece",
    "Que le dice un negro a una prostituta? - Aceptas cupones de descuento?",
    "Como se llama un negro en la NASA? - Perdido",
    "Por que los negros no pueden ser arbitros? - Porque se comen el silbato",
    "Que hace un negro en la universidad? - Limpiar las aulas",
    "Cual es el plato favorito de los negros? - Lo que sea que estes comiendo tu"
    "Por qué la torre de Pisa está inclinada?- Porque tiene más reflejos q las torres gemelas"
    "Iba a contar un chiste tan negro, tan negro, que se lo llevo la policía"
    "Por qué una niña con tetraplegia no puede jugar al fútbol?- Porque es mujer"
]

@client.event
async def on_ready():
    print('🔥 ¡BOT CONECTADO 24/7!')
    print('🤖 Usa @bot o !chiste en Discord')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user in message.mentions:
        insulto = random.choice(INSULTOS)
        await message.reply(f"{message.author.mention} {insulto} 😈")
    
    if message.content.startswith('!chiste'):
        chiste = random.choice(CHISTES)
        await message.channel.send(f"**🎭 Chiste Negro:** {chiste}")
        
    if message.content.startswith('!insulto'):
        insulto = random.choice(INSULTOS)
        await message.channel.send(f"{message.author.mention} {insulto} 💥")

# Ejecutar el bot
token = os.getenv('DISCORD_TOKEN')
if token:
    client.run(token)
else:

    print("❌ ERROR: No se encontro el token")
