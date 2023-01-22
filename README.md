# animated-engine
Deployment scripts for whale health

# Instructions 

* Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) 

* Inside cmd or terminal use the following commands

```
conda create –name whales python=3.9
conda activate whales
git clone https://github.com/karkisa/animated-engine.git
cd animated-engine
mkdir vid
```

* Path changes

In file generate_test_sh.py line 25
Change the base_foleder variable and provide the path for the animated-engine folder
Like this : 
```
base_folder = ‘path_to_animated_engine_folder’
```

* Download all the folders of the test videos inside vid folder.
* Download the weight file of the model best.2 inside the animated folder using the command below.
```
wget -o best.pt  https://oregonstate.box.com/shared/static/4bl2pr0xuygbai8gu97hajjs0ihprc7w.pt
```
Folder structure should look like this

    ├── best.pt
    ├── bravo.sh
    ├── generate_test_imgs.py
    ├── generate_test_sh.py
    ├── ignite.sh
    ├── vid
    │   ├── 210716
    │   │   ├── 210716_I2O_S5_U2_DJI0004.MOV
    │   │   ├── 210716_I2O_S5_U2_DJI0005.MOV
    │   │   └── 210716_I2O_S5_U2_DJI0006.MOV
    │   ├── 220524
    │   │   └── 220524_I2O_S1_U2_DJI0005.MOV
    │   ├── 220807
    │   │   ├── 220807_I2F_S2_U1_DJI0001.MOV
    │   │   └── 220807_I2F_S2_U1_DJI0002.MOV


* If you are running this for the first time. Run this 
```
sh ignite.sh 
```

Else 
```
sh bravo.sh
```



