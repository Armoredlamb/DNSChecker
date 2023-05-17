import dns.resolver

def print_dns_records(domain):
    try:
        print(f"MX records for {domain}:")
        try:
            mx_records = dns.resolver.resolve(domain, 'MX')
            if mx_records:
                for mx in mx_records:
                    print(mx.to_text())
                    
        except dns.resolver.NoAnswer:
            print("No MX Records Detected")

        print(f"\nDMARC record for {domain}:")
        try:
            dmarc_record = dns.resolver.resolve(f"_dmarc.{domain}", 'TXT')
            if dmarc_record:
                for record in dmarc_record:
                    print(record.to_text())

        except dns.resolver.NoAnswer:
            print("No DMARC Records Detected")

        print(f"\nTXT records for {domain}, look for v=spf1:")
        try:
            spf_record = dns.resolver.resolve(domain, 'TXT')
            if spf_record:
                for record in spf_record:
                    print(record.to_text())

        except dns.resolver.NoAnswer:
            print("No TXT Records Detected")

        print(f"\nDKIM records for {domain}:")
        try:
            dkim_records = dns.resolver.resolve(f"_domainkey.{domain}", 'TXT')
            if dkim_records:
                for dkim in dkim_records:
                    print(dkim.to_text())

        except dns.resolver.NoAnswer:
            print("No DKIM Records Detected")

    except dns.resolver.NXDOMAIN:
        print("Invalid domain name or DKIM check failed.")
    except dns.exception.DNSException as e:
        print(f"DNS resolution failed: {str(e)}")

domain_name = input("Enter the domain name without www: ")
print_dns_records(domain_name)
