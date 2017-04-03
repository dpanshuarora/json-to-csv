#Make Python understand the stuff in a page on the Internet is JSON
import json
 
# Make Python understand csvs
import csv
  
# tell computer where to put CSV
outfile_path='F://file.csv'
 
# open it up, the w means we will write to it
writer = csv.writer(open(outfile_path, 'w'))
 
#create a list with headings for our columns
headers = ['Duration', 'Costs','SocCode']
 
#write the row of headings to our CSV file
writer.writerow(headers)
 
 
# GET JSON AND PARSE IT INTO DICTIONARY
# You can also use file operations in Python to extract data from a .json file
data = '{"mailbox":{"showForTypeB":false,"showForTypeS":true,"showForTypeI":false,"url":"https://mailboxansagepro.vodafone.de","enable":true},"costs":[{"duration":"monthly","costs":"5,00 &euro;","socCode":"01INTMIN6"},{"duration":"monthly","costs":"4,99 &euro;","socCode":"03BILDPA"},{"duration":"monthly","costs":"25,00 &euro;","socCode":"24MESALLN"},{"duration":"monthly","costs":"10,00 &euro;","socCode":"24MESFLAT"},{"duration":"monthly","costs":"10,00 &euro;","socCode":"24MIN120"},{"duration":"monthly","costs":"20,00 &euro;","socCode":"24MIN240"},{"duration":"monthly","costs":"5,00 &euro;","socCode":"24MIN60"},{"duration":"monthly","costs":"25,00 &euro;","socCode":"24SMSALL"},{"duration":"monthly","costs":"4,99 &euro;","socCode":"BILD1"},{"duration":"monthly","costs":"7,99 &euro;","socCode":"DEEZER1"},{"duration":"monthly","costs":"0,00 &euro;","socCode":"NO_LIMEU"},{"duration":"monthly","costs":"4,99 &euro;","socCode":"RFLATMON2"},{"duration":"monthly","costs":"4,99 &euro;","socCode":"RFLATMONT"},{"duration":"monthly","costs":"9,99 &euro;","socCode":"TURKEY99"},{"duration":"monthly","costs":"9,99 &euro;","socCode":"TURKEY99R"},{"duration":"monthly","costs":"0,00 &euro;","socCode":"VF_ASOPT"},{"duration":"monthly","costs":"29,95 &euro;","socCode":"VF_TURKEY"}],"saveAndSecure":{"enable":true,"url":"https://securenet.vodafone.de/"},"icons":[{"icon":"http://media.vodafone.de/www/images/app/roaming.png","socCode":"01INTMIN3"},{"icon":"http://media.vodafone.de/www/images/app/roaming.png","socCode":"01INTMIN6"},{"icon":"http://media.vodafone.de/www/images/app/deezer.png","socCode":"03AMPYA"},{"icon":"http://media.vodafone.de/www/images/app/bild.png","socCode":"03BILDPA "},{"icon":"http://media.vodafone.de/www/images/app/sms.png","socCode":"24MESALLN"},{"icon":"http://media.vodafone.de/www/images/app/sms.png","socCode":"24MESFLAT"},{"icon":"http://media.vodafone.de/www/images/app/minutes.png","socCode":"24MIN120"},{"icon":"http://media.vodafone.de/www/images/app/minutes.png","socCode":"24MIN240"},{"icon":"http://media.vodafone.de/www/images/app/minutes.png","socCode":"24MIN60"},{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","socCode":"24UMTS_I1"},{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","socCode":"24UMTS_I2"},{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","socCode":"ASB_ON"},{"icon":"http://media.vodafone.de/www/images/app/bild.png","socCode":"BILD1"},{"icon":"http://media.vodafone.de/www/images/app/roaming.png","socCode":"DASDAY30"},{"icon":"http://media.vodafone.de/www/images/app/deezer.png","socCode":"DEEZER1"},{"icon":"http://media.vodafone.de/www/images/app/deezer.png","socCode":"DEEZERDIS "},{"icon":"http://media.vodafone.de/www/images/app/deezer.png","socCode":"DEEZSRED1"},{"icon":"http://media.vodafone.de/www/images/app/roaming.png","socCode":"EASYTRAVEL_Day_In"},{"icon":"http://media.vodafone.de/www/images/app/roaming.png","socCode":"EASYTRAVEL_FLAT_In"},{"icon":"http://media.vodafone.de/www/images/app/roaming.png","socCode":"EASYTRAVEL_Month_In"},{"icon":"http://media.vodafone.de/www/images/app/roaming.png","socCode":"EASYTRAVEL_Week_In"},{"icon":"http://media.vodafone.de/www/images/app/mobiletv.png","socCode":"MOBTV "},{"icon":"http://media.vodafone.de/www/images/app/mobiletv.png","socCode":"MOBTVGRAT"},{"icon":"http://media.vodafone.de/www/images/app/netflix.png","socCode":"NETFSRED1"},{"icon":"http://media.vodafone.de/www/images/app/roaming.png","socCode":"NO_LIMEU"},{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","socCode":"NPSLTE100"},{"icon":"http://media.vodafone.de/www/images/app/mobiletv.png","socCode":"PROMO029 "},{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","socCode":"REDLTEDAT"},{"icon":"http://media.vodafone.de/www/images/app/roaming.png","socCode":"RFLATDAY"},{"icon":"http://media.vodafone.de/www/images/app/roaming.png","socCode":"RFLATMONT"},{"icon":"http://media.vodafone.de/www/images/app/saveandsecure.png","socCode":"save and secure"},{"icon":"http://media.vodafone.de/www/images/app/sky.png","socCode":"SKYRABATT"},{"icon":"http://media.vodafone.de/www/images/app/sky.png","socCode":"SKYSRED2"},{"icon":"http://media.vodafone.de/www/images/app/sky.png","socCode":"SKYSRED3"},{"icon":"http://media.vodafone.de/www/images/app/roaming.png","socCode":"VF_ASOPT"},{"icon":"http://media.vodafone.de/www/images/app/roaming.png","socCode":"VF_RCROW"}],"cancelableTarifOptions":[{"socCode":"NO_LIMEU"},{"socCode":"VF_ASOPT"},{"socCode":"VF_BUSROB"},{"socCode":"VF_VODROB"},{"socCode":"AROAMFOC"},{"socCode":"AROAM"},{"socCode":"VF_RCROW"},{"socCode":"VF_RCOCO"},{"socCode":"DASDAY"},{"socCode":"DASDAY30"},{"socCode":"RFLATDAY"}],"highspeedTarifOptions":[{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","gb":"10","price":"100,00","socCode":"01REPL10G"},{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","gb":"9","price":"90,00","socCode":"01REDPL9G"},{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","gb":"8","price":"80,00","socCode":"01REDPL8G"},{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","gb":"7","price":"70,00","socCode":"01REDPL7G"},{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","gb":"6","price":"60,00","socCode":"01REDPL6G"},{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","gb":"5","price":"50,00","socCode":"01REDPL5G"},{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","gb":"4","price":"40,00","socCode":"01REDPL4G"},{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","gb":"3","price":"30,00","socCode":"01REDPL3G"},{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","gb":"2","price":"20,00","socCode":"01REDPL2G"},{"icon":"http://media.vodafone.de/www/images/app/highspeed.png","gb":"1","price":"10,00","socCode":"01REDPL1G"}]}'

#use the JSON library to turn this file into a Pythonic data structure
parsed_json = json.loads(data)

#now you have a giant dictionary

#run through each item in results, and jump to an item in that dictionary

for data in parsed_json['costs']:
          #initialize the row
          row = []
          #add every 'cell' to the row list, identifying the item just like an index in a list
          row.append(str(data['duration']))
          row.append(str(data['costs']))
          row.append(str(data['socCode']))

          #once you have all the cells in there, write the row to your csv
          writer.writerow(row)
