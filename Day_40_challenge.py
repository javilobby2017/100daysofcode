name = input("name: ").strip().capitalize()
dob = input("dob: ").strip()
tel = input("phonenumber: ").strip()
email = input("email: ").strip()
address = input("address: ").strip()
contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}

print()
print(f"""name: {contact["name"]}""")
print(f"""dob: {contact["dob"]}""")
print(f"""tel: {contact["tel"]}""")
print(f"""email: {contact["email"]}""")
print(f"""address: {contact["address"]}""")
