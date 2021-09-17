counties = ["Nairobi", "kisumu", "nakuru", "embu", "machakos", "mombasa"]
for county in counties:
    print(county)
    if county == "embu": #stop the loop when embu county is reached
        break
    else:
        continue # continue if the county is not embu
