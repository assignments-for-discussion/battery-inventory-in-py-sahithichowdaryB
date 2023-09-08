
def count_batteries_by_health(present_capacities):
  # initialize counters for healthy,excange and failed batteries
  count_healthy=0             
  count_exchange=0
  count_failed=0
  # iterate through the list of present capacities to assess battery health
  for i in present_capacities:
    # calculate soh (State of Health) as percentage
    soh=(100.0)*(float(i)/120.0) 
    #categorize batteries based on their soh (State of Health) value
    if 80<soh<=100:
      count_healthy+=1
    elif 65<=soh<=80:
      count_exchange+=1
    else:
      count_failed+=1
  return {
    "healthy":count_healthy ,
    "exchange": count_exchange,
    "failed": count_failed
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  
  #Test case 0:Mix of healthy,exchange and failed
  present_capacities_0 = [115, 118, 80, 95, 91, 77]
  counts_0 = count_batteries_by_health(present_capacities_0)
  assert(counts_0["healthy"] == 2)
  assert(counts_0["exchange"] == 3)
  assert(counts_0["failed"] == 1)
  
  #Test case 1:All healthy batteries
  present_capacities_1 = [120,119,118,117,116]
  counts_1 = count_batteries_by_health(present_capacities_1)
  assert (counts_1["healthy"] == 5)
  assert (counts_1["exchange"] == 0)
  assert (counts_1["failed"] == 0)
  
  # Test case 2: All exchange batteries
  present_capacities_2 = [81,94,90,82,85]
  counts_2 = count_batteries_by_health(present_capacities_2)
  assert (counts_2["healthy"]) == 0
  assert (counts_2["exchange"]) == 5
  assert (counts_2["failed"])== 0
  
  # Test case 3: All failed batteries
  present_capacities_3 = [60, 55, 45, 30, 20]
  counts_3 = count_batteries_by_health(present_capacities_3)
  assert (counts_3["healthy"]) == 0
  assert (counts_3["exchange"]) == 0
  assert (counts_3["failed"])== 5
  
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
