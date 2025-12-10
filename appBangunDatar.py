import streamlit as st

# Halaman Utama
st.title ('aplikasi perhitungan luas bangun datar')
st.header ('ini buatan anak si')

menu = st.sidebar.selectbox ('Menu', ['Luas Persegi', 'Luas Segitiga', 'Luas Lingkaran'])

if menu == 'Luas Persegi' :
    st.write (':blue[ini halaman untuk menghitung luas persegi]')
    st.image ('https://www.doyanblog.com/wp-content/uploads/2023/05/rumus-luas-persegi.jpg', caption='gambar dan rumus luas persegi')
    sisi = st.number_input ('silahkan masukkan sisi', min_value=0)
    if st.button('hitung'):
        Luas = sisi * sisi
        st.success (f'Luas persegi adalah {Luas}')

elif menu == 'Luas Segitiga' :
    st.write ('ini halaman untuk menghitung luas segitiga')
    st.image ('https://idschool.net/wp-content/uploads/2018/03/Rumus-Luas-Segitiga.png', caption='gambar dan rumus luas segitiga')