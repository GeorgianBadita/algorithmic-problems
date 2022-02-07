#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
import random
from string import ascii_letters, digits


class Codec:
    def __init__(self):
        self.__hashes = {}
        self.__candidates = ascii_letters + digits
        self.__encoding_size = 6

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        encoding = self.__encode()
        self.__hashes[encoding] = longUrl
        return f"http://tinyurl.com/{encoding}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        encoding = shortUrl.split('/')[-1]
        return self.__hashes[encoding]

    def __encode(self):
        encoding = "".join(random.choices(
            self.__candidates, k=self.__encoding_size))
        while encoding in self.__hashes:
            encoding = "".join(random.choices(
                self.__candidates, k=self.__encoding_size))
        return encoding


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
