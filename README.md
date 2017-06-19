# Wallet-py3k

Python library to read/write [Apple Wallet](http://developer.apple.com/library/ios/#documentation/UserExperience/Conceptual/PassKit_PG/Chapters/Introduction.html#//apple_ref/doc/uid/TP40012195-CH1-SW1) (.pkpass) files

This is a fork of https://github.com/devartis/passbook which doesn't support py3k.

## Getting Started

1. Get a Pass Type Id

   Visit the iOS Provisioning Portal -> Pass Type IDs -> New Pass Type ID
   Select pass type id -> Configure (Follow steps and download generated pass.cer file)
   Use Keychain tool to export a Certificates.p12 file (need Apple Root Certificate installed)

2. Generate the necessary certificate and key .pem files

   ```sh
   openssl pkcs12 -in "Certificates.p12" -clcerts -nokeys -out certificate.pem
   openssl pkcs12 -in "Certificates.p12" -nocerts -out key.pem
   ```

## Typical Usage

```python
    from wallet.models import Pass, Barcode, StoreCard

    cardInfo = StoreCard()
    cardInfo.addPrimaryField('name', 'John Doe', 'Name')

    organizationName = 'Your organization'
    passTypeIdentifier = 'pass.com.your.organization'
    teamIdentifier = 'AGK5BZEN3E'

    passfile = Pass(cardInfo, \
        passTypeIdentifier=passTypeIdentifier, \
        organizationName=organizationName, \
        teamIdentifier=teamIdentifier)

    passfile.serialNumber = '1234567'
    passfile.barcode = Barcode(message = 'Barcode message')

    # Including the icon and logo is necessary for the passbook to be valid.
    passfile.addFile('icon.png', open('images/icon.png', 'rb'))
    passfile.addFile('logo.png', open('images/logo.png', 'rb'))
    passfile.create('certificate.pem', 'key.pem', 'wwdr.pem', '123456', 'test.pkpass') # Create and output the Passbook file (.pkpass)
```
## Note: Getting WWDR Certificate

Certificate is available @ http://developer.apple.com/certificationauthority/AppleWWDRCA.cer
It can be exported from KeyChain into a .pem (e.g. wwdr.pem)
