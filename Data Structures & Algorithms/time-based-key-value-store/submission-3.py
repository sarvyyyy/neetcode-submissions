class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [(value,timestamp)]
        else:
            self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        sf = float('-inf')
        v = ''
        if key not in self.d:
            return ""

        l = 0
        r = len(self.d[key]) - 1
        while l<=r:
            m = (l+r) // 2
            values = self.d[key][m]
            val = values[1]
            if val <= timestamp:
                sf = val
                v = values[0]
                l = m + 1
            else:
                r = m - 1
                
        if sf == float('-inf'):
            return ""
        else:
            return v
