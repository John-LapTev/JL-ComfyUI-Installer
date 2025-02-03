import os
import sys
import platform
import subprocess
import shutil
from pathlib import Path
import json
import urllib.request
import ssl

# Created by John LapTev
# https://github.com/John-LapTev

class JL_ComfyUI_Setup:
    """
    ComfyUI Setup Class
    Created by John LapTev
    """
    def __init__(self):
        self.system, self.gpu = self.JL_get_system_info()

    def JL_get_system_info(self):
        """Определяет систему и GPU пользователя"""
        system = platform.system()
        if system == "Windows":
            try:
                # Проверяем наличие NVIDIA GPU
                import nvidia_smi
                nvidia_smi.nvmlInit()
                return "Windows", "NVIDIA"
            except:
                try:
                    # Проверяем AMD GPU
                    subprocess.run(["wmic", "path", "win32_VideoController", "get", "name"], capture_output=True)
                    output = subprocess.stdout.decode()
                    if "AMD" in output or "Radeon" in output:
                        return "Windows", "AMD"
                    elif "Intel" in output:
                        return "Windows", "Intel"
                except:
                    pass
        elif system == "Linux":
            try:
                # Проверяем GPU в Linux
                lspci_output = subprocess.run(["lspci"], capture_output=True).stdout.decode()
                if "NVIDIA" in lspci_output:
                    return "Linux", "NVIDIA"
                elif "AMD" in lspci_output or "ATI" in lspci_output:
                    return "Linux", "AMD"
                elif "Intel" in lspci_output:
                    return "Linux", "Intel"
            except:
                pass
        
        return system, "Unknown"

    def JL_install_pytorch(self):
        """Устанавливает PyTorch в зависимости от системы и GPU"""
        if self.gpu == "NVIDIA":
            subprocess.run([sys.executable, "-m", "pip", "install", "torch", "torchvision", "torchaudio", 
                        "--index-url", "https://download.pytorch.org/whl/cu121"])
        elif self.system == "Windows" and self.gpu == "AMD":
            subprocess.run([sys.executable, "-m", "pip", "install", "torch-directml"])
        elif self.system == "Linux" and self.gpu == "AMD":
            subprocess.run([sys.executable, "-m", "pip", "install", "torch", "torchvision", "torchaudio",
                        "--index-url", "https://download.pytorch.org/whl/rocm6.2.4"])
        elif self.gpu == "Intel":
            subprocess.run([sys.executable, "-m", "pip", "install", "--pre", "torch", "torchvision", "torchaudio",
                        "--index-url", "https://download.pytorch.org/whl/nightly/xpu"])
        else:
            subprocess.run([sys.executable, "-m", "pip", "install", "torch", "torchvision", "torchaudio"])

    def JL_create_folders(self):
        """Создаёт необходимые папки"""
        paths = {
            "models/checkpoints": [],
            "models/vae": [],
            "models/vae_approx": [],
            "models/embeddings": [],
            "models/loras": [],
            "models/controlnet": [],
            "models/clip_vision": [],
            "custom_nodes": [],
            "input": [],
            "output": [],
        }

        for path in paths.keys():
            os.makedirs(path, exist_ok=True)

    def JL_install_requirements(self):
        """Устанавливает базовые зависимости"""
        print("Установка базовых зависимостей...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        
        requirements = [
            "numpy==1.24.3",
            "pillow",
            "transformers==4.35.2",
            "safetensors==0.4.1",
            "aiohttp",
            "tqdm",
            "accelerate",
            "gitpython"
        ]
        for req in requirements:
            subprocess.run([sys.executable, "-m", "pip", "install", req])

    def JL_create_launcher(self):
        """Создаёт скрипт запуска"""
        if self.system == "Windows":
            with open("run_comfyui.bat", "w") as f:
                if self.gpu == "AMD":
                    f.write("@echo off\n")
                    f.write(".\\python_embeded\\python.exe -s main.py --directml --front-end-version Comfy-Org/ComfyUI_frontend@latest\n")
                    f.write("pause")
                else:
                    f.write("@echo off\n")
                    f.write(".\\python_embeded\\python.exe -s main.py --front-end-version Comfy-Org/ComfyUI_frontend@latest\n")
                    f.write("pause")
        else:
            with open("run_comfyui.sh", "w") as f:
                if self.gpu == "AMD":
                    f.write("#!/bin/bash\n")
                    f.write("HSA_OVERRIDE_GFX_VERSION=10.3.0 ./python_embeded/python -s main.py --front-end-version Comfy-Org/ComfyUI_frontend@latest\n")
                else:
                    f.write("#!/bin/bash\n")
                    f.write("./python_embeded/python -s main.py --front-end-version Comfy-Org/ComfyUI_frontend@latest\n")
            os.chmod("run_comfyui.sh", 0o755)

    def JL_setup(self):
        """Основная функция установки"""
        print(f"Обнаружена система: {self.system} с GPU: {self.gpu}")

        self.JL_create_folders()
        self.JL_install_pytorch()
        self.JL_install_requirements()

        print("Клонирование ComfyUI...")
        subprocess.run(["git", "clone", "https://github.com/comfyanonymous/ComfyUI.git", "."])

        print("Установка зависимостей ComfyUI...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

        print("Установка ComfyUI Manager...")
        subprocess.run([sys.executable, "-c", 
                    "import git; git.Repo.clone_from('https://github.com/ltdrdata/ComfyUI-Manager', './custom_nodes/comfyui-manager')"])

        self.JL_create_launcher()

        print("\nУстановка завершена!")
        print(f"GPU определён как: {self.gpu}")
        print("Запускайте ComfyUI через run_comfyui.bat" if self.system == "Windows" else "Запускайте ComfyUI через ./run_comfyui.sh")

if __name__ == "__main__":
    installer = JL_ComfyUI_Setup()
    installer.JL_setup()