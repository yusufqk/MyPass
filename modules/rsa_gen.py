from Cryptodome.PublicKey import RSA


def rsa_make():

    key = RSA.generate(4096)
    private_key = key.export_key()
    with open("./Keys/private.pem", "wb") as file_out:
        file_out.write(private_key)

    public_key = key.publickey().export_key()
    with open("./Keys/public.pem", "wb") as file_out:
        file_out.write(public_key)
