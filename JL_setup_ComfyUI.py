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
    def __init__(self):
        self.system, self.gpu = self.JL_get_system_info()
        self.comfyui_dir = os.path.join(os.getcwd(), "ComfyUI")
        
        # Создаём основную папку ComfyUI если её нет
        if not os.path.exists(self.comfyui_dir):
            os.makedirs(self.comfyui_dir)

    def JL_get_system_info(self):
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
                    result = subprocess.run(["wmic", "path", "win32_VideoController", "get", "name"], capture_output=True, text=True)
                    output = result.stdout
                    if "AMD" in output or "Radeon" in output:
                        return "Windows", "AMD"
                    elif "Intel" in output:
                        return "Windows", "Intel"
                except:
                    pass
        
        return system, "Unknown"

    def JL_install_pytorch(self):
        print("Установка PyTorch...")
        if self.gpu == "NVIDIA":
            subprocess.run([sys.executable, "-m", "pip", "install", "torch", "torchvision", "torchaudio", 
                        "--index-url", "https://download.pytorch.org/whl/cu121"])
        elif self.system == "Windows" and self.gpu == "AMD":
            subprocess.run([sys.executable, "-m", "pip", "install", "torch-directml"])
        else:
            subprocess.run([sys.executable, "-m", "pip", "install", "torch", "torchvision", "torchaudio"])

    def JL_create_folders(self):
        # Создаём папки внутри ComfyUI
        folders = [
            "models/checkpoints",
            "models/vae",
            "models/vae_approx",
            "models/embeddings",
            "models/loras",
            "models/controlnet",
            "models/clip_vision",
            "custom_nodes",
            "input",
            "output"
        ]
        
        for folder in folders:
            full_path = os.path.join(self.comfyui_dir, folder)
            os.makedirs(full_path, exist_ok=True)

    def JL_install_requirements(self):
        print("Установка базовых зависимостей...")
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
            subprocess.run([sys.executable, "-m", "pip", "install", req, "--no-warn-script-location"])

    def JL_create_launcher(self):
        launcher_path = os.path.join(os.getcwd(), "run_comfyui.bat")
        
        with open(launcher_path, "w") as f:
            f.write("@echo off\n")
            if self.gpu == "AMD":
                f.write("cd ComfyUI\n")
                f.write("..\\python_embeded\\python.exe -s main.py --directml --front-end-version Comfy-Org/ComfyUI_frontend@latest\n")
            else:
                f.write("cd ComfyUI\n")
                f.write("..\\python_embeded\\python.exe -s main.py --front-end-version Comfy-Org/ComfyUI_frontend@latest\n")
            f.write("pause")

    def JL_setup(self):
        print(f"Обнаружена система: {self.system} с GPU: {self.gpu}")
        print(f"Установка будет произведена в: {self.comfyui_dir}")

        # Создаём структуру папок
        self.JL_create_folders()

        # Клонируем ComfyUI
        print("Клонирование ComfyUI...")
        subprocess.run(["git", "clone", "https://github.com/comfyanonymous/ComfyUI.git", "ComfyUI"])

        # Переходим в папку ComfyUI для установки зависимостей
        os.chdir(self.comfyui_dir)

        # Устанавливаем PyTorch и зависимости
        self.JL_install_pytorch()
        self.JL_install_requirements()

        print("Установка ComfyUI Manager...")
        os.makedirs("custom_nodes/comfyui-manager", exist_ok=True)
        subprocess.run(["git", "clone", "https://github.com/ltdrdata/ComfyUI-Manager.git", 
                     "custom_nodes/comfyui-manager"])

        # Возвращаемся в исходную папку для создания launcher
        os.chdir("..")
        self.JL_create_launcher()

        print("\nУстановка завершена!")
        print(f"GPU определён как: {self.gpu}")
        print("Запускайте ComfyUI через run_comfyui.bat")

if __name__ == "__main__":
    installer = JL_ComfyUI_Setup()
    installer.JL_setup()