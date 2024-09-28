# QR Code Generator
This project generates a QR code based on a provided link and saves it as an image.

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