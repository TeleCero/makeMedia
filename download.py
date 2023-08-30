import os 
from time import sleep
DEFAULT_ARGS = "-f 'best[height<=480][ext=mp4]/bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480]'"
DEFAULT_PATH = "/srv/mergerfs/R01/Datos/TeleCero/Videos"
def dfile(file: str, args: str = DEFAULT_ARGS, out: str = DEFAULT_PATH):
  with open(file, "r") as f:
    for line in f.read().splitlines():
      line = line.split("|")
      os.system(f"mkdir -p '{out}/{line[0]}'")
      os.system(f"yt-dlp -P '{out}/{line[0]}' {args} '{line[1]}'")
def dyear(year, out: str = DEFAULT_PATH):
  path = out + "/" + str(year)
  dfile(f"./playlist/{str(year)}.txt")

def parseyear(inp: str):
  return inp.split(":", 1)

if __name__ == "__main__":
  print("The default path is:")
  print(DEFAULT_PATH)
  path = input("Corrected Path Without Trailing Slash\n> ")
  years = input("What years do you want to download?\nSeparate with comma\n> ").split(":", 1)
  for year in years:
    dyear(year)
