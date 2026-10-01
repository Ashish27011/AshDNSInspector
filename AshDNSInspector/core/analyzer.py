
def analyzer_dns(type_result): 

    type_list = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]
    type_count_result = { }
    try:

        for type_checks in type_list:
            records = type_result.get(type_checks, [])
            type_count_result[type_checks] = 0
            for count in records:
                type_count_result[type_checks] += 1

    except Exception as e:
        print("ERROR OCCURE!", e) 

    return type_count_result       
  