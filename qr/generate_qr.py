from qrcode.main import QRCode
from qrcode.constants import ERROR_CORRECT_L
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

# Link to be inserted on the QR
LINK = os.getenv("QR_LINK", None)

# Path to save the QR image. Default is the curr dir
OUT_PATH = Path(os.getenv("OUT_PATH", ".")).resolve()

if not LINK:
    raise ValueError("No `QR_LINK` found on the environment. Please provide one.")


def create_and_get_qr_image(qr_info: str):
    # Create QR object
    qr = QRCode(
        version=1,  # Box Size
        error_correction=ERROR_CORRECT_L,  # Nivel de corrección de errores
        box_size=10,  # Boxes sizes inside the QR
        border=4,  # Border Size
    )

    # Add QR information
    qr.add_data(qr_info)
    qr.make(fit=True)
    logging.info("QR successfully generated.")

    # Generate QR image
    logging.info("Generating QR image.")
    img = qr.make_image(fill="black", back_color="white")
    logging.info("Image successfully generated.")

    return img


if __name__ == "__main__":
    logging.info("Starting process to generate QR.")

    qr_img = create_and_get_qr_image(qr_info=LINK)

    out_posix_path = (OUT_PATH / "qr_image.png").as_posix()
    logging.info(f"Saving QR image on {out_posix_path}.")

    qr_img.save(out_posix_path)
