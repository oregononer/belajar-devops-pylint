"""Modul demonstrasi kode yang telah diperbaiki sesuai standar PEP 8."""


def hitung_operasi_matematika(angka_pertama, angka_kedua):
    """Melakukan operasi penjumlahan sederhana.

    Args:
        angka_pertama: Bilangan pertama.
        angka_kedua: Bilangan kedua.

    Returns:
        Jumlah dari kedua bilangan.
    """
    return angka_pertama + angka_kedua


def main():
    """Fungsi utama demonstrasi."""
    total = hitung_operasi_matematika(10, 20)
    print(f"Hasil penjumlahan: {total}")


if __name__ == "__main__":
    main()
