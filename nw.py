import sys

help = "To jest program służący do dopasowywania globalnego dwóch sekwencji. Podaj plik w formacie FASTA i opcjonalnie parametry punktacji dopasowania."

if len(sys.argv) >= 2:
  plik = sys.argv[1]
else:
  print("Error: You must provide a file in format fasta")
  sys.exit(0)

with open(plik) as f:
  sequence1 = f.readline()
  if sequence1[0] == ">":
    sequence1 = f.readline()
  sequence2 = f.readline()
  if sequence2[0] == ">":
    sequence2 = f.readline()

match_score = 1
mismatch_score = -1
gap_score = -1

if len(sys.argv) == 2:
  print("The program works with default match, mismatch and gap values.")
elif sys.argv[2] == "--help" or sys.argv[2] == "-h":
  print(help)
  sys.exit(0)
elif len(sys.argv) >= 5 and (sys.argv[2] == "--scores" or sys.argv[2] == "-s"):
  match_score = int(sys.argv[3])
  mismatch_score = int(sys.argv[4])
  gap_score = int(sys.argv[5])
else:
  print("Error: unkown switch: ", sys.argv[2], " or not enough arguments. Type --h or --help for help.")
  sys.exit(0)

print("Match_score: ", match_score)
print("Mismatch_score: ", mismatch_score)
print("Gap_score: ", gap_score)

sequence1 = sequence1.strip()
sequence2 = sequence2.strip()
print("\nSequence 1: ", sequence1)
print("Sequence 2: ", sequence2)

matrix = []
for x in range(len(sequence1)+2):
  matrix.append([])
  for y in range(len(sequence2)+2):
    matrix[x].append(0)
  if x == 0:
    for y in range(len(sequence2)+2):
      if y>1:
        matrix[0][y] = sequence2[y-2]
  elif x==1:
    for y in range(len(sequence2)):
      matrix[x][y+1]=y*(-2)
  else:
    matrix[x][0] = sequence1[x-2]
    matrix[x][1] = (x-1)*(-1)
#koniec implementacji macierzy, start dzialania algorytmu

#for line in matrix:
#  print(line)

for x in range(len(matrix)):
  if x==0 or x==1:
    continue
  for y in range(len(matrix[x])):
    if y==0 or y==1:
      continue
    options = []
    options.append(matrix[x][y-1]+gap_score)
    options.append(matrix[x-1][y]+gap_score)
    if matrix[0][y]==matrix[x][0]:
      options.append(matrix[x-1][y-1]+match_score)
    else:
      options.append(matrix[x-1][y-1]+mismatch_score)
    matrix[x][y]=max(options)
##koniec wypelniania macierzy

#for line in matrix:
#  print(line)

cursor = matrix[len(matrix)-1][len(matrix[len(matrix)-1])-1]
score = cursor
cursor_x = len(matrix)-1
cursor_y = len(matrix[len(matrix)-1])-1
#print(cursor)
#print(cursor_x)
#print(cursor_y)

#sprawdzenie z ktorej komorki przyszedl wynik i zapisanie go do result1:
result1=[]
result2=[]
while cursor_x != 1 and cursor_y != 1:
  if cursor == matrix[cursor_x-1][cursor_y-1]+match_score and matrix[0][cursor_y]==matrix[cursor_x][0]:
    result1.insert(0, matrix[cursor_x][0])
    result2.insert(0, matrix[0][cursor_y])
    cursor = matrix[cursor_x-1][cursor_y-1]
    cursor_x = cursor_x-1
    cursor_y = cursor_y-1
  elif cursor == matrix[cursor_x-1][cursor_y]+gap_score:
    result1.insert(0, matrix[cursor_x][0])
    result2.insert(0, "-")
    cursor = matrix[cursor_x-1][cursor_y]
    cursor_x = cursor_x-1
  elif cursor == matrix[cursor_x][cursor_y-1]+gap_score:
    result1.insert(0, "-")
    result2.insert(0, matrix[0][cursor_y])
    cursor = matrix[cursor_x][cursor_y-1]
    cursor_y = cursor_y-1
  elif cursor == matrix[cursor_x-1][cursor_y-1]+mismatch_score:
    result1.insert(0, matrix[cursor_x][0])
    result2.insert(0, matrix[0][cursor_y])
    cursor = matrix[cursor_x-1][cursor_y-1]
    cursor_x = cursor_x-1
    cursor_y = cursor_y-1
  else:
    print("error!!!")
    break
  #print(cursor," ", cursor_x, " ", cursor_y)

print("\nResult is: ")
print(result1)
print(result2)
print("Score: ", score)
print("Keep in mind that there may be more than one result with the same score. Here is an example of one with the highest score.")

with open("alignment_result.txt", "w") as output_file:
    output_file.write("Wynik dopasowania:\n")
    output_file.write("".join(result1) + "\n")
    output_file.write("".join(result2) + "\n")
    output_file.write("Punkty: " + str(score) + "\n")

print("\nThe result has been saved to the 'alignment_result.txt' file.")
