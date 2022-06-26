import time
from pyrogram import filters
from datetime import datetime
from asyncio import sleep
import os
from bs4 import BeautifulSoup
import requests
screen_shot = "downloads/"
async def harem_steal(client, message): 
  S = datetime.now()
  dis_loc = '' 
  if not message.photo:
    return
  dis = await message.client.download_media(
                message=message_,
                file_name=config.Dynamic.DOWN_PATH
            ) 
  dis_loc = os.path.join(config.Dynamic.DOWN_PATH, os.path.basename(dis))
  if dis_loc: 
    base_url = "http://www.google.com" 
    search_url = "{}/searchbyimage/upload".format(base_url) 
    multipart = {
                "encoded_image": (dis_loc, open(dis_loc, "rb")),
                "image_content": ""
            } 
    google_rs_response = requests.post(search_url, files=multipart, allow_redirects=False)
    the_location = google_rs_response.headers.get("Location")
    os.remove(dis_loc) 
  else: 
    await message.delete() 
    return 
  headers = { "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0" } 
  response = requests.get(the_location, headers=headers) 
  soup = BeautifulSoup(response.text, "html.parser") 
  try:
    prs_div = soup.find_all("div", {"class": "r5a77d"})[0] 
  except:
    return
  prs_anchor_element = prs_div.find("a") 
  prs_text = prs_anchor_element.text
  E = datetime.now()
  out_str = f"/protecc {prs_text}" 
  await message.reply_chat_action('typing')
  await message.reply(out_str)

flt = filters.user([792028928, 1334822377, 1232515770, 1086660682, 1733263647,1340683830]) & filters.chat(-1001760969463) & filters.photo

from userge import userge 
from pyrogram.handlers import MessageHandler
userge.add_handler(MessageHandler(harem_steal, flt))
