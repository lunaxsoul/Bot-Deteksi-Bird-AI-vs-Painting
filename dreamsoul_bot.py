import discord
from discord.ext import commands
import requests
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

intents = discord.Intents.default()
intents.message_content = True

quote = "“If you can dream it, you can do it.” ―Walt Disney."

bot = commands.Bot(command_prefix='$', intents=intents)

def pendeteksi(path_image):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_Model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(path_image).convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)

    return class_name[2:]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'''
    Hi! I am a bot {bot.user}!👋
    
    What can I do for you?
    ''')

@bot.command()
async def how(ctx):
    await ctx.send(f'''
These are things you can do with me👇:
1. For motivation ($motivation)
2. For tounge twister ($toungetwister)
3. For earth & nature lovers ($for_earth_lovers)     

check it out!!🙌🙌😃

    -{bot.user}          
    ''')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def thanks(ctx):
    await ctx.send(f'you are welcome!')

@bot.command()
async def motivation(ctx):
    await ctx.send(f"A motivation for you: {quote}")

@bot.command()
async def toungetwister(ctx):
    await ctx.send(f"she sells shell by the seashores")

@bot.command()
async def how_are_you(ctx):
    await ctx.send(f"I'm good")

@bot.command()
async def bye(ctx):
    await ctx.send(f"bye!!👋 thank you for using {bot.user}😃🙌! Have a nice day!")

@bot.command()
async def for_earth_lovers(ctx):
    await ctx.send(f'''
Hola!!👋
To All Earth lovers in INDONESIA❤️🤍🌱
Ini adalah beberapa informasi terkait misi "Save & love our Earth"💖👇:
1. $fakta_polusi_INA
2. $apa_itu_praktik_ramah_lingkungan
3. $contoh_praktik_ramah_lingkungan
4. $cara_mengolah_limbah
5. $bye
                   
Copy and paste these commands to find out of what information it contains!
-Gwaenchanha.bot🌙                   
                   ''')
    
@bot.command()
async def fakta_polusi_INA(ctx):
    await ctx.send(f'''
Halo ❤️ INDONESIAN 🤍
🌱Earth lovers!👋
Berdasarkan laporan terbaru Kualitas Udara Dunia IQAir 2021 yang dirilis pada Maret 2022 
Indonesia menduduki peringkat ke-17 sebagai negara dengan tingkat polusi udara tertinggi di dunia,
dengan konsentrasi PM2,5 mencapai 34,3 μg per meter kubik. 
Penyebab terjadinya polusi ini adalah bentuk gas, cair, dan padat tertentu yang terpendam di udara. 
Partikel tersebut dapat berasal dari aerosol, debu, asap pabrik, kebakaran hutan, asap kendaraan bermotor, dan asap. 
Pada tahun 2022 lalu itu ada 24,5 juta penggunaan kendaraan bermotor
                   
Tentunya kondisi ini sangat memprihatinkan bukan? 😶‍🌫️😶‍🌫️
maka dari itu Earth lovers harus mengetahui cara menyelamatkan bumi kita!!
-Gwaenchanha.bot🌙                   
                   ''')
    
@bot.command()
async def apa_itu_praktik_ramah_lingkungan(ctx):
    await ctx.send(f'''
Subject : Pengenalan Praktik Ramah Lingkungan 🌱🌏
🌱Earth lovers 
Banyaknya tindakan yang bisa merusak ekosistem membuat setiap orang perlu memahami betapa pentingnya perilaku ramah lingkungan.
Salah satu cara untuk mengurangi polusi adalah dengan menerapkan praktik ramah lingkungan.

Apa itu praktik ramah lingkungan?🤷‍♂️🤷‍♀️
Check this out!👇

Ramah lingkungan 
adalah sesuatu yang bekelanjutan dan tidak membahayakan lingkungan atau ekosistem.

Hidup ramah lingkungan/Sustainable living 
adalah gaya hidup yang mencoba untuk mengurangi penggunaan sumber daya alam 
dan harta pribadi yang dilakukan oleh pribadi maupun masyarakat.

-Gwaenchanha.bot🌙                   
                   ''')

@bot.command()
async def contoh_praktik_ramah_lingkungan(ctx):
    await ctx.send(f'''
Subject : Contoh Praktik Ramah Lingkungan 🌱🌏
🌱Earth lovers 
Berikut adalah contoh praktik ramah lingkungan yang dapat kita lakukan😊👇🤍:
1️⃣Membuang sampah pada tempatnya dan bukan sembarangan
2️⃣Tidak membuang sampah atau benda tidak terpakai ke sungai yang bisa menghambat aliran air
3️⃣Membawa tas belanja sendiri yang terbuat dari kain sebagai pengganti kantong plastik
4️⃣Tidak menggunakan sedotan plastik saat minum
5️⃣Tidak membuang baterai sembarangan karena bahan kimia yang dikandungnya bisa mencemari air dan tanah

Itu hanyalah beberapa cara yang dapat kita lakukan! Masih banyak cara lain yang dapat kita lakukan lho!
Save our Earth!🌏🌱 Save our life!!😃🙌
                   
-Gwaenchanha.bot🌙                   
                   ''')
    
@bot.command()
async def cara_mengolah_limbah(ctx):
    await ctx.send(f'''
Subject : Cara Mengolah Limbah🙌🙌
🌱Earth lovers 
Salah satu cara yang paling efektif dalam pengolahan limbah adalah 4R, yakni reduce, reuse, recycle dan replace.

1️⃣ Reduce 
mengurangi penggunaan barang.
CONTOH : mengganti penggunaan kantong plastik sekali pakai menjadi kantong belanja ramah lingkungan.  
                                  
2️⃣ Reuse
menggunakan barang-barang yang masih bisa dipakai kembali.
CONTOH: ketika kita memiliki botol minum dengan label segitiga. Sebaiknya kita tidak langsung membuang botol minum tersebut.
        Hal ini karena kita masih menggunakannya kembali, setidaknya dalam pemakaian tiga kali maksimalnya.
                   
3️⃣ Recycle
melakukan daur ulang barang yang sudah tidak berguna menjadi barang yang lebih bermanfaat kembali.
CONTOH : Membuat karya seni daur ulang dari sampah                    

4️⃣ Replace
melakukan daur ulang barang yang sudah tidak berguna menjadi barang yang lebih bermanfaat kembali.
CONTOH : beralih menggunakan kendaraan pribadi dengan menggunakan sepeda atau kendaraan umum
         dan mengganti Styrofoam dengan daun pisang untuk membungkus makanan.

That's it Earth Lovers!❤️🌏
Adios!👋👋
                                  
-Gwaenchanha.bot🌙                   
                   ''')

@bot.command()
async def mem(ctx):
    with open('M2L1_605/meme.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def animals(ctx):
    with open('M2L1_605/memecapybara.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def klasifikasi(ctx):
    data = ctx.message.attachments
    #print(list(data)[-1])

    # kode untuk AI
    print("hasilnya adalah")
    response = requests.get(list(data)[-1])
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    result = pendeteksi("image.jpg")

    await ctx.send(result)
bot.run("MASUKKAN TOKEN BOT")