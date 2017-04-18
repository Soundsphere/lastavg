# lastavg

:musical_note: :notes:
Check your average playcount up to four decimals :notes: :musical_note:

---

To use with your own last.fm account, replace the following variables:

`profile` = the link to your profile

`joined` = the date you joined last.fm

---

If you want to display the average in conky, use the following line in conky:

`{execi -3600 /path/to/script/lastfmcalc.py | tail -n1 }`
