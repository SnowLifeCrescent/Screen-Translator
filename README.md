# 屏幕翻译 / Screen Translator

基于OCR识别与Bing API的屏幕翻译程序。

A screen translation program based on OCR recognition and the Bing API.

---

## 使用说明：
点击左上角 [置顶] 初始化，然后点 [开始翻译] 即可。
出于网络延迟，目前设置了同屏识别词汇数最大为100。
翻译对象不限语言。
关闭时请先点击 [终止翻译] ，然后关闭窗口。
p.s. 需要联网。
p.p.s. 如遇毛玻璃阻挡鼠标，请牢记 [Alt + F4]。

## 用途：
原本是面对一些无官中也无汉化的游戏生啃费脑子，就摸了这么个简陋玩意儿。

## 目前缺陷：
没用明白PyQt5，置顶窗口做不到透明（透明会导致label一并看不见，单独设置的label.setStyleSheet并不起作用，貌似会被父控件覆盖）。

---

## Instructions for Use:
You can adjust it to translate into any target language by modifying [Class Translator].__translate within the loop, where the translation is performed with the following function: translation = translate(text=text[i], target_lang="zh-CN", source_lang="auto",translators=["bing"]).
Click on [置顶] (Top) in the upper left corner to initialize, then click [开始翻译] (Start Translation) to begin.
Due to network latency, the maximum number of recognized words on the screen is currently set to 100.
Translation is not limited to any specific language.
To close the program, please click [终止翻译] (Terminate Translation) first, then close the window.
p.s. Internet connection is required.
p.p.s. In case the mouse is obstructed by frosted glass, remember [Alt + F4].

## Purpose:
Originally designed to tackle the challenge of deciphering games without official translations or localization, I put together this simple tool.

## Current Limitations:
Not fully adept with PyQt5, unable to achieve transparency for the top window (transparency would cause the label to become invisible as well, setting label.setStyleSheet individually doesn't work, apparently overridden by the parent control).
