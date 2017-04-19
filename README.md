# lastavg

:musical_note: :notes:
Check your average playcount up to four decimals :notes: :musical_note:

---

Run `pip install -r requirements.txt` to set everything up

---

To use with your own last.fm account, replace the following variables:

`username` = your last.fm username

`joined` = the date you joined last.fm

---

At the moment there's no executable, so just run the following:
```
git clone https://github.com/Soundsphere/lastavg.git
cd lastavg
chmod +x lastfmcalc.py
python lastfmcalc.py
```

Alternatively you can copy the script into your $PATH

---

If you want to display the average in conky, use the following line in your .conkyrc:

`{execi -3600 /path/to/script/lastfmcalc.py | tail -n1 | cut -d" " -f2 }`

---

## Screenshot

Here's how the output looks like:
![lastavgscreenshot](/docs/lastavgscreen.png?raw=true "lastavg output")
