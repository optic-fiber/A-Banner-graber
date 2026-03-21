# A Banner Grabber / Port Scanner

## What it does

- Reads banners from open ports (e.g., SSH)
- Has a basic scanning function
- Can distinguish between open and closed ports

## What it struggles with

- Ports that expect the client to speak first
- Proper error handling

## Coming tomorrow (hopefully!)

- Proper banner grabbing for more services
- Better error handling

# The addmain.py

## A much better scanner!
- Handles many errors (still too lazy to add a keyboard interrupt :))
- Handles most timeout issues
- Can only grab banners from SSH for now :(
- Looks and feels much better
- Has no scan function yet — `main.py` has one, and I’ll add it soon

## CVE
Later I will add automatic detection of vulnerable versions!

    
