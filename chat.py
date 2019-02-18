#對話紀錄格式轉換

import os

def open_file(filename): #定義函數「開啟檔案」
	with open(filename, 'r', encoding='utf-8') as f:
		chat_log = []
		for line in f:
			line = line.encode('utf-8').decode('utf-8-sig') #解決出現「\ufeff」問題
			chat_log.append(line.strip())
	return chat_log

def reformate(chat_log): #定義函數「重整格式」
	chat_relog = []
	for line in chat_log:
		if line == 'Allen' or line == 'Tom':
			name = line + ':'
		else:
			chat_relog.append(name + line)
	return chat_relog

def write_file(chat_log): #定義函數「寫入檔案」
	with open ('output.txt', 'w', encoding='utf-8') as f:
		for line in chat_log:
			f.write(line + '\n')

def main():
	filename = input('請輸入欲開啟的檔案名稱：')
	if os.path.isfile(filename):
		chat_log = open_file(filename)
		chat_log = reformate(chat_log)
		write_file(chat_log)
	else:
		print('找不到檔案，請重新輸入')

main()