import streamlit as st

st.set_page_config(page_title="Motion Compare UI", layout="wide")
st.title("SMPL-X Motion Comparison Tool")

# ==============================
# CONFIG: Video paths (relative paths)
# ==============================
video_original = "originalvideo.mp4"
video_gv       = "gv.mp4"
video_sg       = "sg.mp4"

# ==============================
# Helper to show 2 videos side-by-side
# ==============================
def two_videos(left_title, left_path, right_title, right_path):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(left_title)
        st.video(left_path)
    with col2:
        st.subheader(right_title)
        st.video(right_path)

# ==============================
# UI Logic
# ==============================
mode = st.selectbox(
    "Select Comparison Mode:",
    [
        "Original vs GV",
        "Original vs SG",
        "GV vs SG",
        "Original vs GV vs SG"
    ]
)

if mode == "Original vs GV":
    two_videos("Original", video_original, "Gaussian–Volterra (GV)", video_gv)

elif mode == "Original vs SG":
    two_videos("Original", video_original, "Savitzky–Golay (SG)", video_sg)

elif mode == "GV vs SG":
    two_videos("Gaussian–Volterra (GV)", video_gv, "Savitzky–Golay (SG)", video_sg)

elif mode == "Original vs GV vs SG":
    st.subheader("Three-way Comparison")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.video(video_original)
        st.caption("Original")
    with col2:
        st.video(video_gv)
        st.caption("GV")
    with col3:
        st.video(video_sg)
        st.caption("SG")
