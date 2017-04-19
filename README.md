# L![lastfmlogo](/docs/icon.png?raw=true "Lastfm")tavg
:musical_note: :notes:
Check your average playcount up to four decimals :notes: :musical_note:

---
## Requirements
Run `pip install -r requirements.txt` to set everything up


## Install
At the moment there's no executable, so just run the following:
```
git clone https://github.com/Soundsphere/lastavg.git
cd lastavg
python lastfmcalc.py
```

_Alternatively you can copy the script into your $PATH and chmod +x the script so that you can just call it from anywhere_

## Usage
To use with your own last.fm account, replace the following variables:

`username` = your last.fm username

`joined` = the date you joined last.fm


## Conky
If you want to display the average in conky, use the following line in your .conkyrc:

`{execi -3600 /path/to/script/lastfmcalc.py | tail -n1 | cut -d" " -f2 }`


## Screenshot
Here's how the output looks like:
![lastavgscreenshot](/docs/lastavgscreen.png?raw=true "lastavg output")
