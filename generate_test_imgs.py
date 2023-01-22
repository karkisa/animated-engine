import cv2
import matplotlib.pyplot as plt
import pdb,os,shutil
import numpy as np

def get_name_extention(path):
    path=path.split('/')
    s=path[-1]
    s = s.split('.')
    return s[0]

def read_vid_and_save_in_folder(vid_path,save_parent_folder = '/nfs/hpc/share/karkisa/AI cap/sturdy-eureka/yolo_training_data/test_data/210914'):
    vid_ca = cv2.VideoCapture(vid_path)
    extention = get_name_extention(vid_path)
    save_folder =save_parent_folder + '/' + extention
    os.mkdir(save_folder)
    count = 0
    time_skips = 3000             # fps is 29.9 .i.e almost 30
    while vid_ca.isOpened():
        count+=1
        t_msec = 1000*(count)
        vid_ca.set(cv2.CAP_PROP_POS_MSEC, t_msec)
        ret, frame = vid_ca.read()
        name = str(count)+'_'+ extention +'.png'
        if ret :

            cv2.imwrite(save_folder+'/'+name,frame)
            if count%60==0:
                print("frames saved so far: ",count )

            # if count ==10: break

        else : break

def get_vid_paths(folder_path):
    vid_paths = [os.path.join(folder_path,path) for path in os.listdir(folder_path)]
    return vid_paths

def get_save_folder(vid_folder, save_base_folder_path):
    folder_name = vid_folder.split('/')[-1]
    save_path = os.path.join(save_base_folder_path, folder_name)
    return save_path

def main():
    base_vid_folder_path = 'vid'   # folder containg folders that have vidoes in them
    save_path_base_folder = 'test_folder'  # folder to save the frames according to vid folder hirarchy
    os.mkdir(save_path_base_folder)
    #get list of paths for each folder in video base folder
    vid_folders = [os.path.join(base_vid_folder_path,paths) for paths in os.listdir(base_vid_folder_path)]

    #for each video folder in vid base folder
    #   get video paths for videos in that folder
    #   get save path/destination for saving the frames
    #   for each vid in the video folder read the vid and save the frames

    for vid_folder in vid_folders:
        # get the paths tot the vidoes in that folder
        vid_paths = get_vid_paths(vid_folder)
        save_folder_path = get_save_folder(vid_folder,save_path_base_folder)
        os.mkdir(save_folder_path)
        for vid_path in vid_paths:
            read_vid_and_save_in_folder(vid_path,save_folder_path)
    return
    
if __name__ == '__main__':
    main()