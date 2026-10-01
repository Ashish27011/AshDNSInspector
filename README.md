# AshDNSInspector

AshDNSInspector is a Python-based DNS reconnaissance and inspection tool designed to query, analyze, and report DNS records for a given domain.

The project was built as a practical cybersecurity learning project to understand DNS resolution, different DNS record types, Python DNS libraries, modular architecture, and structured reconnaissance reporting.

---

## Features

- Domain validation
- DNS record enumeration
- IPv4 (A) record lookup
- IPv6 (AAAA) record lookup
- CNAME record lookup
- MX mail server lookup
- NS authoritative name server lookup
- TXT record lookup
- DNS record counting and analysis
- Human-readable DNS observations
- Terminal-based reporting
- Automatic report generation
- Modular project architecture
- DNS error handling

---

## DNS Records Supported

| Record | Purpose |
|--------|---------|
| A | IPv4 address |
| AAAA | IPv6 address |
| CNAME | Canonical name / alias |
| MX | Mail exchange servers |
| NS | Authoritative name servers |
| TXT | Text information associated with a domain |

---

## Project Architecture

```text
                         User
                          |
                          v
                    +-----------+
                    | Validator |
                    +-----+-----+
                          |
                          v
                    +-----------+
                    | Resolver  |
                    +-----+-----+
                          |
                 DNS Record Collection
                          |
                          v
                    +-----------+
                    | Analyzer  |
                    +-----+-----+
                          |
                          v
                    +-----------+
                    |  Filters  |
                    +-----+-----+
                          |
                          v
                    +-----------+
                    | Reporter  |
                    +-----+-----+
                          |
                    +-----+-----+
                    |           |
                    v           v
                 Terminal   report.txt
