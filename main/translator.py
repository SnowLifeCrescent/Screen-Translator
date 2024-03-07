import re
import time
import threading
from PyQt5.QtWidgets import QLabel, QWidget
import tesseract_ocr as to
from PyQt_show import TextShow
from translate_shell.translate import translate


class Translator:
    def __init__(self):
        super().__init__()
        self.translation_thread = None
        self.is_translating = False
        self.translation_delay = 2  # 3帧/秒
        self.translations = {}  # 存储翻译文本和位置的字典
        self.translation_labels = {}  # 存储显示翻译文本的 Label
        self.translations = []
        self.positions = []
        self.text_show = TextShow()
        self.tag = False

    def start(self):
        try:
            if self.text_show is None:
                self.text_show = TextShow()
            self.is_translating = True
            if self.translation_thread is None:
                self.translation_thread = threading.Thread(target=self.__translate)
                self.translation_thread.start()
            return None
        except Exception as e:
            print(f"Start translation failed: {e}")

    def stop(self):
        try:
            self.is_translating = False
            if self.translation_thread is not None:
                self.translation_thread.join()
                self.translation_thread = None
            self.text_show.clear_text()
            time.sleep(0.2)
            labels = self.text_show.findChildren(QLabel)
            widgets = self.text_show.findChildren(QWidget)

            all_children = labels + widgets

            for child in all_children:
                child.deleteLater()

            self.text_show.destroy()  # 销毁文本显示窗口
        except Exception as e:
            print(f"Stop translation failed: {e}")

    def __translate(self):
        keys_to_search = ["n.", "v.", "adj.", "adv.", "pron.", "prep.", "conj.", "int.", "web.", "abbr.", "idiom.",
                          "phr.", "aux.", "modal.", "art.", "num.", "pl.", "poss.", "inf.", "na.", "vi.", "vt.",
                          "aux."]
        while True:
            text = None
            post = None
            self.translations = []
            self.positions = []
            if not self.tag:
                text, post = to.gain_text(self.text_show, self.tag)
                self.tag = True
                self.text_show.show()
            else:
                text, post = to.gain_text(self.text_show, self.tag)
            try:
                if text is not None:
                    for i in range(len(text)):
                        translation = translate(text=text[i], target_lang="zh-CN", source_lang="auto",
                                                translators=["bing"])
                        if len(translation.results) > 0:
                            translation_result = translation.results[0]
                            explains = next((translation_result.explains.get(key) for key in keys_to_search), None)
                            if explains is not None:
                                try:
                                    final_text = re.search(r"[\u4e00-\u9fa5]+(?=[^\u4e00-\u9fa5\u3000-\u303F])?",
                                                           explains).group(0)
                                    print("2级结果:", final_text)
                                    self.translations.append(final_text)
                                    self.positions.append(post[i])
                                except Exception as e:
                                    print(f"Translate failed: {e}")
                        if not self.is_translating:
                            return None
                    print("Translations:", self.translations, "\nPositions:", self.positions)
                    self.text_show.show_text(self.translations, self.positions)
                time.sleep(self.translation_delay)
            except Exception as e:
                print(f"Translate loop failed: {e}")
                return None
