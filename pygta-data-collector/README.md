Python package for automating collecting flexible dataset of frames from your favourite game.
It is originally meant to be used with Grand Theft Auto V in project about self-driving car.
It uses hint typing.

Installation:
```
pip install pygta-data-collector==0.0.1
```

Usage:

````
python3 run.py
````
or
````
from pygta-data-collector.screen_scraper import ScreenScrapper


image_collector: ScreenScrapper = ScreenScrapper()
image_collector.collect()
````



