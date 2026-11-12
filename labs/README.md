> kkghrsbsb 2026.11.12

## 如何开始

创建两个环境

```bash
conda create -n rl-labs python=3.10
conda create -n lerobot-labs python=3.12
```

### 1. `rl-labs`：Lab01–Lab11

```bash
conda activate rl-labs
```

先安装基础包和 Notebook 内核：

```bash
python -m pip install numpy matplotlib ipykernel jupyterlab ipywidgets "gymnasium[classic-control,toy-text]==0.29.1"
```

安装 PyTorch 和 torchvision，供 Lab06、Lab09 等使用：

```bash
python -m pip install torch torchvision
```

Lab08 的 Atari 和 TorchRL 依赖：

```bash
python -m pip install "gymnasium[atari,accept-rom-license]==0.29.1" "autorom[accept-rom-license]" ale-py torchrl opencv-python imageio
```

Lab10 和 Lab11 的 MuJoCo、Stable-Baselines3 依赖：

```bash
python -m pip install "gymnasium[mujoco]==0.29.1" "stable-baselines3[extra]"
```

### 2. `lerobot-labs`：Lab12–Lab14

```bash
conda activate lerobot-labs
```

安装基础包和 Notebook 内核：

```bash
python -m pip install ipykernel jupyterlab matplotlib pillow
```

安装 PyTorch、LeRobot 数据集和 SmolVLA 依赖：

```bash
python -m pip install torch torchvision "lerobot[dataset,smolvla]"
```

**关于 GPU：** 上面的 PyTorch 命令没有指定 CUDA 软件包来源。`labs` 中针对 Lab08 和 Lab13 分别写了不同的 CUDA 安装示例；如果你打算使用 NVIDIA GPU，建议先确定显卡和驱动情况，再选择对应的 PyTorch 安装命令。否则需要尝试 CPU 运行。

在 VS Code 或 Jupyter 中打开 Notebook 后，选择对应 Conda 环境的 Python 内核即可。Lab12–14 首次运行还可能需要下载数据集或预训练模型。

```bash
jupyter lab
```
