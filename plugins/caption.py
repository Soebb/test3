from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    media = message.video or message.document
    if (media is not None) and (media.file_name is not None):
        m = media.file_name.replace("Fragmanı", "").replace("Fragmanlarım", "").replace("ı", "i").replace("İ", "I").replace("ö", "o").replace("Ö", "O").replace("Ü", "U").replace("ü", "u").replace("ë", "e").replace("Ë", "E").replace("Ä", "A").replace("ç", "c").replace("Ç", "C").replace("ş", "s").replace("Ş", "S").replace("ğ", "g").replace("Ğ", "G").replace("ä", "a")
        D = m.replace("720P", "").replace("E20", "").replace("E120", "").replace("E220", "").replace("E320", "").replace("E420", "")
        N = m.replace("@dlmacvin2 -", "").replace("@dlmacvin -", "")
        Z = media.file_name
        fa = " "
        X = " "
        tz = " "
        Lo = " "
        if "Sen Cal Kapimi" in m:
            fa += "#تو_در_خانه_ام_را_بزن"
            X += "Sen Cal Kapimi"
            Kh = m.replace("Sen Cal Kapimi", "")
        if "Marasli" in m:
            fa += "#اهل_ماراش"
            X += "Marasli"
        if "Kalp Yarasi" in m:
            fa += "#زخم_قلب"
            X += "Kalp Yarasi"
        if "Dunya Hali" in m:
            fa += "#احوال_دنیایی"
            X += "Dunya Hali"
        if "Ver Elini Ask" in m:
            fa += "#دستت_را_بده_عشق"
            X += "Ver Elini Ask"
        if "Ezel" in m:
            fa += "#ایزل"
            X += "Ezel"
        if "Ikimizin Sirri" in m:
            fa += "#راز_ما_دو_نفر"
            X += "Ikimizin Sirri"
        if "Dirilis Ertugrul" in m:
            fa += "#قیام_ارطغرل"
            X += "Dirilis Ertugrul"
        if "Yemin" in m:
            fa += "#قسم"
            X += "Yemin"
        if "Ask i Memnu" in m:
            fa += "#عشق_ممنوع"
            X += "Ask i Memnu"
        if "Bozkir Arslani Celaleddin" in m:
            fa += "#جلال_الدین_خوارزمشاهی"
            X += "Bozkir Arslani Celaleddin"
        if "Kazara Ask" in m:
            fa += "#عشق_تصادفی"
            X += "Kazara Ask"
        if "Bas Belasi" in m:
            fa += "#بلای_جون"
            X += "Bas Belasi"
        if "Ask Mantik Intikam" in m:
            fa += "#عشق_منطق_انتقام"
            X += "Ask Mantik Intikam"
        if "Baht Oyunu" in m:
            fa += "#بازی_بخت"
            X += "Baht Oyunu"
        if "Ada Masali" in m:
            fa += "#قصه_جزیره"
            X += "Ada Masali"
        if "Askin Tarifi" in m:
            fa += "#طرز_تهیه_عشق"
            X += "Askin Tarifi"
        if "Yesilcam" in m:
            fa += "#سینمای_قدیم_ترکیه"
            X += "Yesilcam"
        if "Camdaki Kiz" in m:
            fa += "#دختر_پشت_پنجره"
            X += "Camdaki Kiz"
        if "Bir Zamanlar Kibris" in m:
            fa += "#روزی_روزگاری_در_قبرس"
            X += "Bir Zamanlar Kibris"
        if "Teskilat" in m:
            fa += "#تشکیلات"
            X += "Teskilat"
        if "Kardeslerim" in m:
            fa += "#خواهر_و_برادرانم"
            X += "Kardeslerim"
        if "Ogrenci Evi" in m:
            fa += "#خانه_دانشجویی"
            X += "Ogrenci Evi"
        if "Sihirli Annem" in m:
            fa += "#مادر_سحرآمیز_من"
            X += "Sihirli Annem"
        if "Yetis Zeynep" in m:
            fa += "#برس_زینب"
            X += "Yetis Zeynep"
        if "Hukumsuz" in m:
            fa += "#بی_قانون"
            X += "Hukumsuz"
        if "Saygi" in m:
            fa += "#احترام"
            X += "Saygi"
        if "Vahsi Seyler" in m:
            fa += "#چیز_های_وحشی"
            X += "Vahsi Seyler"
        if "Seref Bey" in m:
            fa += "#آقای_شرف"
            X += "Seref Bey"
        if "Gibi" in m:
            fa += "#مانند"
            X += "Gibi"
        if "Iste Bu Benim Masalim" in m:
            fa += "#این_داستان_من_است"
            X += "Iste Bu Benim Masalim"
        if "Son Yaz" in m:
            fa += "#آخرین_تابستان"
            X += "Son Yaz"
        if "Akinci" in m:
            fa += "#مهاجم"
            X += "Akinci"
        if "Kirmizi Oda" in m:
            fa += "#اتاق_قرمز"
            X += "Kirmizi Oda"
        if "Emanet" in m:
            fa += "#امانت"
            X += "Emanet"
        if "Ibo Show" in m:
            fa += "#برنامه_ایبو_شو"
            X += "Ibo Show"
        if "EDHO" in m:
            fa += "#راهزنان"
            X += "EDHO"
        if "Uyanis Buyuk Selcuklu" in m:
            fa += "#بیداری_سلجوقیان_بزرگ"
            X += "Uyanis Buyuk Selcuklu"
        if "Yasak Elma" in m:
            fa += "#سیب_ممنوعه"
            X += "Yasak Elma"
        if "Sadakatsiz" in m:
            fa += "#بی_وفا #بی_صداقت"
            X += "Sadakatsiz"
        if "Bir Zamanlar Cukurova" in m:
            fa += "#روزی_روزگاری_چوکورا"
            X += "Bir Zamanlar Cukurova"
        if "Gonul Dagi" in m:
            fa += "#کوه_دل"
            X += "Gonul Dagi"
        if "Ufak Tefek Cinayetler" in m:
            fa += "#خرده_جنایت_ها"
            X += "Ufak Tefek Cinayetler"
        if "Sibe Mamnooe" in m:
            fa += "#سیب ممنوعه"
            X += "Sibe Mamnooe"
        if "Setare Shomali" in m:
            fa += "#ستاره شمالی"
            X += "Setare Shomali"
        if "Otaghe Ghermez" in m:
            fa += "#اتاق قرمز"
            X += "Otaghe Ghermez"
        if "Mojeze Doctor" in m:
            fa += "#دکتر معجزه گر"
            X += "Mojeze Doctor"
        if "Be Eshghe To Sogand" in m:
            fa += "#به عشق تو سوگند"
            X += "Be Eshghe To Sogand"
        if "Eshgh Az No" in m:
            fa += "#عشق از نو"
            X += "Eshgh Az No"
        if "Eshghe Mashroot" in m:
            fa += "#عشق مشروط"
            X += "Eshghe Mashroot"
        if "Cukurova" in m:
            fa += "#روزی روزگاری چکوروا"
            X += "Cukurova"
        if "Yek Jonun Yek Eshgh" in m:
            fa += "#یک جنون یک عشق"
            X += "Yek Jonun Yek Eshgh"
        if "2020" in m:
            fa += "#2020"
            X += "2020"
        if "Hekim" in m:
            fa += "#حکیم اوغلو"
            X += "Hekim"
        if "Godal" in m:
            fa += "#گودال"
            X += "Godal"
        if "Cukur" in m:
            fa += "#گودال"
            X += "Cukur"
        if "Khaneh Man" in m:
            fa += "#سرنوشتت خانه توست"
            X += "Khaneh Man"
        if "Alireza" in m:
            fa += "#علیرضا"
            X += "Alireza"
        if "Dokhtare Safir" in m:
            fa += "#دختر سفیر"
            X += "Dokhtare Safir"
        if "Zarabane Ghalb" in m:
            fa += "#ضربان قلب"
            X += "Zarabane Ghalb"		
            
        if Z.__contains__("Fragman"):
            Jn = m.split("Bolum")[1]
            if "2" in Jn:
                tz += "#دوم"
            elif "1" in Jn:
                tz += "#اول"
            elif "3" in Jn:
                tz += "#سوم"
            elif "4" in Jn:
                tz += "#چهارم"
            elif "5" in Jn:
                tz += "#پنجم"
            elif "6" in Jn:
                tz += "#ششم"
            if X.__contains__("a") or X.__contains__("o") or X.__contains__("i") or X.__contains__("c") or X.__contains__("b") or X.__contains__("e") or X.__contains__("l") or X.__contains__("n") or X.__contains__("m"):
                Yd = X.replace(" ", "_")
                Lo += "#" + f"{Yd}"
                V = Kh.split("Bolum")[0]
                E = V.replace(".", "").replace("_", " ").replace("-", " ")
            else:
                E = ""
            Tzz = tz.replace("#", " ")
            date = "پنجشنبه ساعت 4 بامداد از رسانه اینترنتی دی ال مکوین"
            await message.edit(f"⬇️ تیزر{Tzz} قسمت {E} ({fa} ) {Lo} ، بازیرنویس چسبیده\n\n🔻 پخش {date}\n\n🆔👉 @dlmacvin_new")
        if (media.file_size > 50) and N.__contains__("E0") or N.__contains__("E1") or N.__contains__("E2") or N.__contains__("E3") or N.__contains__("E4") or N.__contains__("E5") or N.__contains__("E6") or N.__contains__("E7") or N.__contains__("E8") or N.__contains__("E9"):
            if '720P' in m:
                Q = '720'
            if '480P' in m:
                Q = '480'
            if '1080P' in m:
                Q = '1080'
            if '240P' in m:
                Q = '240'
            if Q:
                q = f"\n🔹کیفیت : {Q}"
            else:
                q = ""
            if 'E0' in N:
                O = N.split("E0")[1]
                T = O.split()[0]
                E = '0' + f"{T}"
                n = N.split("E0")[0]
            if 'E1' in N:
                O = N.split("E1")[1]
                T = O.split()[0]
                E = '1' + f"{T}"
                n = N.split("E1")[0]
            if 'E2' in N:
                O = N.split("E2")[1]
                T = O.split()[0]
                E = '2' + f"{T}"
                n = N.split("E2")[0]
            if 'E3' in N:
                O = N.split("E3")[1]
                T = O.split()[0]
                E = '3' + f"{T}"
                n = N.split("E3")[0]
            if 'E4' in N:
                O = N.split("E4")[1]
                T = O.split()[0]
                E = '4' + f"{T}"
                n = N.split("E4")[0]
            if 'E5' in N:
                O = N.split("E5")[1]
                T = O.split()[0]
                E = '5' + f"{T}"
                n = N.split("E5")[0]
            if 'E6' in N:
                O = N.split("E6")[1]
                T = O.split()[0]
                E = '6' + f"{T}"
                n = N.split("E6")[0]
            if 'E7' in N:
                O = N.split("E7")[1]
                T = O.split()[0]
                E = '7' + f"{T}"
                n = N.split("E7")[0]
            if 'E8' in N:
                O = N.split("E8")[1]
                T = O.split()[0]
                E = '8' + f"{T}"
                n = N.split("E8")[0]
            if 'E9' in N:
                O = N.split("E9")[1]
                T = O.split()[0]
                E = '9' + f"{T}"
                n = N.split("E9")[0]
            if E.startswith("0"):
                Ee = E.replace("0", "")
            else:
                Ee = E
            if not "Hard-Sub" in N:
                H = fa.replace("_", " ").replace("#", "")
                await message.edit(f"🔺{H} قسمت {Ee} \n🔸 دوبله فارسی {q} \n🆔👉 @dlmacvin_new | {fa}")
            else:
                if message.video:
                    await message.edit(f"♨️ سریال{fa} ( {n}) بازیرنویس چسبیده\n👌قسمت : {Ee} {q} \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new")
                else:
                    await message.edit(f"♨️ سریال{fa} ( {n}) بازیرنویس چسبیده\n👌قسمت : {Ee} {q} \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new")
        elif (media.file_size > 50) and not N.__contains__("E0") or N.__contains__("E1") or N.__contains__("E2") or N.__contains__("E3") or N.__contains__("E4") or N.__contains__("E5") or N.__contains__("E6") or N.__contains__("E7") or N.__contains__("E8") or N.__contains__("E9"):
            if "20" in D:
                f = D.split("20")[0]
                U = D.split("20")[1]
                K = U.split()[0]
                Y = '20' + f"{K}"
                YR = f"\n👌سال : {Y}"
            if "19" in D:
                f = D.split("19")[0]
                U = D.split("19")[1]
                K = U.split()[0]
                Y = '19' + f"{K}"
                YR = f"\n👌سال : {Y}"
            W = "20" or "19"
            if not W in D:
                P = m.split("0P")[0]
                f = P.replace("72", "").replace("48", "").replace("108", "").replace("24", "")
                YR = f"\n👌سال :"
            if '720P' in m:
                Q = '720'
            if '480P' in m:
                Q = '480'
            if '1080P' in m:
                Q = '1080'
            if '240P' in m:
                Q = '240'
            if Q:
                G = f"\n🔹کیفیت : {Q}"
                q = G.replace(".1", " ").replace(".mkv", " ")
            else:
                q = ""
            await message.edit(f"♨️ فیلم {f} بازیرنویس چسبیده{YR} {q} \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new")
