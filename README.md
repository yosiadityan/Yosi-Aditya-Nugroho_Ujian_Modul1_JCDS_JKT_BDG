![purwadhika logo](https://static.wixstatic.com/media/2e6af2_f69a4271c3534ae1869a7ed63e278b2b~mv2.png/v1/fill/w_246,h_39,al_c,usm_0.66_1.00_0.01/2e6af2_f69a4271c3534ae1869a7ed63e278b2b~mv2.png)

Selamat datang di ujian modul 1 JCDS Jakarta dan Bandung. Waktu mengerjakan ujian adalah 3 (tiga) jam. Anda diperkenankan menjawab dalam 3 (tiga) file `.py` berbeda atau 1 (satu) file `.py` saja. Selamat mengerjakan.

1. **(Point 15)** Buatlah sebuah function bernama `create_phone_number`. Function ini akan menerima parameter berupa list of 10 numbers yang boleh diisi dengan angka mulai dari 0 hingga 9. Function ini akan me-return sebuah format nomor telpon dalam bentuk String. Contoh: User menginput '1234567890' maka akan diubah ke '(123) 456-7890' (Seperti pada contoh di foto bawah). **Ketentuan yang perlu diikuti**:
    - Jika dalam string terdapat alphabet, maka yang di-return adalah "Invalid input. No alphabet.".
    - Jika dalam string terdapat symbol, maka yang di-return adalah "Invalid input. No symbols.".
    - Jika panjang dari string kurang dari 10 digit atau lebih dari 10 digit, maka yang di-return adalah "Digits must be in length of 10, not more or less"
    - Jika dalam string terdapat digit di bawah 0 (negative value), maka yang di-return adalah, "Input only positive number"

    ![Jawaban No.1](https://github.com/ridhoaryo/Ujian_Modul1_JCDS_JKT_BDG/blob/main/jawaban_1.jpg?raw=true)

2. **(Point 35)** Buatlah sebuah function bernama `move_zeros`. Function ini akan Memindahkan semua angka 0 ke sisi sebelah kanan list.

    ![Jawaban No.2](https://github.com/ridhoaryo/Ujian_Modul1_JCDS_JKT_BDG/blob/main/jawaban_2.jpg?raw=true)

3. **(Point 50)** Buatlah sebuah class bernama **Statistic**. Yang mana class ini memiliki 4 method yaitu:
    - `mean()` : Untuk mencari rata-rata.
    - `median()` : Untuk mencari nilai tengah.
    - `mode()` : Untuk mencari nilai yang paling sering muncul (_most frequent value_). Jika terdapat satu value yang frekuensi (jumlah) kemunculannya sama dengan value yang lain, maka `mode` akan me-return `tidak ada modus`.
    - `std()` : Untuk mencari nilai standard deviation atau simpangan baku. Rumus standard deviation yang digunakan adalah:
    
        ![rumus](http://2.bp.blogspot.com/-aBOo4BiedBM/U8vonNkJq2I/AAAAAAAD8ao/Qe6oUfbHHOI/s1600/Population+std+dev.png)
    
        - xi = nilai tiap element pada list atau sequence
        - µ = nilai rata-rata dari list atau sequence
        - n = panjang list atau sequence
    - Setiap method di atas hanya menerima 1 parameter berupa list. (Contoh ada di gambar bawah.)
    - Untuk mencari nilai mean, median, mode dan standard deviation, **DILARANG** menggunakan bantuan library atau method apapun. Dengan kata lain, _make them from scratch_. Satu-satunya method yang boleh digunakan adalah method pada list : `sort`.

    ![declare](https://github.com/ridhoaryo/Ujian_Modul1_JCDS_JKT_BDG/blob/main/jawaban_3_0.jpg?raw=true)
    
    case 1: 
    
    ![Jawaban No.3.1](https://github.com/ridhoaryo/Ujian_Modul1_JCDS_JKT_BDG/blob/main/jawaban_3_1.jpg?raw=true)

    case: 2

    ![Jawaban No.3.2](https://github.com/ridhoaryo/Ujian_Modul1_JCDS_JKT_BDG/blob/main/jawaban_3_2.jpg?raw=true)

    case: 3

    ![Jawaban No.3.3](https://github.com/ridhoaryo/Ujian_Modul1_JCDS_JKT_BDG/blob/main/jawaban_3_3.jpg?raw=true)

    
Jika Anda sudah selesai mengerjakan ujian ini, upload jawaban ada ke dalam 1 (satu) repository di github. Lalu kirimkan link repository tadi ke ridhoaryo1991@gmail.com juga ke:

- Untuk murid Bandung: operational_bdg@purwadhika.com
- Untuk murid Jakarta: operational_jkt@purwadhika.com


Dengan Subject [Nama]_Ujian_Modul1_JCDS_JKT_BDG.
