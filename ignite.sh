conda create -name whales python=3.9
conda active whales
git clone https://github.com/ultralytics/yolov5.git
pip install -r requirements.txt
# run use_case_one.py to get the test images 
python generate_test_imgs.py

#create test.sh file
touch test.sh
python generate_test_sh.py

mv test.sh yolov5/test.sh
# run yolov5 model testing sh for the folders in yolov5 folder
cd yolov5
sh test.sh 