def reconstruct_trip(tickets):
  hash = {}
  plans = []
  for ticket in tickets:
    hash[ticket[0]] = ticket[1]
  status = hash[None]
  while status != None:
    plans.append(status)
    if status not in hash:
      return []
    status = hash[status]
  return plans

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
