import os

def installJohn():
  fullPath = os.path.expanduser("~/Documents/psw_finder")
  if os.path.exists(fullPath):
    os.system("rm -rf " + fullPath)
  os.system("mkdir ~/Documents/psw_finder/")
  os.system("curl -s -L https://github.com/openwall/john/zipball/bleeding-jumbo -o ~/Documents/psw_finder/CUDA.zip")
  mvPath = os.path.expanduser("~/Documents/psw_finder/openwall-john-ce1f865");
  os.system(f"mv {mvPath} ~/Documents/psw_finder/CUDA.zip")
  os.system("unzip -qq ~/Documents/psw_finder/CUDA.zip -d ~/Documents/psw_finder/")
  os.system("rm ~/Documents/psw_finder/CUDA.zip")

def getJohnPath():
  return os.path.expanduser("~/Documents/psw_finder/john-CUDA/")

def runConfigure():
  os.system(f"cd {getJohnPath()}src/ && ./configure")

def main():
  installJohn();
  runConfigure();


if __name__ == "__main__":
  main()