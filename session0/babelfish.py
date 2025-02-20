from collections import defaultdict

if __name__ == "__main__":
    data = open(0, "r").read()
    dd, wd = data.split("\n\n")
    d = {v: k for k, v in [
        x.split(" ") for x in dd.split("\n")
    ]}
    d = defaultdict(lambda: "eh", d)
    ws = list(wd.split("\n"))
    for w in ws[:-1]:
        print(d[w])