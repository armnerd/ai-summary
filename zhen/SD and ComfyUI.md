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
* 蒙娜丽莎唱歌 [ LivePortrait ]
* 视频卡通风格 [ AnimateDiff]
* 孙悟空变声 [ undo ]
* 黏土风格 [ undo ]
* 换脸 [ 剪映 ]

### LivePortrait

https://huggingface.co/KwaiVGI/LivePortrait

### AnimateDiff

https://huggingface.co/ByteDance/AnimateDiff-Lightning
