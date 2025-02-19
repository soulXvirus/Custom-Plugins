import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from pyrogram import enums

from userge import userge, Message, config
from userge.utils import take_screen_shot


@userge.on_cmd("h", about={
    'header': "Protecc waifu",
    'description': "Reverse Search waifu and protecc it",
    'usage': "{tr}h [Reply to waifu bot]"})
async def protec(message: Message):
    start = datetime.now()
    dis_loc = ''
    base_url = "https://www.google.com"
    out_str = "Reply to an image to do Google Reverse Search"
    if message.reply_to_message:
        await message.edit("Downloading Media to my Local")
        message_ = message.reply_to_message
        if message_.sticker and message_.sticker.file_name.endswith('.tgs'):
            await message.edit('Bruh, Searching Animated Sticker is no(T YET) implemented')
            return
        if message_.photo or message_.animation or message_.sticker:
            dis = await message.client.download_media(
                message=message_,
                file_name=config.Dynamic.DOWN_PATH
            )
            dis_loc = os.path.join(config.Dynamic.DOWN_PATH, os.path.basename(dis))
        if message_.animation:
            await message.edit("Converting this Gif to Image")
            img_file = os.path.join(config.Dynamic.DOWN_PATH, "grs.jpg")
            await take_screen_shot(dis_loc, 0, img_file)
            if not os.path.lexists(img_file):
                await message.err("Something went wrong in Conversion")
                return
            dis_loc = img_file
        if dis_loc:
            search_url = "{}/searchbyimage/upload".format(base_url)
            multipart = {
                "encoded_image": (dis_loc, open(dis_loc, "rb")),
                "image_content": ""
            }
            google_rs_response = requests.post(search_url, files=multipart, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
            os.remove(dis_loc)
        else:
            await message.edit("No one's gonna help ya (¬_¬)")
            return
        await message.edit("Found Google Result. Lemme pass some Soup;)!")
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        }
        response = requests.get(the_location, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
        except IndexError:
            return await message.err("Index went out of range, Maybe no results were found")
        prs_anchor_element = prs_div.find("a")
        prs_url = base_url + prs_anchor_element.get("href")
        prs_text = prs_anchor_element.text
        img_size_div = soup.find(id="jHnbRc")
        img_size = img_size_div.find_all("div")
        end = datetime.now()
        ms = (end - start).seconds
        out_str = f"""/protecc {prs_text}"""
    await message.reply(out_str, parse_mode=enums.ParseMode.HTML, disable_web_page_preview=True)
    await message.delete()


@userge.on_cmd("c", about={
    'header': "Protecc waifu",
    'description': "Reverse Search waifu and protecc it",
    'usage': "{tr}protecc [Reply to waifu bot]"})
async def protec(message: Message):
    start = datetime.now()
    dis_loc = ''
    base_url = "https://www.google.com"
    out_str = "Reply to an image to do Google Reverse Search"
    if message.reply_to_message:
        await message.edit("Downloading Media to my Local")
        message_ = message.reply_to_message
        if message_.sticker and message_.sticker.file_name.endswith('.tgs'):
            await message.edit('Bruh, Searching Animated Sticker is no(T YET) implemented')
            return
        if message_.photo or message_.animation or message_.sticker:
            dis = await message.client.download_media(
                message=message_,
                file_name=config.Dynamic.DOWN_PATH
            )
            dis_loc = os.path.join(config.Dynamic.DOWN_PATH, os.path.basename(dis))
        if message_.animation:
            await message.edit("Converting this Gif to Image")
            img_file = os.path.join(config.Dynamic.DOWN_PATH, "grs.jpg")
            await take_screen_shot(dis_loc, 0, img_file)
            if not os.path.lexists(img_file):
                await message.err("Something went wrong in Conversion")
                return
            dis_loc = img_file
        if dis_loc:
            search_url = "{}/searchbyimage/upload".format(base_url)
            multipart = {
                "encoded_image": (dis_loc, open(dis_loc, "rb")),
                "image_content": ""
            }
            google_rs_response = requests.post(search_url, files=multipart, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
            os.remove(dis_loc)
        else:
            await message.edit("No one's gonna help ya (¬_¬)")
            return
        await message.edit("Found Google Result. Lemme pass some Soup;)!")
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        }
        response = requests.get(the_location, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
        except IndexError:
            return await message.err("Index went out of range, Maybe no results were found")
        prs_anchor_element = prs_div.find("a")
        prs_url = base_url + prs_anchor_element.get("href")
        prs_text = prs_anchor_element.text
        img_size_div = soup.find(id="jHnbRc")
        img_size = img_size_div.find_all("div")
        end = datetime.now()
        ms = (end - start).seconds
        out_str = f"""/catch {prs_text}"""
    await message.reply(out_str, parse_mode=enums.ParseMode.HTML, disable_web_page_preview=True)
    await message.delete()
