import qrcode

# your information
name = "ali"
lastname = "aliz"
phone = "0000000000"
email = "john@example.com"
company = "microsoft"
title = "admin"
website = "https://example.com"
address = "kenedi"

# ساخت vCard
vcard_data = f"""BEGIN:VCARD
VERSION:3.0
N:{lastname};{name};;;
FN:{name} {lastname}
TEL;TYPE=CELL,VOICE:{phone}
ORG:{company}
TITLE:{title}
ADR;TYPE=WORK:;;{address};;;
NOTE: all internet
END:VCARD"""

# QR code generator
qr = qrcode.make(vcard_data)
qr.save("my_contact_qr.png")
qr.show()
print("✅")