def show_writeup(domain, type_result, type_count_result, type_discorv):
        file = open("AshDNSInspector/reports/report.txt", "w")
        messages = {
            "A": "IPv4 address",
            "AAAA": "IPv6 address",
            "MX": "MX mail servers",
            "NS": "NS authoritative name servers",
            "TXT": "TXT records",
            }
        type_list = ["A", "AAAA", "MX", "NS", "TXT"]
        type_info = {
            "A": "A Records",
            "AAAA": "AAAA Records",
            "MX": "MX Records",
            "NS": "NS Records",
            "TXT": "TXT records",
            "CNAME": "CNAME Records"
            }
        try:

            file.write("-"*130 + "\n")
            file.write("**DOMAIN**\n")
            file.write("\n")
            file.write("Domain Name".ljust(19) + " : " + domain + "\n")
            file.write("\n")

            for type_rocord, message in messages.items():
                file.write("-"*130 + "\n")
                file.write("**" + message + "**\n")
                file.write("\n")
                record_result = type_result.get(type_rocord, [])
                valid_result = ", ".join(str(r) for r in record_result) or "No records found"
                file.write(message.ljust(19) + " : " + valid_result + "\n")
                file.write("\n")
        except Exception as e:
            file.write("ERROR OCCURE! " + str(e))

        try:

            file.write("-"*140 + "\n")
            file.write("       DNS ANALYSIS\n")
            file.write("-"*140 + "\n")
            file.write("\n")
            for type in type_list:
                type_ans = type_discorv.get(type, "Not found")
                file.write(str(type_ans) + "\n")
            file.write("\n")
        except Exception as e:
            file.write("ERROR OCCURE! " + str(e))

        try:

            file.write("-"*140 + "\n")
            file.write("       SUMMARY\n")
            file.write("-"*140 + "\n")
            file.write("\n")
            for types, counts in type_info.items():
                final_result = type_count_result.get(types, "0")
                file.write(counts.ljust(19) + " : " + str(final_result) + "\n")

        except Exception as e:
            file.write("ERROR OCCURE! " + str(e))

        file.close()       
        