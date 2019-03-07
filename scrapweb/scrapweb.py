#!/usr/bin/env python

import requests
import lxml.html
 
class Game:

        def __init__(self,title,price,tags,platforms):
                self.title= title
                self.price=  price
                self.tags= tags
                self.platforms= platforms



html = requests.get ('https://store.steampowered.com/exolore/new/')
doc = lxml.html.fromstring(html.content)

newReleases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]
print(newReleases)


#titulo
titles = newReleases.xpath('.//div[@class="tab_item_name"]/text()')
#print(titles)


#precios
prices = newReleases.xpath('.//div[@class="discount_final_price"]/text()')
#print(prices)


#etiquetas
tags = newReleases.xpath('.//div[@class="tab_item_top_tags"]')
totalTags=[]

for tag in tags:
    totalTags.append(tag.text_content())

totalTags = [tag.split(', ') for tag in totalTags]
#print(totalTags)

#plataformas
platformsDiv = newReleases.xpath('.//div[@class="tab_item_details"]')
totalPlatforms=[]

for game in platformsDiv:
    namePlatform= game.xpath('.//span[contains(@class, "platform_img")]')
    platforms=[t.get('class').split(' ')[-1] for t in namePlatform]
    if 'had_separator' in platforms:
        platforms.remove('had_separator')
    totalPlatforms.append(platforms)

#print(totalPlatforms)

output = []

for info in zip(titles,prices,totalTags,totalPlatforms):
        response= {}
        response['title'] = info[0]
        response['price'] = info[1]
        response['tags'] = info[2]
        response['platforms'] = info[3]
        output.append(response)

#print(output)

count=1

for info in zip(titles,prices,totalTags,totalPlatforms):
    game1 = Game(info[0],info[1],info[2],info[3])
    
    print("************************************************")
    print("Game "+str(count))
    count=count+1
    print("Title: "+ game1.title)
    print("Price:"+ game1.price)
    print("tags: "+ str(game1.tags))
    print("Platforms: "+ str(game1.platforms))
    print("************************************************")
       