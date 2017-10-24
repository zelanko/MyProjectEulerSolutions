collatz_sequences = dict()

def collatz(start):
  """return Collatz sequense started with parameter 'start'"""
  n = start

  collatz_sequence = [n]

  while global.collatz_sequences.key().contains(n):
    if n % 2 == 0:
      n = n // 2
    else:
      n = 3 * n + 1

    collatz_sequence.append(n)

  global.collatz_sequences[]

  return collatz_sequence

max_len = 0

for i in range(1, 1000001):
  seq = collatz(i)
  seq_len = len(seq)
  if (max_len < seq_len):
    max_len = seq_len
    print("({}) [{}]".format(i, seq_len))
