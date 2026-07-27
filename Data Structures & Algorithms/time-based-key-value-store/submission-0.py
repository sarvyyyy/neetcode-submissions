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
            
        for values in self.d[key]:
            val = values[1]
            if val <= timestamp:
                if val > sf:
                    sf = val
                    v = values[0]
                
        if sf == float('-inf'):
            return ""
        else:
            return v
