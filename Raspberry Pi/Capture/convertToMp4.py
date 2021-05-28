from subprocess import call #コマンド実行

#mp4形式に変換&h264形式のファイル削除
def cvtToMp4(file_name):
	#h264形式をmp4形式に変換
	cmdcvt = "MP4Box -fps 30 -add " + file_name + ".h264 " + file_name + ".mp4" #コマンド
	call([cmdcvt], shell = True) #コマンド実行

	##h264形式のファイルを削除
	#cmdrm = "rm " + file_name + ".h264" #コマンド
	#call([cmdrm], shell = True) #コマンド実行

if __name__ == '__main__':
  cvtToMp4('naoki')