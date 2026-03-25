# A Banner Grabber / Port Scanner

## What it does

- Reads banners from open ports (e.g., SSH)
- Has a basic scanning function
- Can distinguish between open and closed ports

## What it struggles with

- Ports that expect the client to speak first

## Coming tomorrow (hopefully!)

- Proper banner grabbing for more services
- Better error handling

# The addmain.py
- Adds a new function so with not giving -p all 65536 ports get scanned with giving a -p you can set ports and with a "," you can scan multipla ports at once.
- And the changes added better error handeling.
- You can now also add a -b to get banners with out it no banners will be not be colected

## CVE
Later I will add automatic detection of vulnerable versions!

    
