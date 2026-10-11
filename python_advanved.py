import re
from datetime import datetime


data_mahasiswa = [
    {
        "nama": "Aisyah Elsi",
        "nim": "230101",
        "tugas": 85,
        "uts": 80,
        "uas": 88
    },
    {
        "nama": "Budi Galon",
        "nim": "230102",
        "tugas": 70,
        "uts": 65,
        "uas": 75
    },
    {
        "nama": "Cantika Berpikir Keras",
        "nim": "230103",
        "tugas": 90,
        "uts": 85,
        "uas": 92
    },
    {
        "nama": "Dimas Ma'had",
        "nim": "230104",
        "tugas": 78,
        "uts": 82,
        "uas": 80
    },
    {
        "nama": "Eka Pentol",
        "nim": "230105",
        "tugas": 95,
        "uts": 90,
        "uas": 94
    }
]


def analisis_nilai():

    print("\n" + "=" * 65)
    print("             STUDI KASUS 1 - ANALISIS NILAI")
    print("=" * 65)

    data_nilai = [
        {
            **mahasiswa,
            "nilai_akhir": (
                mahasiswa["tugas"] * 0.30
                + mahasiswa["uts"] * 0.30
                + mahasiswa["uas"] * 0.40
            )
        }
        for mahasiswa in data_mahasiswa
    ]

    mahasiswa_berprestasi = list(
        filter(
            lambda mahasiswa: mahasiswa["nilai_akhir"] > 80,
            data_nilai
        )
    )

    ranking = sorted(
        data_nilai,
        key=lambda mahasiswa: mahasiswa["nilai_akhir"],
        reverse=True
    )

    print("\nDAFTAR NILAI AKHIR")
    print("-" * 65)

    for mahasiswa in data_nilai:
        print(
            f"{mahasiswa['nama']:10} | "
            f"NIM: {mahasiswa['nim']} | "
            f"Nilai Akhir: {mahasiswa['nilai_akhir']:.2f}"
        )

    print("\nMAHASISWA BERPRESTASI (NILAI > 80)")
    print("-" * 65)

    for mahasiswa in mahasiswa_berprestasi:
        print(
            f"{mahasiswa['nama']:10} | "
            f"NIM: {mahasiswa['nim']} | "
            f"Nilai: {mahasiswa['nilai_akhir']:.2f}"
        )

    print("\nRANKING MAHASISWA")
    print("-" * 65)

    for nomor, mahasiswa in enumerate(ranking, start=1):
        print(
            f"{nomor}. {mahasiswa['nama']:10} | "
            f"NIM: {mahasiswa['nim']} | "
            f"Nilai: {mahasiswa['nilai_akhir']:.2f}"
        )

    mahasiswa_terbaik = ranking[0]

    print("\nMAHASISWA TERBAIK")
    print("-" * 65)
    print(f"Nama        : {mahasiswa_terbaik['nama']}")
    print(f"NIM         : {mahasiswa_terbaik['nim']}")
    print(f"Nilai Tugas : {mahasiswa_terbaik['tugas']}")
    print(f"Nilai UTS   : {mahasiswa_terbaik['uts']}")
    print(f"Nilai UAS   : {mahasiswa_terbaik['uas']}")
    print(f"Nilai Akhir : {mahasiswa_terbaik['nilai_akhir']:.2f}")


def sensor_suhu():

    suhu = 15.0

    while suhu <= 38.0:
        yield suhu
        suhu += 1.5


def kategori_suhu(suhu):

    if suhu < 20:
        return "Dingin"

    elif suhu <= 30:
        return "Normal"

    else:
        return "Panas"


def streaming_sensor():

    print("\n" + "=" * 65)
    print("          STUDI KASUS 2 - STREAMING DATA IoT")
    print("=" * 65)

    data_sensor = sensor_suhu()

    print("\nPEMBACAAN SENSOR SECARA BERTAHAP")
    print("-" * 65)

    for nomor in range(10):

        try:
            suhu = next(data_sensor)

            status = kategori_suhu(suhu)

            print(
                f"Pembacaan ke-{nomor + 1:02} | "
                f"Suhu: {suhu:5.1f} °C | "
                f"Status: {status}"
            )

        except StopIteration:
            print("Data sensor sudah habis.")
            break

    print("-" * 65)
    print("Streaming data selesai.")


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value


def validasi_username(username):

    pola = r"^[A-Za-z0-9]{5,}$"

    if not re.fullmatch(pola, username):
        return False, (
            "Username minimal 5 karakter dan "
            "hanya boleh mengandung huruf dan angka."
        )

    return True, "Username valid."


def validasi_password(password):

    if len(password) < 8:
        return False, "Password minimal 8 karakter."

    pola_angka = r"\d"

    if not re.search(pola_angka, password):
        return False, (
            "Password harus mengandung "
            "minimal satu angka."
        )

    return True, "Password valid."


def audit_login(func):

    def wrapper(username, password):

        waktu = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        hasil, alasan = func(username, password)

        if hasil:

            print(
                f"[AUDIT] {waktu} | "
                f"User: {username} | "
                f"Status: BERHASIL"
            )

        else:

            print(
                f"[AUDIT] {waktu} | "
                f"User: {username} | "
                f"Status: DITOLAK | "
                f"Alasan: {alasan}"
            )

        return hasil, alasan

    return wrapper


user_terdaftar = User(
    "ArulBelajarNgoding",
    "DangakDangakdewe123"
)


@audit_login
def login(username, password):

    username_valid, pesan_username = validasi_username(username)

    if not username_valid:
        return False, pesan_username

    password_valid, pesan_password = validasi_password(password)

    if not password_valid:
        return False, pesan_password

    if username != user_terdaftar.username:
        return False, "Username tidak terdaftar."

    if password != user_terdaftar.password:
        return False, "Password salah."

    return True, "Login berhasil."


def sistem_keamanan():

    print("\n" + "=" * 65)
    print("       STUDI KASUS 3 - SISTEM KEAMANAN AKUN")
    print("=" * 65)

    print("\n[1] LOGIN DENGAN USERNAME TIDAK VALID")

    hasil, pesan = login(
        "ARulBelajarNgoding",
        "Bima1234"
    )

    print("Hasil:", pesan)

    print("\n[2] LOGIN DENGAN PASSWORD TERLALU PENDEK")

    hasil, pesan = login(
        "ArulBelajarNgoding",
        "DangakDangakdewe123"
    )

    print("Hasil:", pesan)

    print("\n[3] LOGIN DENGAN PASSWORD TANPA ANGKA")

    hasil, pesan = login(
        "ArulBelajarNgoding",
        "DangakDangakdewe123"
    )

    print("Hasil:", pesan)

    print("\n[4] LOGIN DENGAN PASSWORD TANPA ANGKA")

    hasil, pesan = login(
        "ArulBelajarNgoding",
        "DangakDangakdewe123"
    )

    print("Hasil:", pesan)

    print("\n[5] LOGIN DENGAN KREDENSIAL BENAR")

    hasil, pesan = login(
        "ArulBelajarNgoding",
        "DangakDangakdewe123"
    )

    print("Hasil:", pesan)


def main():

    while True:

        print("\n")
        print("=" * 65)
        print("             PYTHON ADVANCED CASE STUDY")
        print("=" * 65)
        print("1. Analisis Nilai Mahasiswa")
        print("2. Streaming Data Sensor IoT")
        print("3. Sistem Keamanan Akun & Audit Log")
        print("4. Jalankan Semua Studi Kasus")
        print("5. Keluar")
        print("=" * 65)

        pilihan = input("Pilih menu [1-5]: ")

        if pilihan == "1":

            analisis_nilai()

        elif pilihan == "2":

            streaming_sensor()

        elif pilihan == "3":

            sistem_keamanan()

        elif pilihan == "4":

            analisis_nilai()
            streaming_sensor()
            sistem_keamanan()

        elif pilihan == "5":

            print("\nProgram selesai.")
            print("Terima kasih.")
            break

        else:

            print("\nPilihan tidak valid!")
            print("Silakan pilih menu 1 sampai 5.")


if __name__ == "__main__":
    main()