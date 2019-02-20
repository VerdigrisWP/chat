#對話紀錄計數
import os

def open_file(filename): #定義函數「開啟檔案」
    with open(filename, 'r', encoding='utf-8-sig') as f: #解決出現「\ufeff」問題
        chat_log = []
        for line in f:
            chat_log.append(line.strip())
    return chat_log


def count(chat_log): #內容計數
    allen_word_count = 0
    allen_sticker_count = 0
    allen_picture_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_picture_count = 0
    for line in chat_log:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        for m in s[2:]:
            if name == 'Allen':
                if s[2] == '貼圖':
                    allen_sticker_count += 1
                elif s[2] == '圖片':
                    allen_picture_count += 1
                else:
                    allen_word_count += len(m)
            elif name == 'Viki':
                if s[2] == '貼圖':
                    viki_sticker_count += 1
                elif s[2] == '圖片':
                    viki_picture_count += 1
                else:
                    viki_word_count += len(m)
    print('Allen 輸入的總字數為：', allen_word_count, ', 貼圖數為：', allen_sticker_count, ', 照片數為：', allen_picture_count)
    print('Viki 輸入的總字數為：', viki_word_count, ', 貼圖數為：', viki_sticker_count, ', 照片數為：', viki_picture_count)


def write_file(chat_log): #定義函數「寫入檔案」
    with open ('output.txt', 'w', encoding='utf-8') as f:
        for line in chat_log:
            f.write(line + '\n')


def main():
    filename = 'LINE-Viki.txt'
    chat_log = open_file(filename)
    count(chat_log)
    #write_file(chat_log)


main()