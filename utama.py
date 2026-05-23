import streamlit as st
import pandas as pd
import os

# ==========================
# KONFIGURASI WEBSITE
# ==========================
st.set_page_config(
    page_title="Toko Anggrek 🌸",
    page_icon="🌸",
    layout="wide"
)

# ==========================
# STYLE / BACKGROUND
# ==========================
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(
135deg,
#fff0f5,
#fff8dc,
#e0f7fa
);
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

h1{
text-align:center;
color:#db7093;
font-size:55px;
}

div[data-testid="column"]{
background:white;
padding:20px;
border-radius:25px;
box-shadow:0px 8px 20px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ==========================
# JUDUL
# ==========================
st.title("🌸 Toko Anggrek")

st.markdown(
    "<p style='text-align:center;font-size:18px;color:#6c757d;'>"
    "Menyediakan berbagai anggrek cantik dan segar untuk dekorasi rumahmu ✨"
    "</p>",
    unsafe_allow_html=True
)

st.divider()

# ==========================
# FILE DATA
# ==========================
file_data = "data_anggrek.csv"

if not os.path.exists(file_data):
    st.error("❌ File 'data_anggrek.csv' tidak ditemukan!")
    st.stop()

df = pd.read_csv(file_data)

kategori_list = df["kategori"].unique()

# ==========================
# PRODUK
# ==========================
for kat in kategori_list:

    st.header(f"🌿 Kategori: {kat.title()}")

    data_kat = df[df["kategori"] == kat]
    cols = st.columns(3)

    for index, row in data_kat.reset_index().iterrows():

        with cols[index % 3]:

            # ==========================
            # FOTO
            # ==========================
            nama_foto = os.path.join(
                os.path.dirname(__file__),
                str(row["foto"]).strip()
            )

            if os.path.exists(nama_foto):
                st.image(nama_foto, use_container_width=True)
            else:
                st.caption(f"📸 Foto tidak ditemukan: {row['foto']}")

            # ==========================
            # NAMA PRODUK
            # ==========================
            st.subheader(str(row["nama"]).title())

            # ==========================
            # HARGA
            # ==========================
            st.markdown(f"### 💸 Rp {row['harga']:,}")

            # ==========================
            # STATUS
            # ==========================
            st.success(f"Status: {row['status']}")

            # ==========================
            # BUTTON
            # ==========================
            if st.button(
                f"🛒 Order {row['nama']}",
                key=f"order_{kat}_{index}"
            ):
                st.success("🌸 Pesanan berhasil ditambahkan!")

    st.divider()

# ==========================
# FOOTER
# ==========================
st.subheader("📍 Lokasi & Pemesanan")

col1, col2 = st.columns(2)

with col1:
    st.info("""
🏪 **Toko Anggrek**

Jl. Melati Indah No. 77  
Kota Bunga, Indonesia 🇮🇩
""")

with col2:
    no_hp = "62895400551222"

    pesan = "Halo! Saya mau pesan anggrek 🌸"

    link = f"https://wa.me/{no_hp}?text={pesan.replace(' ','%20')}"

    st.link_button("📱 Pesan WhatsApp", link)

st.caption("© 2026 Toko Anggrek — Made with Love 🌸")
