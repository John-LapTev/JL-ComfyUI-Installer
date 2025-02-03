# JL ComfyUI Installer Wiki

[English](#english) | [Русский](#russian)

## English

### Installation Process Details

#### 1. Initial Setup
When you run `JL_install_ComfyUI.bat`, the installer:
- Downloads portable Git
- Downloads portable Python 3.11.9
- Sets up Python environment
- Downloads the setup script

#### 2. System Detection
The installer automatically detects:
- Operating system (Windows/Linux)
- GPU type (NVIDIA/AMD/Intel)
- Available RAM

#### 3. Installation Steps
After detection, it:
- Creates necessary folders structure
- Installs correct PyTorch version
- Clones ComfyUI repository
- Installs ComfyUI Manager
- Creates launch script

### Folder Structure
After installation:
```
📁 Your_Installation_Folder
 ├── 📁 python_embeded (portable Python)
 ├── 📁 git (portable Git)
 ├── 📁 models
 │   ├── 📁 checkpoints
 │   ├── 📁 vae
 │   └── 📁 loras
 ├── 📁 custom_nodes
 │   └── 📁 comfyui-manager
 └── 📄 run_comfyui.bat
```

### Known Issues
1. If you get "Access Denied":
   - Run as administrator
   - Check antivirus
2. If PyTorch installation fails:
   - Check internet connection
   - Try running installer again

## Russian

### Детали процесса установки

#### 1. Начальная настройка
При запуске `JL_install_ComfyUI.bat` установщик:
- Скачивает портативный Git
- Скачивает портативный Python 3.11.9
- Настраивает окружение Python
- Загружает скрипт установки

#### 2. Определение системы
Установщик автоматически определяет:
- Операционную систему (Windows/Linux)
- Тип видеокарты (NVIDIA/AMD/Intel)
- Доступную оперативную память

#### 3. Этапы установки
После определения:
- Создаёт структуру папок
- Устанавливает нужную версию PyTorch
- Клонирует репозиторий ComfyUI
- Устанавливает ComfyUI Manager
- Создаёт скрипт запуска

### Структура папок
После установки:
```
📁 Папка_Установки
 ├── 📁 python_embeded (портативный Python)
 ├── 📁 git (портативный Git)
 ├── 📁 models
 │   ├── 📁 checkpoints
 │   ├── 📁 vae
 │   └── 📁 loras
 ├── 📁 custom_nodes
 │   └── 📁 comfyui-manager
 └── 📄 run_comfyui.bat
```

### Известные проблемы
1. Если появляется "Отказано в доступе":
   - Запустите от имени администратора
   - Проверьте антивирус
2. Если не устанавливается PyTorch:
   - Проверьте интернет-соединение
   - Попробуйте запустить установщик ещё раз