import json
import qrcode

# 1. Define the exact JSON structure from your target image
invoice_data = {
    "data": {
        "SellerGstin": "27AAACB2894G1ZN",
        "BuyerGstin": None,
        "DocNo": "PA2726B34317332",
        "DocTyp": "INV",
        "DocDt": "2026-06-01",
        "TotInvVal": 598.0,
        "ItemCnt": 1,
        "MainHsnCode": "998413",
        "Irn": None,
    }
}

# 2. Serialize dictionary to compact string format (no extra whitespaces)
json_payload = json.dumps(invoice_data, separators=(",", ":"))

# 3. Configure the QR code parameters to match the target's module density
qr = qrcode.QRCode(
    version=None,  # Automatically determines standard matrix layout fit
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # standard error correction level
    box_size=10,  # Controls pixel scale sizing per block
    border=0,  # Standard quiet zone margin around the matrix
)

# 4. Compile the payload data structure
qr.add_data(json_payload)
qr.make(fit=True)

# 5. Render the high contrast monochrome image
qr_img = qr.make_image(fill_color="black", back_color="white")

# 6. Save the output file
qr_img.save("replicated_invoice_qr.png")
print("Successfully generated standard invoice format QR code asset.")
