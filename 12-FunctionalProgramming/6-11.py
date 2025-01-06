test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}]

condition = lambda x: (x["result"]>=50) and (x["result"]<=70)
results_filtered = list(filter(condition, test_results))

print(results_filtered)