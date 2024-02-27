
# Mcships database in Pascal-VOC


The code was written by [Yitong-Zheng](2016100530@mail.nwpu.edu.cn)

If you use this code for your research, please cite:

Y. Zheng and S. Zhang, "Mcships: A Large-Scale Ship Dataset For Detection And Fine-Grained Categorization In The Wild," 2020 IEEE International Conference on Multimedia and Expo (ICME), London, United Kingdom, 2020, pp. 1-6, doi: 10.1109/ICME46284.2020.9102907.


## Prerequisites
- Linux or macOS
- Python 3
- CPU or NVIDIA GPU + CUDA CuDNN

## Getting Started
### Installation

- Install [CUDA](https://developer.nvidia.com/zh-cn/cuda-downloads) and [CUDNN](https://developer.nvidia.com/rdp/cudnn-archive)

- Download [Yolov5](https://github.com/topics/yolov5)

- Download [Mcships_database_lite(BaiduYun)](https://pan.baidu.com/s/1rDeiCPX4EdRUvBl5jnWqDQ)  password: dqwu or
  [Mcships_database_lite(GoogleDrive)](https://drive.google.com/file/d/1udewXbHCS9WKM-MPpWqouUUGs6Vx5iWf/view?usp=sharing)

### Mcship train/test
- Download a Mcship dataset (e.g. maps):

- Trans the dataset into yolo format:
```
python voc2yolo.py
```
- Mcships_database_lite contains 9000 imgs/annotations in Pascal-VOC

- Mcships_satellite_database_lite contains 800 imgs/annotations in Pascal-VOC

- Train/Val/Test/Trainval imgs are listed in .ImageSet/Main/*

## Citation
If you use this code for your research, please cite our papers.
```
@INPROCEEDINGS{Mcships2020 ,
  author={Y. {Zheng} and S. {Zhang}},
  booktitle={2020 IEEE International Conference on Multimedia and Expo (ICME)}, 
  title={Mcships: A Large-Scale Ship Dataset For Detection And Fine-Grained Categorization In The Wild}, 
  year={2020},
  volume={},
  number={},
  pages={1-6},
  doi={10.1109/ICME46284.2020.9102907}
}

```
