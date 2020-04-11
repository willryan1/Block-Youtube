# Block-Youtube
Just for personal use, fun project, inspiration from the internet

### Overview

Found bits and pieces on the internet and use it to minimize distractions

Might improve later for actual use

## Usage

Use a crontab to activate (MacOS or Linux)
```
git clone https://github.com/willryan1/Block-Youtube.git
```

To block youtube just run the script:

```
sudo python3 block_youtube.py
```

To enable youtube just run the script:
```
sudo python3 enable_youtube.py
```

Or you can set it up using crontab during a certain time interval
```
sudo crontab -e
```
```
@reboot python3 <path> (choose which time is your favorite)
```

### Variations
* 9-5Block.py - blocks youtube from 9 AM - 5 PM
* block_youtube - blocks youtube
* Enable_youtube - enable youtube
