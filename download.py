import os
import requests
from time import sleep
DEFAULT_ARGS = "-f 'best[height<=480][ext=mp4]/bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480]' --write-sub --write-auto-sub --sub-lang '*'"
DEFAULT_PATH = input("Corrected Path Without Trailing Slash\n> ")
def dfile(file: str, args: str = DEFAULT_ARGS, out: str = DEFAULT_PATH):
  with open(file, "r") as f:
    for line in f.read().splitlines():
      line = line.split("|")
      os.system(f"mkdir -p '{out}/{line[0]}'")
      os.system(f"yt-dlp -P '{out}/{line[0]}' {args} '{line[1]}'")
def dmode(mode, out: str = DEFAULT_PATH):
  path = out + "/" + str(mode)
  dfile(f"./playlist/{str(mode)}.txt")

if __name__ == "__main__":
  modes = input("What modes do you want to download?\nSeparate with comma\n> ").split(":", 1)
  for mode in modes:
    dmode(mode)
