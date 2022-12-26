## os.system('ls > ls.txt')

# list_ls = []
# list_code = ['py','html','txt','css']

# with open('ls.txt', 'r') as f:
#     f = f.read()
#     for i in f.split():
#         list_ls.append(i)
    
#     for passes in list_ls:
#         for j in passes.split('.'):
#             if j in list_code:
#                 os.system(f'mv {passes} /home/marselle/Рабочий\ стол/def\ main/lessons2')



# def file_passes():
#     list_file = ['Загрузки','Видео','Музыка','Рабочий\ стол','Изображения']
#     for i in range(1):
#         for passes in list_file:
            
#     os.system('cd')
#     time.sleep(1)
#     os.system(f'cd {passes}')
#     time.sleep(1)
#     os.system('ls > list.txt')       
        
import os, time
        

def download_passes():
    list_file = []
    list_expansion = ['png', 'jpg', 'jpeg']
    os.system('cd /home/oem/Загрузки')
    os.system('ls /home/oem/Загрузки > /home/oem/Рабочий\ стол/def\ main/list.txt')
    time.sleep(1)
    with open('list.txt', 'r') as file:
        ls_download = file.read()
    for name_file in ls_download.split():
        
        print(name_file)
        
        
    for items in ls_download.split('.'):
        p = items.split()
        if p in list_expansion:
            os.system(f'mv {items} /home/oem/Изображения')
        else:
            continue
            
                
            # if item in list_expansion.split('.'):
print(download_passes())

