import streamlit as st
import base64
from io import BytesIO
from pathlib import Path

import qrcode

st.set_page_config(page_title="Regalo de boda", page_icon="💍", layout="centered")

ENTRY_BONUS_NUMBER = "KLK6842830242"


def get_entry_qr():
    qr_image = qrcode.make(ENTRY_BONUS_NUMBER)
    qr_buffer = BytesIO()
    qr_image.save(qr_buffer, format="PNG")
    return qr_buffer.getvalue()


def show_entry_qr_button(key):
    if st.button("QR de entrada", key=key, type="tertiary", use_container_width=True):
        st.session_state[f"{key}_visible"] = True

    if st.session_state.get(f"{key}_visible", False):
        left_space, qr_column, right_space = st.columns([1, 2, 1])
        with qr_column:
            st.image(
                get_entry_qr(),
                caption=f"N.º de bono: {ENTRY_BONUS_NUMBER}",
                width=220,
            )

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #fff7f0 0%, #f8e4e1 100%);
    }
    .block-container {
        position: relative;
        z-index: 2;
        max-width: 700px;
    }
    .hero {
        padding: 4rem 1.5rem 2.5rem;
        text-align: center;
        background: rgba(255, 255, 255, 0.86);
        border: 1px solid rgba(255, 255, 255, 0.9);
        border-radius: 28px;
        box-shadow: 0 18px 45px rgba(86, 52, 53, 0.12);
    }
    .hero p {
        color: #8d5d5a;
        font-size: 1.1rem;
    }
    .hero h1 {
        color: #563435;
        font-size: 2.8rem;
        margin: 1rem 0 2rem;
    }
    .stButton > button {
        width: 220px !important;
        min-height: 205px;
        margin: 0 auto;
        padding: 4rem 1.5rem 3rem;
        border: 0;
        border-radius: 0;
        background: #d87579;
        color: #fff;
        font-size: 1.05rem;
        font-weight: 700;
        clip-path: polygon(50% 97%, 8% 53%, 5% 38%, 9% 24%, 19% 13%, 31% 11%, 41% 17%, 50% 29%, 59% 17%, 69% 11%, 81% 13%, 91% 24%, 95% 38%, 92% 53%);
        transition: transform 180ms ease, background 180ms ease;
    }
    .stButton > button:hover {
        background: #c65f68;
        transform: scale(1.05);
    }
    .stButton > button:focus-visible {
        outline: 3px solid #563435;
        outline-offset: 4px;
    }
    .stButton > button[kind="tertiary"] {
        width: 100% !important;
        min-height: 2.5rem !important;
        padding: 0.5rem 1rem !important;
        border: 1px solid #d7d9df !important;
        border-radius: 8px !important;
        background: #fff !important;
        color: #563435 !important;
        font-size: 0.9rem !important;
        clip-path: none !important;
    }
    .stButton > button[kind="tertiary"]:hover {
        background: #fff7f0 !important;
        color: #563435 !important;
        transform: none;
    }
    .photo-frame {
        position: fixed;
        inset: 0;
        z-index: 1;
        pointer-events: none;
    }
    .frame-photo {
        position: absolute;
        width: 230px;
        height: 290px;
        object-fit: cover;
        padding: 7px 7px 30px;
        background: #fff;
        border: 1px solid #ead8d2;
        box-shadow: 0 12px 28px rgba(86, 52, 53, 0.2);
        border-radius: 3px;
    }
    .photo-1 { top: 8%; left: 4%; transform: rotate(-9deg); }
    .photo-2 { top: 12%; right: 4%; transform: rotate(8deg); }
    .photo-3 { top: 48%; left: 3%; transform: rotate(6deg); }
    .photo-4 { top: 51%; right: 3%; transform: rotate(-7deg); }
    .photo-5 { bottom: 4%; left: calc(50% - 600px); transform: rotate(-5deg); }
    @media (max-width: 1280px) {
        .photo-frame { display: none; }
    }
    @media (max-width: 900px) {
        .frame-photo { width: 170px; height: 215px; padding-bottom: 22px; }
        .photo-1 { left: 1%; }
        .photo-2 { right: 1%; }
        .photo-3, .photo-4 { display: none; }
        .photo-5 { left: 5%; bottom: 2%; }
        .block-container { padding-left: 1rem; padding-right: 1rem; }
    }
    @media (max-width: 600px) {
        .frame-photo { width: 120px; height: 155px; padding: 4px 4px 16px; }
        .photo-1 { top: 5%; }
        .photo-2 { top: 7%; }
        .photo-5 { display: none; }
        .hero h1 { font-size: 2.2rem; }
        .stButton > button { width: 150px !important; min-height: 155px; padding: 3rem 0.5rem 2rem; font-size: 0.9rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <h1>Que se casan ¡LOL!</h1>
        <p>Después del fiestón que nos vamos a pegar para celebrar lo enamorados que estáis, os toca disfrutar del MEJOR PAÍS DEL MUNDO. Queremos tener un detallito con vosotros para que podáis disfrutar juntos por allí. Como sabemos que cada personita vive los viajes de una manera y no queremos influir en vuestro nivel de ansiedad, os damos la opción de dejaros sorprender (os daremos la información justa y necesaria), o la opción de conocer todos los detalles de nuestro regalito con antelación. Está en vuestra mano decidir, pulsad el botón con el que os sintáis más cómodos.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

photo_dir = Path(__file__).parent / "assets" / "fotos"
photo_paths = sorted(
    path
    for path in photo_dir.glob("*")
    if path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
)

if photo_paths:
    photo_tags = []
    for index, photo_path in enumerate(photo_paths[:5], start=1):
        encoded_photo = base64.b64encode(photo_path.read_bytes()).decode("ascii")
        mime_type = "image/jpeg" if photo_path.suffix.lower() in {".jpg", ".jpeg"} else f"image/{photo_path.suffix.lower().lstrip('.') }"
        photo_tags.append(
            f'<img class="frame-photo photo-{index}" src="data:{mime_type};base64,{encoded_photo}" alt="Foto de la boda">'
        )
    st.markdown(f'<div class="photo-frame">{"".join(photo_tags)}</div>', unsafe_allow_html=True)
else:
    st.caption("Añade tus fotos en assets/fotos para verlas aquí.")

left_button, right_button = st.columns([1, 1], gap="large")

with left_button:
    wants_to_know = st.button("Quiero  \nsaber", use_container_width=True)

with right_button:
    wants_a_surprise = st.button("Quiero  \nsorpresa", use_container_width=True)

if wants_to_know:
    st.session_state["show_know_details"] = True
    st.session_state["show_surprise_details"] = False

if wants_a_surprise:
    st.session_state["show_surprise_details"] = True
    st.session_state["show_know_details"] = False

if st.session_state.get("show_know_details", False):
    location_url = "https://www.google.com/maps/place/Manyo+Club+(Toyosu)/@35.6464135,139.7830627,17z/data=!4m21!1m11!3m10!1s0x601889a7257fa2b3:0x4f16b5579a219ae8!2sManyo+Club+(Toyosu)!5m2!4m1!1i2!8m2!3d35.6461872!4d139.7831588!10e5!16s%2Fg%2F11kqgnd8c2!3m8!1s0x601889a7257fa2b3:0x4f16b5579a219ae8!5m2!4m1!1i2!8m2!3d35.6461872!4d139.7831588!16s%2Fg%2F11kqgnd8c2?entry=ttu&g_ep=EgoyMDI2MDkyMi4wIKXMDSoASAFQAw%3D%3D"

    with st.expander("Detalles del regalo", expanded=True):
        st.markdown(
            """
            Vais a pasar una velada relajante en el **Onsen de Manyo Club (Toyosu)**. Podréis estar el tiempo que queráis en el Onsen, donde tendréis que estar separados. Juntos podéis disfrutar del Onsen de pies que tienen en la última planta. También tenéis incluida una cena, así que a poneros como bolitas rechonchas y japonesas.

            **¿Qué necesitáis?**

            - Comprar pegatinas para tapar tatuajes y llevarlas ya puestas. Directamente decir allí que no tenéis (malotes jeje).
            - Cuando lleguéis os darán una yukata para que podáis ir cómodos por las instalaciones; no tenéis que preocuparos del vestuario.
            - Podéis ir a la hora que queráis. Calculad cuánto tiempo más o menos queréis pasar en el Onsen y contad con el tiempo de la cena para que no os cierren.

            **Horario de la cena:** de 17:00 a 22:00.

            Luego tenéis tiempo para seguir en las instalaciones si aún os habéis quedado con ganas.
            """
        )
        st.link_button("Ubicación", location_url, use_container_width=True)
        show_entry_qr_button("know_entry_qr")

    if st.session_state.get("show_surprise_details", False):
        st.success("¡La sorpresa está en camino!")
        show_entry_qr_button("surprise_entry_qr")
