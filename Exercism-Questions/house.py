def recite(start_verse, end_verse):
    start = "This is the "
    end = "house that Jack built."
    verses = [
        'blank',
        '',
		'malt that lay in the ',
		'rat that ate the ',
		'cat that killed the ',
		'dog that worried the ',
		'cow with the crumpled horn that tossed the ',
		'maiden all forlorn that milked the ',
		'man all tattered and torn that kissed the ',
		'priest all shaven and shorn that married the ',
		'rooster that crowed in the morn that woke the ',
		'farmer sowing his corn that kept the ',
		'horse and the hound and the horn that belonged to the '
    ]
    
    nursery = []
    for a in range(start_verse, end_verse+1):
        verse = start
        for i in range(a, 0, -1):
            verse += verses[i]
        verse += end
        nursery.append(verse)
    return nursery