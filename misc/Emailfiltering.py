from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]  # Take the part before the '+'
            local = local.replace('.', '')  # Remove all dots
            res.add(f"{local}@{domain}")
        return len(res)
