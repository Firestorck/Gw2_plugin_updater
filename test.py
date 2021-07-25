ConfigF = open("config_updater.txt", "r")
config = ConfigF.readlines()
links = []
n = -1
for i in config:
    n = n+1
    print(n)
    print(i)
    if config[n].startswith('    https://'):
        new_link = config[n].strip() # or config[n].replace(" ", "")
        new_link = new_link.replace("\n", '')
        links.append(new_link)
        print(f'added {new_link} to links.')
print('\r\nprinting links')
for i in links:
    print(i)
print('test')