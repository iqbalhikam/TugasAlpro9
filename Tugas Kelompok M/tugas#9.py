anggota_kelompok = [
    # Ahkmad Kholil Baidhawi
    {"Nama": "Ahkmad Kholil Baidhawi",
     "NIM/NPM": "2023310091",
     "Prody": "Teknik Informatika",
     "Fakultas": "Informatika",
     "Pekerjaan impian" : "Expert Network Engineer",
     "Gaji" : "≥ 50jt",
     "Perusahaan" : "Mastersystem Infotama"},
    
    # Destrian Adi Pamungkas
    {"Nama": "Destrian Adi Pamungkas",
     "NIM/NPM": "2023310013",
     "Prody": "Teknik Informatika",
     "Fakultas": "Informatika",
     "Pekerjaan impian" : "Director of the company ",
     "Gaji" : "≥ 40jt",
     "Perusahaan" : "NASA (National Aeronautics and Space Administration)"},
    
    # Gelmon Ferdinant
    {"Nama": "Gelmon Ferdinant",
     "NIM/NPM": "2023310014",
     "Prody": "Teknik Informatika",
     "Fakultas": "Informatika",
     "Pekerjaan impian" : "Website Developer Design Interior",
     "Gaji" : "≥ 15jt",
     "Perusahaan" : "NUC Corporation"},
    
    # M. Iqbal Fatkhul Hikam
    {"Nama": "M Iqbal Fatkhul Hikam",
     "NIM/NPM": "2023310004",
     "Prody": "Teknik Informatika",
     "Fakultas": "Informatika",
     "Pekerjaan impian" : "Pengembang Perangkat Lunak (Software Developer)",
     "Gaji" : "≥ 40jt",
     "Perusahaan" : "Microsoft"},
    
    # Rangga Apre Dianta Sembiring Meliala
    {"Nama": "Rangga Apre Dianta Sembiring Meliala",
     "NIM/NPM": "2023310019",
     "Prody": "Teknik Informatika",
     "Fakultas": "Informatika",
     "Pekerjaan impian" : "Security Sytem,backend developer",
     "Gaji" : "≥ 25jt",
     "Perusahaan" : "Microsoft"}
]

# Menampilkan informasi anggota kelompok
print ("\n\n\t\t\t\t|-----------| PERKENALAN |-----------|")
print ("\t\t\t\t|-----------| KELOMPOK M |-----------|")
print ("\t\t\t\t|                                    |")
print ("-----------------------------------------------------------------------------------------------------\n\n")
for anggota in anggota_kelompok:
    print(f"Nama\t\t\t: {anggota['Nama']}")
    print(f"Fakultas\t\t: {anggota['Fakultas']}")
    print(f"Prody\t\t\t: {anggota['Prody']}")
    print(f"NIM/NPM\t\t\t: {anggota['NIM/NPM']}")
    print(f"Pekerjaan impian\t: {anggota['Pekerjaan impian']}")
    print(f"Gaji\t\t\t: {anggota['Gaji']}")
    print(f"Perusahaan\t\t: {anggota['Perusahaan']}\n")
    print ("-----------------------------------------------------------------------------------------------------\n")