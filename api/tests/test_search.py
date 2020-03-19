import search

x = search.get_users('light+repos:>5','stars','asc')
print(x[0],len(x[1]))