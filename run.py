import os, blade as rozh
try: os.system("git pull"); os.system("python3.10 build.py")
except: print("[!] anda memakai versi terbaru")
folder = ["OK","CP"]
for x in folder:
	try: os.mkdir("/sdcard/FBL {}".format(x))
	except Exception as e: pass
rozh.menu_utama()
