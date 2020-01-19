import inflect

def recite(start_verse, end_verse):
    days={12:"twelve Drummers Drumming, ",11:"eleven Pipers Piping, ",10:"ten Lords-a-Leaping, ",
          9:"nine Ladies Dancing, ",8:"eight Maids-a-Milking, ",7:"seven Swans-a-Swimming, ",
          6:"six Geese-a-Laying, ",5:"five Gold Rings, ",4:"four Calling Birds, ",
          3:"three French Hens, ",2:"two Turtle Doves, ",1:"a Partridge in a Pear Tree."}

    p = inflect.engine()

    answer = []

    for day in range(start_verse, end_verse + 1):
        day_text = p.number_to_words(p.ordinal(day))

        text = ('On the ' + day_text + ' day of Christmas my true love gave to me: ')

        for i in range(day, 0, -1):
            if (i == 1) and (day > 1): text += 'and '
            text += days.get(i)
        answer.append(text)

    return(answer)

