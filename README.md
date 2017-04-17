# lastavg

:musical_note: :notes:
Check your average playcount up to four decimals :notes: :musical_note:

---

To use with your own last.fm account, replace the following variables:

`profile` = the link to your profile

`joined` = the date you joined last.fm

---

If you want to display the average in conky, use the following line in conky:
> make sure to change the variables in conkycalc.py to your profile before using it
`{execi -3600 /home/bene/bin/conkycalc.py }`
