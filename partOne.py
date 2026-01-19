def main():
  slow = input("Input ")
  slow = myFunction(slow)
  print(slow)

def myFunction(text):
  text = text.replace(" ", "...")
  return text

main()
