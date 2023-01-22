import os

def get_results_folder_path(path,results_main_folder):
    folder_name = path.split('/')[-1]
    result_path = results_main_folder+'/'+folder_name
    return result_path

def write_test_sh_file(main_folders,test_sh_path,results_main_folder):
    f  = open(test_sh_path,'w')
    # pdb.set_trace()
    for main_folder in main_folders:
        results_folder_path = get_results_folder_path(main_folder,results_main_folder)
        # os.mkdir(results_folder_path)
        sub_folders = [os.path.join(main_folder,p) for p in os.listdir(main_folder)]
        for sub_folder_path in sub_folders:
            f.write('python detect.py --weights /nfs/hpc/share/karkisa/AI_Cap/yolov5/runs/train/exp3/weights/best.pt ')
            f.write(f'--source {sub_folder_path} ')
            f.write(f'--project {results_folder_path} ')
            f.write('--nosave  --save-crop  --conf-thres 0.75 \n')

    f.close()

def main():
    test_sh_path = 'test.sh'
    main_folder = 'test_folder'
    main_folders = [os.path.join(main_folder,p) for p in os.listdir(main_folder)]
    results_main_folder = 'results'
    os.mkdir(results_main_folder)
    write_test_sh_file(main_folders,test_sh_path,results_main_folder)
    

    return


if __name__ == "__main__":
    main()
