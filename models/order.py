"""Order — Minggu 11.

Hasil akhir sebuah transaksi.

Order dibuat dari isi Cart, tetapi bukan Cart itu sendiri: keranjang
masih bisa berubah, sedangkan order adalah catatan yang sudah selesai.
Karena itu total disimpan sebagai angka, bukan dihitung ulang.
"""

STATUS_QUEUED = "QUEUED"


class Order:
    def __init__(self, order_id, items, total, status=STATUS_QUEUED):
        self.order_id = order_id
        self.items = items
        self.total = total
        self.status = status
        
    def item_count(self):
        return len(self.items)