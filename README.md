# QR Code Generator
This repository is part of a broader project aimed at demonstrating how QR codes have become widely popular and how easily people scan and follow them without thinking twice about their origin. The same way attackers used to scatter USB drives around company parking lots to lure people into inserting them into their computers, today, it's as simple as placing a QR code in public spaces.

Attackers can replace a QR code in a restaurant, for example, leading users to a malicious link, and the users wouldn't notice since the behavior of scanning a QR code is so seamless and trusted.

For more details on this topic and the full project, visit my LinkedIn post.







## Requirements
 * Python 3.12.5
 * Dependencies managed via Poetry.

## Setup

1. Install dependencies:

```bash
poetry install
```

2. Create a `.env` file with the following variables:

* `QR_LINK`: (Required) The URL or text to encode into the QR.
* `OUT_PATH`: (Optional) Path where the QR image will be saved. Defaults to the current directory.


## Usage
To generate a QR code:

1. Load the environment variables:

```bash
set -a 
source .env
set +a
```

2. Run the script:

```bash
python -m qr.generate_qr
```

This will create and save the QR image in the specified `OUT_PATH` or the current directory as `qr_image.png`.