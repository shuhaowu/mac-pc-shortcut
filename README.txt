Remap OS X shortcut to PC-styled ones. You can make computers do whatever you
want.

Howto:

1. Change files in rules/ if necessary.
2. Files in common/ can be substituted into any value field in the rules.
3. Run make
4. The output will be stored in rules.json. Copy this file.
5. Open ~/.config/karabiner/karabiner.json
6. Paste the rules.json content into the key [0]["profile"][0]["rules"]. The
   exact position might be different, depending on which profile is active.
7. Restart karabiner elements.
