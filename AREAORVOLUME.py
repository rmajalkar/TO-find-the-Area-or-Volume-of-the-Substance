import streamlit as st
import math

st.set_page_config(page_title="Area & Volume Calculator", page_icon="📐")

st.title("📐 Area and Volume Calculator")
st.write("Calculate Area and Volume of Various Shapes")

shape_icons = {
    "Rectangle": "▭",
    "Square": "⬜",
    "Triangle": "🔺",
    "Circle": "⚪",
    "Parallelogram": "▱",
    "Trapezium": "⬠",
    "Ellipse": "🥚",
    "Cube": "🧊",
    "Cuboid": "📦",
    "Cylinder": "🥫",
    "Cone": "🔻",
    "Sphere": "⚽",
    "Hemisphere": "🌐",
    "Prism": "🔷"
}

shape = st.selectbox(
    "Select Shape",
    list(shape_icons.keys())
)

col1, col2 = st.columns([1,2])

with col1:
    st.markdown(f"# {shape_icons[shape]}")
    st.subheader(shape)

with col2:

    if shape == "Rectangle":
        l = st.number_input("Length", min_value=0.0)
        b = st.number_input("Breadth", min_value=0.0)
        st.info("Formula: Area = Length × Breadth")

        if st.button("Calculate"):
            st.success(f"Area = {l*b:.2f}")

    elif shape == "Square":
        s = st.number_input("Side", min_value=0.0)
        st.info("Formula: Area = Side²")

        if st.button("Calculate"):
            st.success(f"Area = {s**2:.2f}")

    elif shape == "Triangle":
        b = st.number_input("Base", min_value=0.0)
        h = st.number_input("Height", min_value=0.0)
        st.info("Formula: Area = ½ × Base × Height")

        if st.button("Calculate"):
            st.success(f"Area = {(0.5*b*h):.2f}")

    elif shape == "Circle":
        r = st.number_input("Radius", min_value=0.0)
        st.info("Formula: Area = πr²")

        if st.button("Calculate"):
            st.success(f"Area = {(math.pi*r*r):.2f}")

    elif shape == "Parallelogram":
        b = st.number_input("Base", min_value=0.0)
        h = st.number_input("Height", min_value=0.0)

        if st.button("Calculate"):
            st.success(f"Area = {(b*h):.2f}")

    elif shape == "Trapezium":
        a = st.number_input("Parallel Side A", min_value=0.0)
        b = st.number_input("Parallel Side B", min_value=0.0)
        h = st.number_input("Height", min_value=0.0)

        if st.button("Calculate"):
            area = 0.5*(a+b)*h
            st.success(f"Area = {area:.2f}")

    elif shape == "Ellipse":
        a = st.number_input("Major Radius", min_value=0.0)
        b = st.number_input("Minor Radius", min_value=0.0)

        if st.button("Calculate"):
            area = math.pi*a*b
            st.success(f"Area = {area:.2f}")

    elif shape == "Cube":
        s = st.number_input("Side", min_value=0.0)
        st.info("Formula: Volume = Side³")

        if st.button("Calculate"):
            st.success(f"Volume = {s**3:.2f}")

    elif shape == "Cuboid":
        l = st.number_input("Length", min_value=0.0)
        b = st.number_input("Breadth", min_value=0.0)
        h = st.number_input("Height", min_value=0.0)

        if st.button("Calculate"):
            st.success(f"Volume = {(l*b*h):.2f}")

    elif shape == "Cylinder":
        r = st.number_input("Radius", min_value=0.0)
        h = st.number_input("Height", min_value=0.0)
        st.info("Formula: Volume = πr²h")

        if st.button("Calculate"):
            volume = math.pi*r*r*h
            st.success(f"Volume = {volume:.2f}")

    elif shape == "Cone":
        r = st.number_input("Radius", min_value=0.0)
        h = st.number_input("Height", min_value=0.0)

        if st.button("Calculate"):
            volume = (1/3)*math.pi*r*r*h
            st.success(f"Volume = {volume:.2f}")

    elif shape == "Sphere":
        r = st.number_input("Radius", min_value=0.0)

        if st.button("Calculate"):
            volume = (4/3)*math.pi*r**3
            st.success(f"Volume = {volume:.2f}")

    elif shape == "Hemisphere":
        r = st.number_input("Radius", min_value=0.0)

        if st.button("Calculate"):
            volume = (2/3)*math.pi*r**3
            st.success(f"Volume = {volume:.2f}")

    elif shape == "Prism":
        area = st.number_input("Base Area", min_value=0.0)
        h = st.number_input("Height", min_value=0.0)

        if st.button("Calculate"):
            volume = area*h
            st.success(f"Volume = {volume:.2f}")

st.markdown("---")
st.caption("Created using Python + Streamlit + GitHub")
