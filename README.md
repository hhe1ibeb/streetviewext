# Streetview Extention

This is an module of extensions of [the streetview module by robolyst](https://github.com/robolyst/streetview/tree/v0.0.2).
The functions allows you to collect streetview photos or panoramas among a route just by entering the origin and destination.

## Requirements

### Environment
This module requires python 3.11.3 or higher.

First, you'll have to install the original streetview module with pip:
```bash
pip install streetview
```
Then install this module with:
```bash
pip install git+https://github.com/hhe1ibeb/streetviewext
```

### API Keys
Get your Directions and Streetview Imagery APIs from https://developers.google.com/maps/

## Functions

### Collect Streetview Photos Among Route
This functions allows you to collect a batch of photos among a route by entering the origin and destination.

Example Code:
```python
from streetviewext import sv_among_route

sv_among_route(
    origin="Section 1, Jianguo S Rd, Daan District, Taipei City, 106",
    destination="No. 10, Section 4, Ren'ai Rd, Daan District, Taipei City, 106", 
    mode="driving",
    dir_key=GOOGLEMAPS_DIRECTIONS_KEY,
    street_key=GOOGLEMAPS_STREETVIEW_KEY,
    save_destination="./data", # default to current directory if not specified
    # you can also specify value such as width, height, field of view, or pitch
)
```
It saves a batch of photos to the destination you specify.

#### Params Specs
* **origin**: the address of the origin
* **destination**: the address of the destination
* **mode**: driving, walking, bicycling, transit, or flight (driving, walking, and bicycling are recommended)
* **dir_key**: your directions api key, it is recommended to use a .env file to store sensitive data
* **street_key**: your streetview imagery api key
* **save_destination**: the directory you wish to save the photos


> More Functions Coming Soon!
