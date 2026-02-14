def analyze_error(title, description):
    text = (title + " " + description).lower()

    if "null" in text:
        return (
            "Bir nesne None olduğu halde kullanılmaya çalışılmış olabilir.",
            "Null kontrolü ekleyin veya varsayılan değer atayın."
        )

    if "timeout" in text:
        return (
            "Sunucu veya veritabanı yanıt süresi aşılmış.",
            "Query optimize edin veya timeout süresini artırın."
        )

    if "database" in text:
        return (
            "Veritabanı bağlantı problemi olabilir.",
            "Connection string ve DB servis durumunu kontrol edin."
        )

    if "permission" in text:
        return (
            "Yetkisiz erişim denemesi yapılmış olabilir.",
            "Rol ve yetki ayarlarını kontrol edin."
        )

    if "memory" in text:
        return (
            "Bellek sızıntısı olabilir.",
            "Nesne yönetimi ve garbage collection kontrol edilmeli."
        )

    return (
        "Otomatik analiz net sebep bulamadı.",
        "Logları manuel inceleyin."
    )
