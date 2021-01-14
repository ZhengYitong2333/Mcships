# -*- coding=utf-8 -*-

import os
import random
import xml.etree.ElementTree as ET
from shutil import copyfile
import cv2 as cv
from os import listdir, getcwd
from os.path import join

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(path,image_id,classes,save_xml_path,save_img_path,classnum):
    in_file = open(path+'Annotations/'+image_id+'.xml')
    
    out_file = open(save_xml_path+image_id+'.txt', 'w+')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    copyfile(path+'JPEGImages/'+image_id+'.jpg',save_img_path+image_id+'.jpg')
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        if classnum == 2:
        	cls_id = int(classes.index(cls)/3)
        elif classnum == 4:
        	cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

	
	
def test_dir(paths):
    if isinstance(paths,list):
        for path in paths:
            if not os.path.exists(path):
                os.makedirs(path)
        return 1
    elif isinstance(paths,str):
        if not os.path.exists(paths):
            os.makedirs(paths)
        return 1
    else:
        print('test_dir error!Please check your input!')
        return 1

def voc_label(path,classnum):
    sets=[('2007', 'train'),('2007', 'val'),('2007', 'test')]
   
    classes = ["aircraft","submarines","destroyer","civilianship"]
    classes1 = ["warship","civilianship"]
    if classnum == 4:
        _classes = classes
        
        for year,image_set in sets:
        	test_dir(path+'labels/')
        	image_ids = open(path+'ImageSets/Main1/'+image_set+'.txt').read().strip().split()
        	list_file = open('%s%s_%s.txt'%(path,year, image_set), 'w+')
        	save_path_xml = path + 'labels/' + image_set + '/'
        	test_dir(save_path_xml)
        	save_img_path = path+'images/' + image_set + '/'
        	test_dir(save_img_path)
        	for image_id in image_ids:
        		list_file.write(path+'JPEGImages/%s.jpg\n'%(image_id))
        		convert_annotation(path,image_id,_classes,save_path_xml,save_img_path,classnum)
        		print('create_label'+image_id+'Done!')
        	list_file.close() 
    elif classnum == 2:
        _classes = classes
        for year,image_set in sets:
        	test_dir(path+'labels/')
        	image_ids = open(path+'ImageSets/Main1/'+image_set+'.txt').read().strip().split()
        	list_file = open('%s%s_%s.txt'%(path,year, image_set), 'w+')
        	save_path_xml = path + 'labels/' + image_set + '/'
        	test_dir(save_path_xml)
        	save_img_path = path+'images/' + image_set + '/'
        	test_dir(save_img_path)
        	for image_id in image_ids:
        		list_file.write(path+'JPEGImages/%s.jpg\n'%(image_id))
        		convert_annotation(path,image_id,_classes,save_path_xml,save_img_path,classnum)
        		print('create_label'+image_id+'Done!')
        	list_file.close() 

 
if __name__ == '__main__':
    
    xmlpath = 'Annotations/'
    jpgpath = 'JPEGImages/'
    localpath = os.getcwd() + '/'
    voc_label(localpath,2)
#    create_database(xmlpath,jpgpath,localpath)
