"""Case-study #5 Parsing web-pages
Developers:
Batenev P.A., Grigorev A.E., Dolgih N.A.
"""
import urllib.request

with open('input.txt', 'r') as f_in:
    with open('output.txt', 'w') as f_out:

        # Header.
        print('{:<20s}{:<7s}{:<7s}{:<7s}{:<7s}{:<7s}{:<7s}'
              .format("Name", "Comp", "Att", "Yds",
                      "TD", "Int", "Passer rating"), file=f_out)

        for line in f_in:
            url = line.strip()
            f = urllib.request.urlopen(url)
            s = f.read()
            text = str(s)

            # Extract player name.
            part_name = text.find("player-name")
            name = text[text.find('>', part_name) + 1:text.find('&', part_name)]

            # Extract player metrics.
            nums = text[text.find('TOTAL</td>') +
                        5:text.find('</tr>', text.find("TOTAL"))]

            nums = nums.replace("\\", '')\
                .replace("t", '').replace("n", '')
            nums = nums.replace("</d><d>", ' ')\
                .replace(",", "").replace("</d>", "")
            nums = nums.split()

            comp = int(nums[0])
            att = int(nums[1])
            yds = int(nums[3])
            td = int(nums[5])
            _int = int(nums[6])

            # Сalculate passer rating.
            a = (comp / att - .3) * 5
            b = (yds / att - 3) * .25
            c = (td / att) * 20
            d = 2.375 - (_int / att * 25)

            pas_rat = round(((a + b + c + d) / 6) * 100, 2)

            print('{:<20s}{:<7s}{:<7s}{:<7s}{:<7s}{:<7s}{:<7s}'
                  .format(name, str(comp), str(att), str(yds), str(td), str(_int), str(pas_rat)), file=f_out)
