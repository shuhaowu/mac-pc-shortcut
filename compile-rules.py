import json
import os
import sys


def substitute_json(j, commons):
  for k, v in j.items():
    if isinstance(v, str) and v in commons:
      j[k] = commons[v]
    elif isinstance(v, dict):
      j[k] = substitute_json(v, commons)
    elif isinstance(v, list):
      new_list = []
      for item in v:
        if isinstance(item, dict):
          item = substitute_json(item, commons)

        new_list.append(item)
      j[k] = new_list

  return j


def main():
  commons = {}
  for filename in os.listdir("common"):
    with open(os.path.join("common", filename)) as f:
      commons[os.path.splitext(filename)[0]] = json.load(f)

    print("loaded {}".format(filename), file=sys.stderr)

  rules = []

  for filename in os.listdir("rules"):
    with open(os.path.join("rules", filename)) as f:
      rules.append(substitute_json(json.load(f), commons))

    print("loaded {}".format(filename), file=sys.stderr)

  print(json.dumps(rules, indent=2))

if __name__ == "__main__":
  main()
