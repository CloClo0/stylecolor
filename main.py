import src.stylecolor as sc
print()


colored = sc.blue("raw blue text")
raw = sc.raw(colored) # return raw string
print(raw)
sc.rprint(colored)  # directly print raw result
