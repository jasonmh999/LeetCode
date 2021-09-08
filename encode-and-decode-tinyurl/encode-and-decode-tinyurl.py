"""
Time: O(1)
Space: O(N)
"""
class Codec:
    
    def __init__(self):
        self.memo = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hashcode=hash(longUrl)
        self.memo[hashcode]=longUrl
        return hashcode
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.memo[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))