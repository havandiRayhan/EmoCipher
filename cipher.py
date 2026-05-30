# cipher.py
# Logika utama untuk mengubah teks ke emoji dan sebaliknya

EMOJI_MAP = {
    'a': '🍎', 'b': '🐝', 'c': '🎪', 'd': '💎', 'e': '🌍',
    'f': '🔥', 'g': '🍇', 'h': '🏠', 'i': '🍦', 'j': '🎷',
    'k': '🔑', 'l': '🍋', 'm': '🌊', 'n': '🌙', 'o': '🍊',
    'p': '🐼', 'q': '👑', 'r': '🌹', 's': '⭐', 't': '🌴',
    'u': '🦄', 'v': '🎻', 'w': '🍉', 'x': '❌', 'y': '🌻',
    'z': '⚡', ' ': '⬜', '0': '🌑', '1': '🌟', '2': '🌺',
    '3': '🎯', '4': '🎲', '5': '🏆', '6': '🎭', '7': '🎸',
    '8': '🎱', '9': '🎰', '.': '🔹', ',': '🔸', '?': '❓',
    '!': '❗', "'": '🔖'
}

# Balik kamus: emoji → huruf (untuk decode)
REVERSE_MAP = {v: k for k, v in EMOJI_MAP.items()}


def encode(text: str) -> str:
    """Mengubah teks biasa menjadi emoji.
    Huruf yang tidak ada di kamus akan dibiarkan apa adanya.
    """
    result = ''
    for char in text.lower():
        result += EMOJI_MAP.get(char, char)
    return result


def decode(emoji_text: str) -> str:
    """Mengubah emoji kembali menjadi teks biasa.
    Emoji yang tidak dikenal akan dibiarkan apa adanya.
    """
    result = ''
    for char in emoji_text:
        result += REVERSE_MAP.get(char, char)
    return result


# ─── Test sederhana (jalankan file ini langsung untuk coba) ───
if __name__ == '__main__':
    pesan_asli = "halo dunia!"
    encoded = encode(pesan_asli)
    decoded = decode(encoded)

    print(f"Asli   : {pesan_asli}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Berhasil: {pesan_asli == decoded}")