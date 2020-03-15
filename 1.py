from chardet.universaldetector import UniversalDetector

detector = UniversalDetector()
with open('1638125.html', 'rb') as fh:
    for line in fh:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
print(detector.result)