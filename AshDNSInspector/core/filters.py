def show_filter(type_count_result):

    messages = {
        "A": "IPv4 address discovered",
        "AAAA": "IPv6 address discovered",
        "MX": "MX mail servers discovered",
        "NS": "NS authoritative name servers discovered",
        "TXT": "TXT records discovered",
    }
    type_discorv = {}
    try:
        for record_type, message in messages.items():
            count_records = type_count_result.get(record_type, 0)
            if count_records > 0:
                type_discorv[record_type] = f"[+] {count_records} {message}"
    except Exception as e:
        print("ERROR OCCURRED!", e)

    return type_discorv



                        
