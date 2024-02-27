import qrcode
def generate_qr_code(data, file_name="qrcode.png", color_scheme="black_on_white"):
    color_schemes = {
        "black_on_white": {"fill": "black", "back": "white"},
        "red_on_white": {"fill": "red", "back": "white"},
        "green_on_pink": {"fill": "green", "back": "pink"},
        "blue_on_yellow": {"fill": "blue", "back": "yellow"},
    }
    if color_scheme not in color_schemes:
        print("Invalid color scheme. Using default black_on_white.")
        color_scheme = "black_on_white"
    scheme = color_schemes[color_scheme]
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=scheme["fill"], back_color=scheme["back"])
    img.save(file_name)
    print(f"QR Code saved as {file_name} with color scheme: {color_scheme}")
data = input("Enter the URL to encode: ")
print("Choose a color scheme:")
print("1. Black on White")
print("2. Red on White")
print("3. Green on Pink")
print("4. Blue on Yellow")

choice = input("Choose the number for color scheme: ")
color_mapping = {
        "1": "black_on_white",
        "2": "red_on_white",
        "3": "green_on_pink",
        "4": "blue_on_yellow",
          }
color = color_mapping.get(choice, "black_on_white")
generate_qr_code(data, color_scheme=color)
