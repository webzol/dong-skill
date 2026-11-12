import io, sys
from bs4 import BeautifulSoup, Tag
p = sys.argv[1]
s = io.open(p, encoding="utf-8").read()
soup = BeautifulSoup(s, "html.parser")
def has_leaf(node):
    for parent in node.parents:
        if isinstance(parent, Tag) and parent.name == "span" and parent.get("leaf") is not None:
            return True
    return False
for node in list(soup.find_all(string=True)):
    if not node.strip() or has_leaf(node):
        continue
    span = soup.new_tag("span"); span["leaf"] = ""
    node.replace_with(span); span.append(node)
out = str(soup)
io.open(p, "w", encoding="utf-8", newline="\n").write(out)
print(p, out.count('<span leaf="">'))
