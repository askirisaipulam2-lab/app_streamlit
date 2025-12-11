import streamlit as st
import math

# Halaman Utama
st.title ('aplikasi perhitungan luas bangun datar')
st.header ('ini buatan anak si')

menu = st.sidebar.selectbox ('Menu', ['Luas Persegi', 'Luas Segitiga', 'Luas Lingkaran', 'Luas Persegi Panjang'])

if menu == 'Luas Persegi' :
    st.write (':blue[ini halaman untuk menghitung luas persegi]🔥')
    st.image ('https://www.doyanblog.com/wp-content/uploads/2023/05/rumus-luas-persegi.jpg', caption='gambar dan rumus luas persegi')
    sisi = st.number_input ('silahkan masukkan sisi', min_value=0)

    if st.button('hitung'):
        Luas = sisi * sisi
        st.success (f'Luas persegi adalah {Luas}')

elif menu == 'Luas Segitiga' :
    st.write ('ini halaman untuk menghitung luas segitiga 💡')
    st.image ('https://idschool.net/wp-content/uploads/2018/03/Rumus-Luas-Segitiga.png', caption='gambar dan rumus luas segitiga')
    alas = st.number_input ('masukan alas segitiga', min_value=0)
    tinggi = st.number_input ('masukan tinggi segitiga', min_value=0)

    if st.button ('hitung') :
        Luas = 0.5 * alas * tinggi
        st.success (f'Luas segitiga adalah {Luas}')

elif menu == 'Luas Lingkaran':
    st.write ('ini halaman untuk menghitung luas lingkaran 🤖') 
    st.image ('https://i.pinimg.com/736x/e3/ec/fc/e3ecfc747bbfe1186aa4992e19ea8596.jpg', caption='gambar dan rumus luas lingkaran')
    r = st.number_input ('masukan nilai jari jari lingkaran', min_value=0)
    
    if st.button ('hitung'):
        Luas = math.pi * (r**2)
        st.success (f'Luas Lingkaran adalah {Luas}')

elif menu == 'Luas Persegi Panjang' :
    st.write ('Ini Halaman Untuk Menghitung Luas Persegi Panjang')
    st.image ('https://cnc-magazine.oramiland.com/parenting/images/rumus_keliling_persegi_panjang.width-800.format-webp.webp', caption= 'gambar dan rumus luas persegi panjang')
    panjang = st.number_input ('masukan panjang persegi panjang', min_value=0)
    lebar = st.number_input ('masukan lebar persei panjang', min_value=0)

    if st.button ('hitung'):
        Luas = panjang * lebar
        st.success (f'Luas Persegi Panjang Adalah {Luas}')