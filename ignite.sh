# conda create --name whales python=3.9
# conda activate whales
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
cd ..
# run use_case_one.py to get the test images 
python generate_test_imgs.py

#create test.sh file
touch test.sh
python generate_test_sh.py

mv test.sh yolov5/test.sh
mkdir yolov5/weights_whale
cp best.pt yolov5/weights_whale/best.pt
# run yolov5  model testing sh for the folders in yolov5 folder
cd yolov5
sh test.sh 