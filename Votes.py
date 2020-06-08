input_file = open('input.txt', 'r', encoding='utf-8')
parties = []
votes = []
input_file.readline()
for row in input_file:
    if row != 'VOTES:\n':
        parties.append(row.strip())
    else:
        break
print(parties)
for line in input_file:
    votes.append(line.strip())
print(votes)
count_party = [0] * len(parties)
for element in votes:
    count_party[parties.index(element)] += 1
print(count_party)
all_votes = []
for i in range(len(count_party)):
    all_votes.append((count_party[i], parties[i]))
print(all_votes)
all_votes.sort(key=lambda x: x[0], reverse=True)
print(all_votes)
for party in all_votes:
    print(party[1])