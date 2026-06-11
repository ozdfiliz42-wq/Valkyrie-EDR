# 🛡️ VALKYRIE-EDR: Çekirdek Düzeyde Süreç ve Bütünlük İzleme Sistemi

## 1. Proje Hakkında (Özet)
Valkyrie-EDR; uç noktalarda (Endpoint) çalışan canlı süreçleri (Processes) izlemek, bu süreçlerin yürütülebilir dosyalarının dijital parmak izlerini (SHA-256) hesaplamak ve bilinen tehdit istihbaratı veri tabanlarıyla karşılaştırarak analiz etmek üzere geliştirilmiş hafif düzey bir **EDR (Endpoint Detection and Response)** çekirdeğidir. Ostim Teknik University Bilgi Güvenliği Teknolojisi ders projesi kapsamında geliştirilmiştir.

## 2. Mimari ve Çalışma Mantığı
1. **Süreç Keşif Katmanı:** `psutil` kütüphanesi kullanılarak işletim sistemi üzerinde o an aktif olan tüm canlı süreçlerin ID (PID) ve isim bilgileri anlık olarak yakalanır.
2. **Kriptografik Bütünlük Doğrulama:** Yakalanan süreçlerin çalıştırılabilir dosyaları `hashlib` üzerinden **SHA-256** algoritması ile taranarak benzersiz dijital imzası oluşturulur.
3. **Tehdit İstihbaratı ve Raporlama:** Elde edilen hash değerleri zararlı imza veri tabanlarıyla karşılaştırılır. Eşleşme durumunda kurumsal siber olay müdahale standartlarına uygun **JSON formatında** adli bilişim raporu üretilir.

## 3. Sistem Çıktısı ve Adli Bilişim Günlüğü (SIEM Log)
EDR motorunun simüle edilen zararlı yazılımı (`ransomware_sim.exe`) yakaladığı an ürettiği ve otomatik olarak `valkyrie_alerts.json` dosyasına kaydettiği kurumsal siber olay alarm log yapısı:

```json
[
    {
        "timestamp": "2026-06-12T01:06:41.171032",
        "alert_level": "CRITICAL",
        "pid": 666,
        "process_name": "ransomware_sim.exe",
        "file_path": "/Users/filizozdemir/Desktop/Valkyrie-EDR/malicious/ransomware_sim.exe",
        "sha256_hash": "84898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "message": "Critical Threat Detected: Known Ransomware signature family matched."
    }
]
