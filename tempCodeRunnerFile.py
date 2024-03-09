
rows=table.find_all("tr")
for i in rows[1:]:
    data=i.find_all("td")
    print(data)