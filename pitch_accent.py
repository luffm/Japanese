    # Get the nasal positions
    nasal = []
    if e.nasalsoundpos:
        positions = e.nasalsoundpos.split('0')
        for p in positions:
            if p:
                nasal.append(int(p))
            if not p:
                # e.g. "20" would result in ['2', '']
                nasal[-1] = nasal[-1] * 10

    # Get the no pronounce positions
    nopron = []
    if e.nopronouncepos:
        positions = e.nopronouncepos.split('0')
        for p in positions:
            if p:
                nopron.append(int(p))
            if not p:
                # e.g. "20" would result in ['2', '']
                nopron[-1] = nopron[-1] * 10

kana_conv = {'カ':'ガ',
             'キ':'ギ',
             'ク':'グ',
             'ケ':'ゲ',
             'コ':'ゴ'}

new = list(midashigo1)
for pos in nasal:
    new[pos-1] = kana_conv[new[pos-1]]
midashigo1 = ''.join(new)
