import streamlit as st

def show():

    st.title("♿ Accessibility Reviews")

    st.markdown(
        "Explore accessibility ratings for different public places."
    )

    st.divider()

    # ─────────────────────────────────────────────
    # SAMPLE DATA
    # ─────────────────────────────────────────────

    places = [
        {
            "name": "Public Library",
            "score": "4.8/5",
            "badge": "🏆 Excellent",
            "ramp": "★★★★★",
            "washroom": "★★★★★",
            "elevator": "★★★★☆",
            "space": "★★★★★",
            "review": "One of the best accessible venues."
        },

        {
            "name": "Metro Station",
            "score": "3.5/5",
            "badge": "⚠️ Good",
            "ramp": "★★★★☆",
            "washroom": "★★★☆☆",
            "elevator": "★★★★☆",
            "space": "★★★☆☆",
            "review": "Mostly accessible, rush hour is tight."
        },

        {
            "name": "Central Park",
            "score": "2.8/5",
            "badge": "⚠️ Fair",
            "ramp": "★★★☆☆",
            "washroom": "★★☆☆☆",
            "elevator": "N/A",
            "space": "★★★★☆",
            "review": "Outdoor movement is decent but facilities are limited."
        }
    ]

    # ─────────────────────────────────────────────
    # DISPLAY REVIEWS
    # ─────────────────────────────────────────────

    for place in places:

        with st.container(border=True):

            col1, col2 = st.columns([4, 1])

            with col1:
                st.subheader(f"📍 {place['name']}")

            with col2:
                st.metric("Score", place["score"])

            st.caption(place["badge"])

            st.divider()

            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.metric("♿ Ramp", place["ramp"])

            with c2:
                st.metric("🚻 Washroom", place["washroom"])

            with c3:
                st.metric("🛗 Elevator", place["elevator"])

            with c4:
                st.metric("📏 Space", place["space"])

            st.markdown(
                f"**Review:** {place['review']}"
            )

            st.write("")

    # ─────────────────────────────────────────────
    # ADD REVIEW SECTION
    # ─────────────────────────────────────────────

    st.divider()

    st.subheader("➕ Add Accessibility Review")

    place_name = st.text_input("Place Name")

    ramp = st.slider("Ramp Accessibility", 1, 5, 3)

    washroom = st.slider("Washroom Accessibility", 1, 5, 3)

    elevator = st.slider("Elevator Availability", 1, 5, 3)

    space = st.slider("Movement Space", 1, 5, 3)

    review = st.text_area("Write a Review")

    if st.button("Submit Review"):

        avg_score = round(
            (ramp + washroom + elevator + space) / 4,
            1
        )

        st.success(
            f"Review submitted successfully! Accessibility Score: {avg_score}/5"
        )