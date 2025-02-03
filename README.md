# JL ComfyUI Installer

[English](#english) | [Русский](#russian)

## English

### JL ComfyUI Installer
Created by John LapTev
https://github.com/John-LapTev

Easy ComfyUI installer with portable Python and automatic GPU detection.

### Description
JL ComfyUI Installer provides:
- Automatic portable Python 3.11.9 setup
- GPU detection (NVIDIA/AMD/Intel)
- Correct PyTorch version installation
- ComfyUI with manager installation
- All necessary folders creation
- Launch script with correct parameters

### Installation
1. Download `JL_install_ComfyUI.bat`
2. Run it as administrator
3. Wait for installation to complete
4. Use `run_comfyui.bat` to launch

### System Requirements
- Windows 10/11
- 8GB RAM minimum (16GB recommended)
- DirectX 12 capable GPU
- Internet connection

### Supported GPUs
- NVIDIA GPUs (CUDA)
- AMD GPUs (DirectML on Windows, ROCm on Linux)
- Intel GPUs (XPU)

### FAQ

#### Q: Do I need to have Python installed?
A: No, the installer includes portable Python.

#### Q: Will it work with my GPU?
A: Yes, the installer automatically detects your GPU and installs the correct version.

#### Q: What if I get an error during installation?
A: Create an issue in this repository with error details.

## Russian

### JL ComfyUI Installer
Автор: John LapTev
https://github.com/John-LapTev

Простой установщик ComfyUI с портативным Python и автоматическим определением GPU.

### Описание
JL ComfyUI Installer предоставляет:
- Автоматическую настройку портативного Python 3.11.9
- Определение GPU (NVIDIA/AMD/Intel)
- Установку правильной версии PyTorch
- Установку ComfyUI с менеджером
- Создание всех необходимых папок
- Скрипт запуска с нужными параметрами

### Установка
1. Скачайте `JL_install_ComfyUI.bat`
2. Запустите от имени администратора
3. Дождитесь завершения установки
4. Используйте `run_comfyui.bat` для запуска

### Системные требования
- Windows 10/11
- Минимум 8GB RAM (рекомендуется 16GB)
- Видеокарта с поддержкой DirectX 12
- Доступ в интернет

### Поддерживаемые GPU
- NVIDIA видеокарты (CUDA)
- AMD видеокарты (DirectML для Windows, ROCm для Linux)
- Intel видеокарты (XPU)

### Частые вопросы

#### В: Нужно ли устанавливать Python?
О: Нет, установщик включает портативную версию Python.

#### В: Будет ли работать с моей видеокартой?
О: Да, установщик автоматически определяет вашу видеокарту и устанавливает правильную версию.

#### В: Что делать если возникла ошибка при установке?
О: Создайте issue в этом репозитории с описанием ошибки.

## License
[MIT License](LICENSE)