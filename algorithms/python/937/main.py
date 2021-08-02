class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digit = [], []
        logs = list(reversed(logs))
        while logs:
            log = logs.pop()
            if (log.split()[1]).isdigit():
                digit.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digit
