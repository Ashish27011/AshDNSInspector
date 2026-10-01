import dns.resolver

def resolve_dns(domain):

    type_list = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]
    type_result = {}

    for record_type in type_list: 
     type_result[record_type] = [ ]
     try:
        dns_builder = dns.resolver.resolve(domain, record_type)
        for result in dns_builder:
         type_result[record_type].append(str(result))

     except Exception:
       print("ERROR OCCURE!")

    return type_result      