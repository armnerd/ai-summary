#  SD、ComfyUI 与自媒体

## 0. 模型下载

> stable-diffusion

```bash
https://huggingface.co/runwayml/stable-diffusion-v1-5
https://hf-mirror.com/runwayml/stable-diffusion-v1-5/blob/main/v1-5-pruned-emaonly.ckpt
```

## 1. stable-diffusion-webui

```bash
// Clone the repository
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git

// Models
models/Stable-diffusion/*.ckpt

// Run
cd stable-diffusion-webui && python webui.py
```

## 2. ComfyUI

### 2.1 安装

```bash
// source
https://www.comfy.org

// Clone the repository
git clone git@github.com:comfyanonymous/ComfyUI.git

// Create an environment with Conda
conda create -n comfyenv
conda activate comfyenv

// Install GPU Dependencies
conda install pytorch-nightly::pytorch torchvision torchaudio -c pytorch-nightly

// Install pip requirements
cd ComfyUI
pip install -r requirements.txt

// Models
models/checkpoints/*.ckpt

// Start the application
cd ComfyUI
python main.py
```

### 2.2 管理器

### 2.3 模版

## 3. civitai

* Model anf LoRA
* https://civitai.com

## 4. 自媒体

* 甄子丹鬼畜动作 [ undo ]
* 蒙娜丽莎唱歌 [ LivePortrait, MuseTalk ]
* 视频卡通风格 [ undo ]
* 孙悟空变声 [ undo ]

### 4.1 LivePortrait

> 面部图片a + 面部动作视频b = a 按照 b 的动作生成视频

https://huggingface.co/spaces/KwaiVGI/LivePortrait

### 4.2 MuseTalk

> 嘴形生成

https://huggingface.co/spaces/TMElyralab/MuseTalk
