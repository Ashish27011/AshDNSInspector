from banners import banner
from core import validator
from core import resolver
from core import analyzer
from core import filters
from core import reporter
from outputs import writeup

domain = validator.domain_validate()
banner.s_banner()
print("")
type_result = resolver.resolve_dns(domain)
type_count_result = analyzer.analyzer_dns(type_result)
type_discorv = filters.show_filter(type_count_result)
reporter.show_report(domain, type_result, type_count_result, type_discorv)
writeup.show_writeup(domain, type_result, type_count_result, type_discorv)
print("")
banner.e_banner()