from collections import Counter


# T: O(len(letters) + len(message) + len(alphabet)) = O(m + n)
# S: O(2 * len(alphabet)) = O(1)
class Solution(object):
    def _to_dict(self, text):
        if not text:
            return None
        return dict(Counter(text.lower()))

    def can_spell(self, msg, letters):
        if not msg:
            return True
        if not letters:
            return False
        if len(msg) > len(letters):
            return False
        msg_char_count = self._to_dict(msg)
        letter_char_count = self._to_dict(letters)
        for key in msg_char_count.keys():
            if not (key in letter_char_count.keys() and msg_char_count.get(key) <= letter_char_count.get(key)):
                return False
        return True


print(Solution().can_spell('bed', 'ABCED'))
print(Solution().can_spell('cat', 'ABCED'))
