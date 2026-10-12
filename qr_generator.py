
import qrcode

# Generate a personal QR code
message = input("Enter your name or a short message: ")

img1 = qrcode.make(message)
img1.save("personal_qrcode.png")

print("Personal QR code saved successfully!")

# Generate a website QR code
website = input("Enter your favorite website URL: ")

img2 = qrcode.make(website)
img2.save("website_qrcode.png")

print("Website QR code saved successfully!")
