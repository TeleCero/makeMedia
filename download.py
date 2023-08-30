import os 
  
def dfile(file: str, args: str = "", out: str = "./videos/"): 
  with open(file, "r") as f: 
    for line in f.read().splitlines(): 
      try: 
        os.system(f"yt-dlp {args} {line}") 
      except Exception as e: 
        print(e) 
def dyear(year: int, args: str = "", out: str = "./videos/"): 
  y = str(year) 
  file = f"./playlist/{year}.txt" 
  dfile(file, args) 
if __name__ == "__main__": 
  dyear(2023)