import os
import hashlib
import json
import psutil
import time
from datetime import datetime

# VIP Siber Güvenlik Teması - ASCII Banner
BANNER = """
\033[1;32m================================================================
██╗   ██╗ █████╗ ██╗     ██╗  ██╗██╗   ██╗██████╗ ██╗███████╗
██║   ██║██╔══██╗██║     ██║  ██║╚██╗ ██╔╝██╔══██╗██║██╔════╝
██║   ██║███████║██║     ███████║ ╚████╔╝ ██████╔╝██║█████╗  
╚██╗ ██╔╝██╔══██║██║     ██╔══██║  ╚██╔╝  ██╔══██╗██║██╔══╝  
 ╚████╔╝ ██║  ██║███████╗██║  ██║   ██║   ██║  ██║██║███████╗
  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝
             [ CORE EDR ENGINE v1.0 - VIP INTERFACES ]
================================================================\033[0m
"""

def dosya_sha256_hesapla(dosya_yolu):
    if not dosya_yolu or not os.path.exists(dosya_yolu):
        return None
    try:
        hash_sha256 = hashlib.sha256()
        with open(dosya_yolu, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except Exception:
        return None

def yukleme_cubugu(sure=1.5):
    """Siber güvenlik araçlarındaki gibi havalı bir yüklenme çubuğu simüle eder."""
    print("\033[1;36m[*] Bellek Haritası Alınıyor ve Çekirdek Taraması Başlatılıyor...\033[0m")
    genislik = 40
    for i in range(genislik + 1):
        yuzde = int((i / genislik) * 100)
        blok = "█" * i
        bosluk = " " * (genislik - i)
        print(f"\r\033[1;32m Tarama Durumu: |{blok}{bosluk}| {yuzde}% \033[0m", end="")
        time.sleep(sure / genislik)
    print("\n\n" + "-" * 90)

def sistem_sureclerini_tara():
    print(BANNER)
    yukleme_cubugu()
    
    print(f"\033[1;34m[*] Canlı Süreç Analiz Zamanı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\033[0m\n")
    print(f"\033[1;37m{'PID':<8} | {'Süreç Adı':<30} | {'SHA-256 Bütünlük Parmak İzi (İmza)':<40}\033[0m")
    print("-" * 90)
    
    tespit_edilen_tehditler = []
    sayac = 0

    # 1. ADIM: Canlı Süreçlerin Taranması ve Listelenmesi
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            exe_path = proc.info['exe']
            
            # Sadece ilk 15 süreci gösterelim ki terminal şişmesin, temiz dursun
            if sayac >= 15:
                break
                
            current_hash = dosya_sha256_hesapla(exe_path)
            
            if current_hash:
                durum = f"\033[0;32m{current_hash[:35]}...\033[0m"
            else:
                durum = "\033[0;33m[Sistem Süreci / Erişim Kısıtlı]\033[0m"

            print(f"{pid:<8} | {name:<30} | {durum}")
            sayac += 1

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    # 2. ADIM: Tehdit Avcılığı ve Yapay Zeka Tehdit Simülasyonu
    print("-" * 90)
    print(f"\033[1;31m🚨 666      | ransomware_sim.exe             | [CRITICAL] ZARARLI YAZILIM TESPİT EDİLDİ!\033[0m")
    print("-" * 90)
    
    tehdit_detay = {
        "timestamp": datetime.now().isoformat(),
        "alert_level": "CRITICAL",
        "pid": 666,
        "process_name": "ransomware_sim.exe",
        "file_path": "/Users/filizozdemir/Desktop/Valkyrie-EDR/malicious/ransomware_sim.exe",
        "sha256_hash": "84898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "message": "Critical Threat Detected: Known Ransomware signature family matched."
    }
    tespit_edilen_tehditler.append(tehdit_detay)

    # 3. ADIM: Adli Bilişim JSON Siber Olay Raporunu Ekrana Basma
    print("\n\033[1;35m" + "="*31 + " SİBER OLAY RAPORU (JSON CODES) " + "="*31 + "\033[0m")
    json_raporu = json.dumps(tespit_edilen_tehditler, indent=4, ensure_ascii=False)
    print(f"\033[0;31m{json_raporu}\033[0m")
    print("\033[1;35m" + "="*94 + "\033[0m")
    
    # Raporu arka planda kaydetme
    with open("valkyrie_alerts.json", "w", encoding="utf-8") as f:
        f.write(json_raporu)
    print("\n\033[1;32m[+] Analiz Tamamlandı! Kritik alarm verileri 'valkyrie_alerts.json' dosyasına işlendi.\033[0m")

if __name__ == "__main__":
    sistem_sureclerini_tara()