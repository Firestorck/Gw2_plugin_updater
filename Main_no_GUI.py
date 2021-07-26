from os import kill
import requests

def Startup():
    #print("Bienvenue dans le programme d'installation et de mise à jour de plugins pour GuildWars 2")
    #print("Fait par Firestorck")
    print('Welcome to the installation and update program for guildwars 2 plugins, by Firestorck')

    try:        #Opens config or start the config process
        open("config_updater.txt", "r")
    except:
        #if re.lower().findall("n", input("Il semblerais que ça soit votre première utilisation du programme, Voulez-vous commencer la configuration? (N pour annuler)")) != 0:
        #    print("début de la configuration.")
        #    Config()
        #else:
        #    print('Vous avez décidé de ne pas configurer ce programme, il utilisera donc la configuration par défaut. Vous pourrez toujours changer ces paramètres en modifiant le fichier "config_updater.txt" ou en le supprimant')
        if input("It seems like it is you first time using this programm, Do you want to start the config? (N for manual configuration, enter for automatic configuration.)").lower().find("n") == -1:
            print('You have decided to not manually configurate this programm. All will be set to default, but you can still change them by editing or deleting the "config_updater.txt"')
            open('config_updater.txt', 'w').write("#Firestorck's plugin updater for GuildWars2\r\npath : C:\\Program Files\\Guild Wars 2\\bin64\r\narcdps\r\n    True\r\n    https://www.deltaconnected.com/arcdps/x64/d3d9.dll\r\n    d3d9.dll\r\nhealing stats\r\n    True\r\n    https://github.com/Krappa322/arcdps_healing_stats/releases/latest/download/arcdps_healing_stats.dll\r\n    d3d9_arcdps_healing_stats\r\nbuildpad\r\n    True\r\n    https://buildpad.gw2archive.eu/versions/latest\r\n    d3d9_arcdps_buildpad.dll\r\nkillproof\r\n    True\r\n    https://github.com/knoxfighter/arcdps-killproof.me-plugin/releases/latest/download/d3d9_arcdps_killproof_me.dll\r\n    d3d9_arcdps_killproof_me.dll\r\nmechanics\r\n    True\r\n    https://github.com/knoxfighter/GW2-ArcDPS-Mechanics-Log/releases/latest/download/d3d9_arcdps_mechanics.dll\r\n    d3d9_arcdps_mechanics.dll\r\nboon table\r\n    True\r\n    https://github.com/knoxfighter/GW2-ArcDPS-Boon-Table/releases/latest/download/d3d9_arcdps_table.dll\r\n    d3d9_arcdps_table.dll\r\n")
        else:
            print("Start of the configuration")
            ConfigEdit()

def ConfigEdit():
    open("config_updater.txt", "a").write("#Firestorck's plugin updater for GuildWars2\r\n")
    #Config.write("#Firestorck's plugin updater for GuildWars2\r\n")
    path = r'C:\Program Files\Guild Wars 2\bin64'
    arcdps = [r'https://www.deltaconnected.com/arcdps/x64/d3d9.dll', 'arcdps', 'd3d9.dll']
    healing_stats = [r'https://github.com/Krappa322/arcdps_healing_stats/releases/latest/download/arcdps_healing_stats.dll', 'healing stats', 'd3d9_arcdps_healing_stats']
    buildpad = [r'https://buildpad.gw2archive.eu/versions/latest', 'buildpad', 'd3d9_arcdps_buildpad.dll']
    killproof = [r'https://github.com/knoxfighter/arcdps-killproof.me-plugin/releases/latest/download/d3d9_arcdps_killproof_me.dll', 'killproof', 'd3d9_arcdps_killproof_me.dll']
    mechanics = [r'https://github.com/knoxfighter/GW2-ArcDPS-Mechanics-Log/releases/latest/download/d3d9_arcdps_mechanics.dll', 'mechanics', 'd3d9_arcdps_mechanics.dll']
    boontable = [r'https://github.com/knoxfighter/GW2-ArcDPS-Boon-Table/releases/latest/download/d3d9_arcdps_table.dll', 'boon table', 'd3d9_arcdps_table.dll']
    if input(f"Is {path} the path to your Guildwars 2 folder?").lower().find("n") == -1 :
        open("config_updater.txt", "a").write(f'path : {path}\r\n')
    else:
        path = input('Please write the path to the "bin64" folder of your game\r\n')
        open("config_updater.txt", "a").write(f'path : {path}\r\n')
    ConfigLinks(arcdps)
    ConfigLinks(healing_stats)
    ConfigLinks(buildpad)
    ConfigLinks(killproof)
    ConfigLinks(mechanics)
    ConfigLinks(boontable)
    print("config done")

def ConfigLinks(Data):
    if input(f'\r\nDo you want to install {Data[1]} ? (N to cancel, enter to continue)\r\n').lower().find('n') == -1:
        if input(f'Keep theese informations?\r\n Download link : {Data[0]} \r\nFinal file name : {Data[2]}\r\n').lower().find('n') == -1:
            open('config_updater.txt', 'a').write(f'{Data[1]}\r\n    True\r\n    {Data[0]}\r\n    {Data[2]}\r\n')
        else:
            
            usr_input = input(f'Please enter the new name for {Data[1]}\r\n')
            if usr_input.replace(' ', '') != '':
                Data[1] = usr_input
            else:
                print(f'Could not find a correct input, set to default as {Data[1]}')
            
            usr_input = input(f'Please enter the new File name for {Data[2]} in the format of "d3d9_arcdps_<name>.dll\r\n')
            if usr_input.replace(' ', '') != '':
                Data[2] = usr_input
            else:
                print(f'Could not find a correct input, set to default as {Data[2]}')
                usr_input = Data[2]
            while usr_input.find('.dll') == -1 and usr_input.find('d3d9') == -1:
                usr_input = input(f'Please enter the new File name for {Data[1]} in the format of "d3d9_arcdps_<name>.dll\r\n')
                if usr_input.replace(' ', '') != '':
                    Data[2] = usr_input
                else:
                    print(f'Could not find a correct input, set to default as {Data[2]}')
                    usr_input = Data[2]
            
            usr_input = input(f'Please enter the new download link for {Data[0]}\r\n')
            if usr_input.replace(' ', '') != '':
                Data[0] = usr_input
            else:
                print(f'Could not find a correct input, set to default as {Data[0]}')
                usr_input = Data[0]
            while usr_input.find('http') == -1:
                usr_input = input(f'Please enter the new download link for {Data[1]}\r\nLast input : {Data[0]}\r\n')
                if usr_input.replace(' ', '') != '':
                    Data[0] = usr_input
                else:
                    print(f'Could not find a correct input, set to default as {Data[0]}')
                    usr_input = Data[0]
            open('config_updater.txt', 'a').write(f'{Data[1]}\r\n    False\r\n    {Data[0]}\r\n    {Data[2]}\r\n')

def UpdateAuto():
    ConfigF = open("config_updater.txt", "r")
    config = ConfigF.readlines()
    links, filenames = [], []
    n = -1
    Enabled = False
    for i in config:        #use a loop to read the config file and extract the links from it.
        n = n+1
        if config[n].startswith('    https://') and Enabled == True:
            new_link = config[n].strip() # or config[n].replace(" ", "")
            new_link = new_link.replace("\n", '')
            links.append(new_link)
            filenameL = new_link.split('/')
            for i in filenameL:
                filename = i
                if filename.lower().find('.dll') == -1:
                    filename = config[n + 1].strip()
            filenames.append(filename)
            #print(f'added {new_link} to links.')
        elif config[n].startswith('path : '):
            path = config[n].replace('path : ', '')
            path = path.replace('\n', '')
        if config[n].startswith('    True'):
            print()
            Enabled = True
        else:
            Enabled = False
    print('\r\nLinks found :')
    for i in links:
        print(i)
    print('\r\nFile names found :')
    for i in filenames:
        print(i)
    n = 0
    for i in filenames:
        Plugin = requests.get(links[n], allow_redirects=True)
        open(path + '\\' + filenames[n], 'wb').write(Plugin.content)
        print('Written ' + path + '\\' + filenames[n] + "\r\nfrom " + links[n])
        n = n+1

Startup()
UpdateAuto()