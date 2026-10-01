def show_report(domain, type_result, type_count_result, type_discorv):

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

       print("-"*130)
       print("**DOMAIN**")
       print("")
       print("Domain Name".ljust(19),":", domain)
       print("")

       for type_rocord, message in messages.items():
           print("-"*130)
           print("**",message,"**")
           print("")
           record_result = type_result.get(type_rocord, "No records found")
           valid_result = ", ".join(str(r) for r in record_result)
           print(message.ljust(19),":",valid_result)
           print("")
    except Exception as e:
        print("ERROR OCCURE!", e)     

    try:
        print("-"*140)
        print("       DNS ANALYSIS")  
        print("-"*140)
        print("")
        for type in type_list:
            type_ans = type_discorv.get(type)
            print(type_ans)
        print("")
    except Exception as e:
        print("ERROR OCCURE!", e)       

    try:

        print("-"*140)
        print("       SUMMARY")  
        print("-"*140)        
        print("")
        for types, counts in type_info.items():
            final_result = type_count_result.get(types, "0")
            print(counts.ljust(19),":", final_result)

    except Exception as e:
        print("ERROR OCCURE!", e)        
    