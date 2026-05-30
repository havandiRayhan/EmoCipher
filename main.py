# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.clipboard import Clipboard
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.lang import Builder
import platform
import os

# ── Font emoji sesuai OS ──
try:
    if platform.system() == 'Windows':
        LabelBase.register('EmojiFont', 'C:/Windows/Fonts/seguiemj.ttf')
    elif platform.system() == 'Darwin':
        LabelBase.register('EmojiFont', '/System/Library/Fonts/Apple Color Emoji.ttc')
    else:
        # Mencoba load font Noto Linux/Android
        LabelBase.register('EmojiFont', '/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf')
except Exception:
    # Jika gagal (seperti di beberapa HP Android), gunakan font default agar tidak crash
    LabelBase.register('EmojiFont', DEFAULT_FONT)

# ── Font playful untuk UI ──
# Pastikan nama file cocok persis dengan yang ada di folder
if os.path.exists('Fredoka-Regular.ttf'):
    LabelBase.register('AppFont', 'Fredoka-Regular.ttf')
else:
    # Fallback yang benar: gunakan DEFAULT_FONT bawaan Kivy yang aman
    LabelBase.register('AppFont', DEFAULT_FONT)

Builder.load_file('emoji_cipher.kv')

from cipher import encode, decode


class CipherLayout(BoxLayout):

    def encode_text(self):
        input_text = self.ids.input_field.text.strip()
        if not input_text:
            self.set_status("Masukkan teks terlebih dahulu!", error=True)
            return
        self.ids.output_field.text = encode(input_text)
        self.set_status("Teks berhasil diubah ke emoji!")

    def decode_text(self):
        input_text = self.ids.input_field.text.strip()
        if not input_text:
            self.set_status("Masukkan emoji terlebih dahulu!", error=True)
            return
        self.ids.output_field.text = decode(input_text)
        self.set_status("Emoji berhasil dikembalikan ke teks!")

    def copy_output(self):
        output = self.ids.output_field.text
        if not output:
            self.set_status("Belum ada hasil untuk disalin.", error=True)
            return
        Clipboard.copy(output)
        self.set_status("Hasil disalin ke clipboard!")

    def paste_input(self):
        pasted = Clipboard.paste()
        if pasted:
            self.ids.input_field.text = pasted
            self.set_status("Teks ditempel dari clipboard!")
        else:
            self.set_status("Clipboard kosong.", error=True)

    def clear_all(self):
        self.ids.input_field.text = ''
        self.ids.output_field.text = ''
        self.ids.status_label.text = ''

    def set_status(self, message, error=False):
        label = self.ids.status_label
        label.text = message
        label.color = (1, 0.4, 0.4, 1) if error else (0.58, 0.43, 0.95, 1)


class EmoCipherApp(App):
    def build(self):
        self.title = 'EmoChiper'
        return CipherLayout()


if __name__ == '__main__':
    EmoCipherApp().run()