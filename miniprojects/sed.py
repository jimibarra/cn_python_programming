def sed(pattern, replacement, source, dest):
   fin = open(source, 'r')
   fout = open(dest, 'w')

   content = fin.readlines()
   for line in content:
      line = str(line.replace(pattern, replacement))
      fout.write(line)

   fin.close()
   fout.close()

def main():

   try:
      pattern = 'dog'
      replacement = 'cat'
      source = 'test1.txt'
      dest = source + '.replaced'
      sed(pattern, replacement, source, dest)
   except:
      print("Something went wrong")

if __name__ == '__main__':
   main()
