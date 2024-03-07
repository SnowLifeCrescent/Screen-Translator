from PIL import ImageGrab, ImageEnhance
from pytesseract import pytesseract


def gain_text(text_show, tag):
    print("截图识别")
    if tag:
        text_show.hide_text()
        screenshot = __take_screenshot()
        text_show.de_hide_text()
    else:
        screenshot = __take_screenshot()
    text, positions = __ocr_text(screenshot)
    print("识别完成")
    return text, positions


def __take_screenshot():
    # 截取屏幕
    screenshot = ImageGrab.grab()

    # 图像预处理
    screenshot = screenshot.convert('L')  # 灰度化
    screenshot = ImageEnhance.Contrast(screenshot).enhance(1.8)  # 增加对比度
    # screenshot = screenshot.filter(ImageFilter.MedianFilter())  # 中值滤波去噪
    return screenshot


def __ocr_text(image):
    try:
        # 使用 Tesseract 进行 OCR 识别
        ocr_results = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

        # 解析 OCR 结果，获取每个识别到的文本区域的位置信息
        text = []
        positions = []
        for i in range(len(ocr_results['text'])):
            # 仅考虑包含文本的区域
            if int(ocr_results['conf'][i]) > 0.97:
                x = ocr_results['left'][i]
                y = ocr_results['top'][i]
                width = ocr_results['width'][i]
                height = ocr_results['height'][i]
                position = (x, y, width, height)
                text.append(ocr_results['text'][i])
                positions.append(position)

        return text[:100], positions[:100]
    except Exception as e:
        print(f"OCR failed: {e}")
        return [], []
