def invisible(text):
    binary = ''.join(format(ord(c), '08b') for c in text)
    invisible = binary.replace('0', '\u200b').replace('1', '\u200c')
    return invisible
def visible(invisible_text):
    filtered = ''.join(ch for ch in invisible_text if ch in ['\u200b', '\u200c'])
    binary = filtered.replace('\u200b', '0').replace('\u200c', '1')
    length = len(binary)
    if length % 8 != 0:
        binary = binary[:length - (length % 8)]
    chars = [chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
    return ''.join(chars)


