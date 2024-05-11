import telebot
from telebot import types 
# Ekstra kütüphaneleri yükleyin
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os

# Telegram Bot'unuzu oluşturun
bot = telebot.TeleBot("6769905904:AAHVvXUpdKsfGr5CwbOlIaqiGkFsVqWip2Q")
# Ülkeler için fotoğraf dosya yollarını belirtin
turkeygeorgia_photo_link = "https://i.imgur.com/v5UyXJk.jpg"
turkey_photo_link = "https://f.invest.gov.tr/en/PublishingImages/WHY-TURKEY_375x500.jpg"
georgia_photo_link = "https://turuncudergi.com/wp-content/uploads/2022/12/image-18.jpeg"
wcm_photo_link = "https://d14d5nk8lue86f.cloudfront.net/s3fs-public/2022-10/From%20Cannabis%20to%20Opioids%2C%20Meth%2C%20and%20Cocaine%20Drugs%20Are%20Linked%20to%20More%20AF.jpg"
product_photo_link = {
    "Weed": "https://www.verywellmind.com/thmb/m2VVBXgqiFcrWXrqwdvBmpRXDZ4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/marijuana-454601963-resized-569fd2345f9b58eba4ad583d.jpg",
    "Cocaine": "https://www.medinat.com.au/media/Drugs_Cocaine_powder_and_lines.jpg",
    "Meth": "https://www.banyantreatmentcenter.com/wp-content/uploads/2021/07/meth-myths-and-facts.gif"
}
new_users = set()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id not in new_users:
        # Kullanıcı daha önce botla etkileşime girmediyse hoş geldin mesajını gönder
        bot.reply_to(message, "🇺🇸 For proof, you can see the orders and satisfaction of our customers by joining our Telegram channel. You can join our channel from the link below: 👇" + "\n" +  

"https://t.me/weedshopoo420                            " + 

"🇹🇷 Kanıt için , müşterilerimizin eline geçen siparişleri, memnuniyetini Telegram kanalımıza katılarak göre bilirsiniz. Kanalımıza aşağıdaki linkten katıla bilirsiniz: 👇" + "\n" +

"https://t.me/weedshopoo420                            "+

"🇷🇺 В качестве доказательства вы можете увидеть заказы и удовлетворенность наших клиентов, присоединившись к нашему каналу Telegram. Вы можете присоединиться к нашему каналу по ссылке ниже: 👇" + "\n" +

"https://t.me/weedshopoo420" )
        # Kullanıcıyı yeni kullanıcılar setine ekleyin
    else:
        bot.reply_to(message, "🇺🇸 For proof, you can see the orders and satisfaction of our customers by joining our Telegram channel. You can join our channel from the link below: 👇" + "\n" +  

"https://t.me/weedshopoo420                            " + 

"🇹🇷 Kanıt için , müşterilerimizin eline geçen siparişleri, memnuniyetini Telegram kanalımıza katılarak göre bilirsiniz. Kanalımıza aşağıdaki linkten katıla bilirsiniz: 👇" + "\n" +

"https://t.me/weedshopoo420                            "+

"🇷🇺 В качестве доказательства вы можете увидеть заказы и удовлетворенность наших клиентов, присоединившись к нашему каналу Telegram. Вы можете присоединиться к нашему каналу по ссылке ниже: 👇" + "\n" +

"https://t.me/weedshopoo420")
        new_users.add(message.from_user.id)
    bot.send_photo(message.chat.id, turkeygeorgia_photo_link, caption="")
    # Butonları içeren klavyeyi oluşturun
    keyboard = types.InlineKeyboardMarkup()
    # İstediğiniz kadar buton ekleyebilirsiniz
    button1 = types.InlineKeyboardButton(text="Turkey \U0001F1F9\U0001F1F7", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Georgia \U0001F1EC\U0001F1EA", callback_data="button2")
    # Butonları klavyeye ekleyin
    keyboard.add(button1, button2)
    # Mesajı gönderin
    bot.send_message(message.chat.id, "Choose Your Country:", reply_markup=keyboard)

# İçeceklerin fiyatlarını tutan bir sözlük oluşturun
drink_prices = {
    "Weed": {"1gr": 35, "3gr": 75, "5gr": 120, "10gr": 230,"20gr":430},
    "Cocaine": {"1gr": 150, "3gr": 380, "5gr": 550},
    "Meth": {"1gr": 65, "3gr": 150, "5gr": 380}
}

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "button1":
        bot.send_photo(call.message.chat.id, turkey_photo_link, caption="Welcome to Turkey!")
        # Şehir butonlarını gönderin
        keyboard = types.InlineKeyboardMarkup()
        new_button1 = types.InlineKeyboardButton(text="Izmir", callback_data="city_Izmir")
        new_button2 = types.InlineKeyboardButton(text="Antalya", callback_data="city_Antalya")
        new_button3 = types.InlineKeyboardButton(text="Alanya", callback_data="city_Alanya")
        new_button4 = types.InlineKeyboardButton(text="Istanbul", callback_data="city_Istanbul")
        new_button5 = types.InlineKeyboardButton(text="Mugla", callback_data="city_Mugla")
        keyboard.add(new_button1)
        keyboard.add(new_button2)
        keyboard.add(new_button3)
        keyboard.add(new_button4)
        keyboard.add(new_button5)
        bot.send_message(call.message.chat.id, "Choose Your City", reply_markup=keyboard)
    elif call.data == "button2":
        bot.send_photo(call.message.chat.id, georgia_photo_link, caption="Welcome to Georgia!")
        # Button 2'e tıklandığında yeni bir buton ekleyin
        keyboard = types.InlineKeyboardMarkup()
        new_button6 = types.InlineKeyboardButton(text="Batum", callback_data="city_Batum")
        new_button7 = types.InlineKeyboardButton(text="Tblisi", callback_data="city_Tblisi")
        new_button8 = types.InlineKeyboardButton(text="Telavi", callback_data="city_Telavi")
        new_button9 = types.InlineKeyboardButton(text="Kutaisi", callback_data="city_Kutaisi")
        new_button10 = types.InlineKeyboardButton(text="Rustavi", callback_data="city_Rustavi")
        keyboard.add(new_button6)
        keyboard.add(new_button7)
        keyboard.add(new_button8)
        keyboard.add(new_button9)
        keyboard.add(new_button10)
        bot.send_message(call.message.chat.id, "Choose Your City", reply_markup=keyboard)
    elif call.data.startswith("city_"):

        city = call.data.split("_")[1]
        bot.send_photo(call.message.chat.id, wcm_photo_link, caption="")
        # Seçilen şehir için içecek butonlarını gönderin
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Weed", callback_data=f"{city}_Weed")
        button2 = types.InlineKeyboardButton(text="Cocaine", callback_data=f"{city}_Cocaine")
        button3 = types.InlineKeyboardButton(text="Meth", callback_data=f"{city}_Meth")
        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)
        bot.send_message(call.message.chat.id, f"Choose your drugs in {city}:", reply_markup=keyboard)
    elif call.data.endswith("_Weed") or call.data.endswith("_Cocaine") or call.data.endswith("_Meth"):
        product = call.data.split("_")[1]
        product_photo_path = product_photo_link.get(product)
        if product_photo_path:
                bot.send_photo(call.message.chat.id, product_photo_path, caption="")

        drugs = call.data.split("_")[1]
        # İçecek seçildikten sonra litre seçeneklerini gösterin
        keyboard = types.InlineKeyboardMarkup()
        prices = drink_prices[drugs]  # İçecek için fiyatları alın
        for size, price in prices.items():
            button = types.InlineKeyboardButton(text=f"{size} - ${price}", callback_data=f"{drugs}_{size}")
            keyboard.add(button)
        bot.send_message(call.message.chat.id, f"Choose the size for your {drugs}:", reply_markup=keyboard)
    # Diğer kod blokları da benzer şekilde devam eder...
    elif call.data.endswith("_1gr") or call.data.endswith("_3gr") or call.data.endswith("_5gr") or call.data.endswith("_10gr") or call.data.endswith("_20gr"):
        payment_method = call.data.split("_")[1]
    # Ödeme yöntemi seçildikten sonra fotoğraf gönderin
        payment_photo_link = "https://www.1kosmos.com/wp-content/uploads/2018/07/Bitcoin-vs-Ethereum-vs-Litecoin.jpg"  # Ödeme yöntemi fotoğrafı yolunu belirtin
        bot.send_photo(call.message.chat.id, payment_photo_link, caption="")
        size = call.data.split("_")[1]
        # Litre seçildikten sonra ödeme yöntemi seçeneklerini gösterin
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Usdt trc20", callback_data=f"{size}_Usdt trc20")
        button2 = types.InlineKeyboardButton(text="Bitcoin btc", callback_data=f"{size}_Bitcoin btc")
        button3 = types.InlineKeyboardButton(text="Litecoin LTC", callback_data=f"{size}_Litecoin LTC")
        button4 = types.InlineKeyboardButton(text="Ethereum  ETH", callback_data=f"{size}_Ethereum  ETH")
        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)
        keyboard.add(button4)
        bot.send_message(call.message.chat.id, f"Choose your payment method for {size}:", reply_markup=keyboard)
    elif call.data.endswith("_Litecoin LTC") or call.data.endswith("_Usdt trc20") or call.data.endswith("_Bitcoin btc") or call.data.endswith("_Ethereum  ETH"):
        payment_method = call.data.split("_")[1]
    # Ödeme yöntemine bağlı olarak fotoğraf gönder
        if payment_method == "Usdt trc20":
            payment_photo_path = "https://i.imgur.com/zm2e6zO.jpg" 
            caption_text = "TPj9p1DhbNA7KMX7xVUmHzmNAEoSLDhvin" 
        elif payment_method == "Bitcoin btc":
            payment_photo_path = "https://i.imgur.com/L5jyUDb.jpg"
            caption_text = "bc1qf3stn5et7kc8mmqc5a9k5ce007q94pfxa5pxsu"
        elif payment_method == "Litecoin LTC":
            payment_photo_path = "https://i.imgur.com/QfcFBcT.jpg"
            caption_text = "ltc1qqtjw75ysjlp9shs2gev6mtpxpgwy6ysfyjq47t"
        elif payment_method == "Ethereum  ETH":
            payment_photo_path = "https://i.imgur.com/8Wz281X.jpg"
            caption_text = "0x952e590A14FF263d93bBC6C2a919bAc5d0E62618"

    # Canlı destek butonunu oluşturun
        live_support_button = types.InlineKeyboardButton("ADMIN", url="https://t.me/weedshopadminn")
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(live_support_button)


        bot.send_photo(call.message.chat.id, payment_photo_path, caption=caption_text, reply_markup=keyboard)

bot.polling()
