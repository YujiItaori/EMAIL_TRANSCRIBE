import re
from nameparser import HumanName

def parse_emails(email):
    local, domain = email.split("@")
    parts = re.split(r"[._]", local)
    name_str = " ".join(parts)
    name = str(HumanName(name_str).first)
    return name, domain
