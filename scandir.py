# -*- coding: utf-8 -*-
"""
Created on 24 OCT 2018


"""
from fileinput import filename
__author__ = "Marcin Roszczyk"
__copyright__ = "Copyright 2018, Marcin Roszczyk"
__credits__ = [" ", "  "]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Marcin Roszczyk"
__email__ = "mikolunar@github.com"
__status__ = "Development"

import os
import sys
from os import walk
import time
import datetime
import platform
import operator
from collections import Counter
import logging
import json




# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# #setting up logger 
# def setup_logging(
#     default_path='log_conf.json',
#     default_level=logging.INFO,
#     env_key='LOG_CFG'
# ):
#     """Setup logging configuration

#     """
#     path = default_path
#     value = os.getenv(env_key, None)
#     if value:
#         path = value
#     if os.path.exists(path):
#         with open(path, 'rt') as f:
#             config = json.load(f)
#         logging.config.dictConfig(config)
#     else:
#         logging.basicConfig(level=default_level)


# def bytesToString(bytes):
#     if 1000< bytes < 1000000:
#         return str(bytes/1000)+' KB'
#     elif bytes>1000000 and bytes<10000000000:
#         return str(bytes/1000000) + ' MB'
#     elif bytes>10000000000:
#         return str(bytes/(1000000000))+' GB'


class DataCapture:

    filename=''
    dirname=''

    def __init__(self, dirname, filename):
        self.filename=filename
        self.dir=dirname


    def set_writer(self, filename):
        return True

    def store_data(self, DirData):
        return DirData


class DirData:
    scan_info={}
    data=[]

# Get dir data:files and folders

def getSystemInfo():

    system_info={}

    system_info['OS']= os.name
    system_info['Platform']=platform.system()
    system_info['Rel']=platform.release()
    system_info['Architecture']= platform.architecture()

    return system_info


def getDirData(root_dir):

          
    #start_time=datetime.datetime.fromtimestamp(time.time())
    #start_collection_time=datetime.datetime.fromtimestamp(time.time())
    
    scan = walk(root_dir)
    DirData.data=list(scan)    
    dirs=len(DirData.data)

    file_count=0

    for items in scan:
        file_count+=len(items)
    
    DirData.scan_info['Number of dirs']=dirs
    DirData.scan_info['Number of files']=file_count
   
    return DirData


def scanDir(rootpath, full_scan, output_file):
    
    counter=0
    myfile=open(output_file, 'w',  encoding='utf-8', newline='\n')
    # #print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

    
    # start_collection_time=datetime.datetime.fromtimestamp(time.time())
    
    no_files=0
    total_size=0
    ext_set=[]
    total_types=0
    max_size=0
    max_directory_size=0
    directory_size=0
    type_sizes={}
    dir_counter=0
    max_size_file=0
    max_directory=""

    myfile.write("ID"+';'+ "Directory"+';'+"File"+';'+'File Size'+';'+'File Type'+';'+'Mod Time'+';'+'Access Time'+';'+'Modification'+';'+'Creation Time'+'\n')
    
    for dir_item in scan_info:
        no_files+=len(dir_item[2])       
        directory_size=0
        dir_counter=dir_counter+1
        for file_item in dir_item[2]:
            file_path=os.path.join(dir_item[0],file_item)
            file_info=os.stat(file_path) 
            file_size=os.path.getsize(file_path)
            file_access=time.asctime(time.localtime(os.path.getatime(file_path)))
            file_mtime=time.asctime(time.localtime(os.path.getmtime(file_path)))
            file_crtime=time.asctime(time.localtime(os.path.getctime(file_path)))
            
            file_name, file_ext=os.path.splitext(file_item)
            #file_ext='NULL'
            ext_set.append(file_ext) 
            if file_ext in type_sizes:
                type_sizes[file_ext]+=type_sizes[file_ext]
            else:
                type_sizes.update({file_ext:file_size})  

            #file_size=file_info.st_size 
            file_mod_time=time.asctime(time.localtime(file_info.st_mtime))
            directory_size+=file_size
            counter=counter+1
            #myfile.write(str(counter)+';'+dir_item[0]+';'+file_item+';'+str(file_size)+';'+file_ext+';'+str(file_mod_time)+';'+file_access+';'+file_mtime+';'+file_crtime+'\n')
            #work_progress = '{0:.0f}'.format((dir_counter / dirs))
            work_progress=(dir_counter/dirs)*100
            work_progress=str(work_progress)[0:4]
            sys.stdout.write("\r Directories  .. %s  files %s of   " % (work_progress, counter))
            # \r %s " %counter )
            #sys.stdout.write(str(dir_counter))           
            sys.stdout.flush()
            if file_size>max_size:
                max_size=file_size 
                max_size_file=file_path
            total_size+=file_info.st_size
        if directory_size>max_directory_size:
            max_directory_size=directory_size
            max_directory=dir_item[0]
    
    cnt=Counter(ext_set)
    
    dist_types=set(ext_set)
    total_types+=len(dist_types)  
    most_common_files=cnt.most_common(total_types)

    myfile.close()
   
   
    # finish_time=datetime.datetime.fromtimestamp(time.time())
    # print('Done')
    # print('Timestamp',finish_time)
    # print('Duration', finish_time-start_time)

    # stat_file=open('sensid_file_system_prescan_stats.csv', 'w',  encoding='utf-8', newline='\n')
    # stat_file.write('Total number of files'+';'+str(no_files)+'\n')


    # print('----------------------------- 3 Statistics -------------------------------')
    # print('Total number of files: ', no_files)

    # stat_file.write('Total size of data'+';'+str(total_size)+'\n')
    # print('Total size of data: ', bytesToString(total_size))

    # stat_file.write('Total number of identified file types'+';'+str(total_types)+'\n')    
    # print('Total number of identified file types: ', total_types)

    # stat_file.write('Total number of uknown file types: TBC'+';'+'0'+'\n')
    # print('Total number of unknow file type: TBC' )

    # stat_file.write('Maximum file size'+';'+str(max_size)+'\n')
    # stat_file.write('Maximum file size path'+';'+str(max_size_file)+'\n')
    # print('Maximum file\'s size: ',bytesToString(max_size), max_size_file)
    
    # print('Maximum directory size:', max_directory_size, max_directory)
        
    
    # #write additional info to file
    # print('Check additional statistics in sensid_file_system_prescan_stats.csv')
 
    # print('Most frequent file types: ')
    # for item in most_common_files:
    #     print(str(item[1]), ': '+str(item[0]))
        
    # # print('TBC Size by type')
    # # for i in type_sizes:
    # #     print(i, ' ', type_sizes[i])
    # # stat_file.close()

    # # print(type_sizes)
   

    # return True

#####################################################
# main script
# start logging

# logger.info('Start skandir')
# logger.debug('Records: %s', 7)
# logger.info('Updating records ...')
# # update records here
# logger.info('Finish updating records')

for i in range(len(sys.argv)):
    print("Input argument :",i,': ', sys.argv[i] )

if len(sys.argv)==1:
    
    print('No arguments, using default \n')
    out_file='scandir.csv'
    source_dir='.'
else:
    
    if len(sys.argv)==3:
        out_file=sys.argv[2]
        source_dir=sys.argv[1]
    else:
        print(sys.argv[0])
        print("Missing parameters: [1] source directory [2] output directory")
        exit()

#'d:\\00. My Personal\\01. Travel\\Windsurf'
dir_data=getDirData(source_dir)
print(dir_data.scan_info)
print(dir_data.data)
user=input('Do you want to write raw data to file? [Y]ES/[N]O: ')
if user=='Y':
    dc=DataCapture('.','test.csv')
    print(dc.store_data(DirData))
elif user=='N':
    pass

else:
    exit()