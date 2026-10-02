import json
import os
import platform
import sys

def get_type_os():
    name_os = platform.system()
    if name_os == "Windows":
        return "Windows"
    elif name_os == "Darwin":
        return "MacOS"
    elif name_os == "Linux":
        return "Linux"

def os_parameters(os_type):
    data = {
        "Тип_OS": os_type,
        "Архитектура_процессора": platform.machine(),
        "Логические_ядра_ЦП": os.cpu_count(),
    }
    if os_type == "Windows":
        win_ver = sys.getwindowsversion()
        data["Детальная_информация"] = {
            "Версия_Windows": win_ver.major,
            "Номер сборки": win_ver.build
        }
    elif os_type == "MacOS":
        mac_ver = platform.mac_ver()
        data["Детальная_информация"] = {
            "Версия_MacOS": mac_ver[0] if mac_ver else "Unknown"
        }
    elif os_type == "Linux":
        linux_distro = "Unknown Linux"
        if os.path.exists("/etc/os-release"):
            with open("/etc/os-release", "r") as f:
                for line in f:
                    if line.startswith("PRETTY_NAME="):
                        linux_distro = line.strip().split("=")[1].replace('"', '')
                        break
        data["Детальная_информация"] = {
            "Дистрибутив": linux_distro
        }

    return data

def save_to_json(data, filename="os_info.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Данные успешно сохранены в файл: {filename}")
    except Exception as e:
        print(f"Не удалось записать файл: {e}")

def main():
    os_type = get_type_os()
    os_data = os_parameters(os_type)
    os_data = os_parameters(os_type)
    save_to_json(os_data)

    print(f"Обнаруженная ОС: {os_type}")


if __name__ == "__main__":
    main()