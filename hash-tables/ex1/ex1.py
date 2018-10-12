def get_indices_of_item_weights(weights, limit):
  hash = {}
  for value in range(len(weights)):
    if (weights[value] not in hash):
      hash[weights[value]] = value
    
    if (limit - weights[value] in hash and hash[limit - weights[value]] != value):
      return (value, hash[limit - weights[value]])

  return()


if __name__ == '__main__':
  print(get_indices_of_item_weights([0,5,7,12,25,34], 23))