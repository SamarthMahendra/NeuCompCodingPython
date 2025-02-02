class ProxyInternet:
    def __init__(self):
        self.blocked_sites = {"banned-site.com", "hacker-site.com"}

    def connect_to(self, website):
        if website in self.blocked_sites:
            print(f"🚫 Access Denied: {website} is blocked!")
        else:
            print(f"✅ Connecting to {website}...")  # Allows access if not blocked
