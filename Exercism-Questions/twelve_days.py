def recite(start_verse, end_verse):
    verses = [
        ("On the", "day of Christmas my true love gave to me: "),
        ("first", "a Partridge in a Pear Tree."),
        ("second", "two Turtle Doves"),
        ("third", "three French Hens"),
        ("fourth", "four Calling Birds"),
        ("fifth", "five Gold Rings"),
        ("sixth", "six Geese-a-Laying"),
        ("seventh", "seven Swans-a-Swimming"),
        ("eighth", "eight Maids-a-Milking"),
        ("ninth", "nine Ladies Dancing"),
        ("tenth", "ten Lords-a-Leaping"),
        ("eleventh", "eleven Pipers Piping"),
        ("twelfth", "twelve Drummers Drumming")
             ]
       
    return [f"{verses[0][0]}{verses[n][0]}{verses[0][1]}"
            f"{', '.join(verses[j][1] for j in range(n, 1, -1))}"
            f"{', and ' if n > 1 else ''}{verses[1][1]}"
            for n in range(start_verse, end_verse+1)]
      

