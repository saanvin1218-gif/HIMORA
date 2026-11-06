import streamlit as st

# ==========================================
# HIMORA - LADAKH TOURISM APPLICATION
# ==========================================

st.set_page_config(
    page_title="HIMORA | Discover Ladakh",
    page_icon="🏔️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ------------------ DESIGN ------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

.stApp {
    background: linear-gradient(180deg, #eff8f8, #ffffff);
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: #183f4b;
}

.brand {
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    font-weight: bold;
    color: #183f4b;
    letter-spacing: 2px;
}

.tagline {
    color: #68848a;
    letter-spacing: 3px;
    font-size: 11px;
    font-weight: bold;
}

.hero {
    background:
    linear-gradient(90deg, rgba(14,43,54,.85), rgba(14,43,54,.3)),
    url("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1400");
    background-size: cover;
    background-position: center;
    border-radius: 22px;
    padding: 40px 25px;
    color: white;
    min-height: 230px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}

.hero h1 {
    color: white;
    font-family: 'Playfair Display', serif;
    font-size: 38px;
}

.hero p {
    color: white;
}

.card {
    background: white;
    border: 1px solid #e3eceb;
    border-radius: 17px;
    padding: 19px;
    margin: 12px 0;
    box-shadow: 0 5px 18px rgba(20,60,70,.05);
}

.small {
    color: #718489;
    font-size: 14px;
}

.pill {
    background: #e5f1ef;
    color: #315d62;
    padding: 5px 11px;
    border-radius: 20px;
    font-size: 12px;
}

div.stButton > button {
    border-radius: 12px;
    font-weight: bold;
    min-height: 43px;
}

div.stButton > button[kind="primary"] {
    background: #194a56;
    border-color: #194a56;
}

.footer {
    text-align: center;
    color: #849497;
    font-size: 12px;
    padding: 25px;
}

/* HIMORA: targeted contrast fixes */

/* Keep normal page text dark, but do not override hero text or button labels. */
.stApp .stMarkdown p,
.stApp .stCaption,
.stApp label,
.stTabs [data-baseweb="tab"] {
    color: #263F46;
}

/* Hero text must stay white over the dark image overlay. */
.stApp .hero,
.stApp .hero h1,
.stApp .hero p {
    color: #FFFFFF !important;
}

/* Make both regular buttons and form-submit buttons readable. */
.stButton > button,
.stFormSubmitButton > button {
    background-color: #244C55 !important;
    color: #FFFFFF !important;
    border: 1px solid #244C55 !important;
    font-weight: 700 !important;
}

/* Streamlit places button labels inside paragraph/span elements. */
.stButton > button *,
.stFormSubmitButton > button * {
    color: #FFFFFF !important;
}

/* Keep the red primary login button and its label readable. */
.stFormSubmitButton > button[kind="primary"] {
    background-color: #D94355 !important;
    border-color: #D94355 !important;
}

/* Inputs and their labels */
.stTextInput label,
.stSelectbox label,
.stMultiSelect label,
.stSlider label {
    color: #263F46 !important;
}
.stTextInput input {
    color: #263F46 !important;
}

/* FIX: Make destination names and headings visible */

.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4 {
    color: #183F4B !important;
}

/* Destination names inside Explore expanders */
.stApp [data-testid="stExpander"] summary,
.stApp [data-testid="stExpander"] summary p,
.stApp [data-testid="stExpander"] summary span {
    color: #183F4B !important;
}

/* Names inside destination cards */
.stApp .card h3 {
    color: #183F4B !important;
}

/* Preserve white hero text */
.stApp .hero h1,
.stApp .hero p {
    color: #FFFFFF !important;
}

</style>
""", unsafe_allow_html=True)


# ------------------ SESSION DATA ------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = "Explorer"


# ------------------ DESTINATIONS ------------------

destinations = [
    {
        "name": "Pangong Tso",
        "image": "https://b2bzend.s3.ap-south-1.amazonaws.com/img/4539/package/images/treasures-of-ladakh_1709633035",
        "category": "Lake",
        "emoji": "🏞️",
        "description": "A spectacular high-altitude lake famous for its changing shades of blue.",
        "best": "Generally May to September, subject to conditions.",
        "duration": "Full-day excursion or longer."
    },
    {
        "name": "Nubra Valley",
        "image": "https://media.assettype.com/outlooktraveller/import/outlooktraveller/public/uploads/articles/stays/shutterstock_2273585477.png?ar=40%3A21&auto=format%2Ccompress&enlarge=true&mode=crop&ogImage=true&overlay=false&overlay_position=bottom&overlay_width=100&w=1200",
        "category": "Valley",
        "emoji": "🏜️",
        "description": "A beautiful cold desert surrounded by dramatic mountains and villages.",
        "best": "Generally May to September.",
        "duration": "Allow 2 days for a relaxed visit."
    },
    {
        "name": "Thiksey Monastery",
        "image": "https://images.nativeplanet.com/img/2025/05/untitleddesign-2025-05-28t205935-824-1748446575.jpg",
        "category": "Monastery",
        "emoji": "🏯",
        "description": "A magnificent hilltop monastery known for its architecture and Buddhist heritage.",
        "best": "Year-round, depending on local conditions.",
        "duration": "1–2 hours."
    },
    {
        "name": "Shanti Stupa",
        "image": "https://images.nativeplanet.com/img/2025/05/untitleddesign-2025-05-28t205935-824-1748446575.jpg",
        "category": "Heritage",
        "emoji": "☀️",
        "description": "A peaceful white-domed monument overlooking Leh and the surrounding mountains.",
        "best": "May to October is generally easier.",
        "duration": "Around 1 hour."
    },
    {
        "name": "Alchi Monastery",
        "image": "https://images.nativeplanet.com/img/2025/05/untitleddesign-2025-05-28t205935-824-1748446575.jpg",
        "category": "Monastery",
        "emoji": "🎨",
        "description": "A historic monastery famous for its beautiful ancient wall paintings.",
        "best": "Spring to autumn, subject to access.",
        "duration": "1–2 hours, plus travel."
    },
    {
        "name": "Tso Moriri",
        "image": "https://b2bzend.s3.ap-south-1.amazonaws.com/img/4539/package/images/treasures-of-ladakh_1709633035",
        "category": "Lake",
        "emoji": "💧",
        "description": "A remote high-altitude lake surrounded by the landscapes of Changthang.",
        "best": "Usually summer, depending on access.",
        "duration": "A separate multi-day excursion."
    },
    {
        "name": "Turtuk",
        "image": "https://media.assettype.com/outlooktraveller/import/outlooktraveller/public/uploads/articles/stays/shutterstock_2273585477.png?ar=40%3A21&auto=format%2Ccompress&enlarge=true&mode=crop&ogImage=true&overlay=false&overlay_position=bottom&overlay_width=100&w=1200",
        "category": "Village",
        "emoji": "🌳",
        "description": "A culturally distinctive village known for Balti heritage and apricot orchards.",
        "best": "Generally May to September.",
        "duration": "A full-day visit from Nubra."
    },
    {
        "name": "Magnetic Hill",
        "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1200",
        "category": "Natural Wonder",
        "emoji": "🧲",
        "description": "A famous optical illusion that makes vehicles appear to roll uphill.",
        "best": "Check local road and weather conditions.",
        "duration": "15–30 minutes."
    }
]


# ------------------ LOGIN PAGE ------------------

if not st.session_state.logged_in:

    st.markdown(
        '<div class="brand">HIMORA</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="tagline">DISCOVER • EXPERIENCE • EXPLORE</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown("""
    <div class="hero">
        <h1>Your journey<br>begins here.</h1>
        <p>Discover the extraordinary beauty,
        culture and nature of Ladakh.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("Welcome, Explorer! 👋")
    st.caption("Enter your details to explore HIMORA.")

    with st.form("login_form"):

        name = st.text_input(
            "Your name",
            placeholder="Enter your name"
        )

        email = st.text_input(
            "Email address",
            placeholder="Enter your email"
        )

        login = st.form_submit_button(
            "Explore HIMORA →",
            type="primary",
            use_container_width=True
        )

        if login:
            st.session_state.username = name.strip() or "Explorer"
            st.session_state.logged_in = True
            st.rerun()

    if st.button("Continue as Guest", use_container_width=True):
        st.session_state.username = "Explorer"
        st.session_state.logged_in = True
        st.rerun()

    st.caption("Student demonstration login. No real account is created.")

    st.stop()


# ------------------ MAIN APP ------------------

col1, col2 = st.columns([3, 1])

with col1:
    st.markdown(
        '<div class="brand">HIMORA</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="tagline">YOUR LADAKH EXPERIENCE</div>',
        unsafe_allow_html=True
    )

with col2:
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()


st.write("")

home, explore, discover, planner, eco = st.tabs([
    "🏠 Home",
    "🧭 Explore",
    "✨ Discover",
    "📅 Planner",
    "🌿 Eco"
])


# ==========================================
# PAGE 1 - HOME
# ==========================================

with home:

    st.subheader(
        f"Hello, {st.session_state.username}! 👋"
    )

    st.markdown("""
    <div class="hero">
        <h1>Find your own<br>way through Ladakh.</h1>
        <p>Mountains, memories and experiences
        waiting to be discovered.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("Explore something extraordinary")

    c1, c2, c3 = st.columns(3)

    c1.metric("Destinations", "8")
    c2.metric("Nature highlights", "6")
    c3.metric("Experiences", "5")

    st.write("")

    st.subheader("Popular destinations")

    for d in destinations[:3]:

        st.image(d["image"], use_container_width=True)
        st.markdown(f"""
        <div class="card">
            <span class="pill">{d['category']}</span>
            <h3>{d['emoji']} {d['name']}</h3>
            <p class="small">{d['description']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "Travel tip: Spend at least 48 hours acclimatising "
        "in Leh before travelling to higher-altitude areas."
    )


# ==========================================
# PAGE 2 - EXPLORE
# ==========================================

with explore:

    st.subheader("Explore Ladakh 🏔️")

    st.write(
        "Discover breathtaking destinations, "
        "historic sites and hidden gems."
    )

    category = st.selectbox(
        "Filter destinations",
        [
            "All",
            "Lake",
            "Valley",
            "Monastery",
            "Heritage",
            "Village",
            "Natural Wonder"
        ]
    )

    search = st.text_input(
        "Search a destination",
        placeholder="Search Pangong, Nubra, Turtuk..."
    )

    for d in destinations:

        category_match = (
            category == "All" or d["category"] == category
        )

        search_match = (
            search.lower() in d["name"].lower()
            or search.lower() in d["description"].lower()
        )

        if category_match and search_match:

            with st.expander(
                f"{d['emoji']} {d['name']} — {d['category']}"
            ):

                st.image(d["image"], use_container_width=True)
                st.write(d["description"])

                st.markdown(
                    f"**Best time:** {d['best']}"
                )

                st.markdown(
                    f"**Suggested duration:** {d['duration']}"
                )


# ==========================================
# PAGE 3 - DISCOVER LADAKH
# ==========================================

with discover:

    st.subheader("Discover the soul of Ladakh")

    st.write(
        "Explore the traditions, flavours, "
        "heritage and biodiversity of this unique region."
    )

    culture, food, biodiversity = st.tabs([
        "🎭 Culture",
        "🍲 Cuisine",
        "🌸 Biodiversity"
    ])

    # CULTURE

    with culture:

        st.image(
            "https://images.nativeplanet.com/img/2025/05/untitleddesign-2025-05-28t205935-824-1748446575.jpg",
            caption="Monastery architecture in the Himalayan landscape",
            use_container_width=True
        )
        st.image(
            "https://media.assettype.com/outlooktraveller/import/outlooktraveller/public/uploads/articles/stays/shutterstock_2273585477.png?ar=40%3A21&auto=format%2Ccompress&enlarge=true&mode=crop&ogImage=true&overlay=false&overlay_position=bottom&overlay_width=100&w=1200",
            caption="A monastery landscape in Ladakh",
            use_container_width=True
        )

        culture_data = [
            ("🎭 Festivals",
             "Monastic festivals feature traditional masked dances, music and community celebrations."),

            ("🏯 Monasteries",
             "Monasteries preserve Buddhist art, architecture, history and spiritual traditions."),

            ("🧵 Handicrafts",
             "Traditional weaving, wool products, woodwork and locally made crafts."),

            ("👘 Traditional clothing",
             "Explore traditional Ladakhi garments, including the goncha, and their regional variations."),

            ("🗣️ Languages",
             "Ladakh has a rich linguistic landscape, including Ladakhi, Balti and Purgi."),

            ("🌾 Lifestyle",
             "Learn about traditional farming, pastoral life, apricot cultivation and mountain communities.")
        ]

        for title, description in culture_data:

            st.markdown(f"""
            <div class="card">
                <h3>{title}</h3>
                <p class="small">{description}</p>
            </div>
            """, unsafe_allow_html=True)

    # CUISINE

    with food:

        food_col1, food_col2 = st.columns(2)
        with food_col1:
            st.image(
                "https://static.thehosteller.com/blogimage/image-1742977493640.jpg",
                caption="Momos and thukpa",
                use_container_width=True
            )
        with food_col2:
            st.image(
                "https://media.assettype.com/outlooktraveller/2024-01/25afc7e2-463d-4d85-9683-c23ecda3f4c6/shutterstock_708210952.jpg",
                caption="A spread of regional dishes",
                use_container_width=True
            )

        food_data = [
            ("🥣 Thukpa",
             "A warming noodle soup with vegetables and sometimes meat."),

            ("🥟 Momos",
             "Popular steamed dumplings served with chutney."),

            ("🍲 Skyu",
             "A traditional Ladakhi stew prepared with small pieces of dough and vegetables."),

            ("🍞 Khambir",
             "Traditional round whole-wheat bread."),

            ("🫖 Butter Tea",
             "Traditional tea prepared with tea leaves, butter and salt."),

            ("🍑 Apricots",
             "An important local fruit, enjoyed fresh, dried and in regional products.")
        ]

        for title, description in food_data:

            st.markdown(f"""
            <div class="card">
                <h3>{title}</h3>
                <p class="small">{description}</p>
            </div>
            """, unsafe_allow_html=True)

    # BIODIVERSITY

    with biodiversity:

        nature_col1, nature_col2 = st.columns(2)
        with nature_col1:
            st.image(
                "https://media2.thrillophilia.com/images/photos/000/379/786/original/1646117020_Snow_Leopard.jpg?dpr=1.5&h=450&w=753",
                caption="Snow leopard",
                use_container_width=True
            )
        with nature_col2:
            st.image(
                "https://i.assetzen.net/i/EhrqKCT5iR3w/w%3A1920/h%3A/q%3A70.jpg",
                caption="Wildlife of the high mountains",
                use_container_width=True
            )

        nature_data = [
            ("🌸 Himalayan Blue Poppy",
             "A beautiful alpine flower associated with high mountain habitats."),

            ("🌿 Sea Buckthorn",
             "A hardy shrub with bright orange berries, valued for local products."),

            ("🐆 Snow Leopard",
             "An elusive high-altitude predator and an important conservation symbol."),

            ("🦌 Kiang",
             "The Tibetan wild ass, found across parts of the Changthang plateau."),

            ("🦢 Black-necked Crane",
             "A rare high-altitude wetland bird that needs protected breeding habitats."),

            ("🐐 Himalayan Ibex",
             "A wild mountain goat adapted to steep rocky terrain.")
        ]

        for title, description in nature_data:

            st.markdown(f"""
            <div class="card">
                <h3>{title}</h3>
                <p class="small">{description}</p>
            </div>
            """, unsafe_allow_html=True)

        st.warning(
            "Observe wildlife from a distance. Never feed animals "
            "or pick wild plants."
        )


# ==========================================
# PAGE 4 - PERSONAL TRIP PLANNER
# ==========================================

with planner:

    st.subheader("Your Personal Trip Planner 🧭")

    st.write(
        "Create a day-by-day journey according to "
        "your available time and interests."
    )

    days = st.slider(
        "How many days are you visiting Ladakh?",
        min_value=3,
        max_value=8,
        value=5
    )

    interests = st.multiselect(
        "Choose your interests",
        [
            "Nature and lakes",
            "Culture and monasteries",
            "Local cuisine",
            "Photography",
            "Villages and heritage"
        ],
        default=["Nature and lakes", "Culture and monasteries"]
    )

    pace = st.select_slider(
        "Choose your travel pace",
        options=["Relaxed", "Balanced", "Full days"],
        value="Balanced"
    )

    # Every day has suggested activities and meal stops.
    itinerary = [
        {
            "day": "Day 1 — Arrival in Leh",
            "events": [
                ("Arrival", "Arrive in Leh and settle in."),
                ("Afternoon", "Rest and allow your body to acclimatise."),
                ("Evening", "Enjoy a light dinner at a local restaurant and rest.")
            ]
        },
        {
            "day": "Day 2 — Acclimatisation",
            "events": [
                ("Morning", "Rest, hydrate and avoid strenuous activity."),
                ("Afternoon", "Continue acclimatisation. Take only a gentle stroll if feeling well."),
                ("Evening", "Try local cuisine such as thukpa or skyu.")
            ]
        },
        {
            "day": "Day 3 — Discover Leh",
            "events": [
                ("8:30 AM", "Breakfast at a local cafe."),
                ("10:00 AM", "Explore Leh Palace and its historical surroundings."),
                ("1:00 PM", "Lunch at a local restaurant in Leh."),
                ("3:00 PM", "Visit Shanti Stupa, depending on how you feel."),
                ("6:00 PM", "Explore Leh Market and enjoy dinner.")
            ]
        },
        {
            "day": "Day 4 — Monastery Trail",
            "events": [
                ("8:00 AM", "Breakfast in Leh."),
                ("9:00 AM", "Visit Thiksey Monastery."),
                ("12:30 PM", "Lunch at a local restaurant along the route."),
                ("2:00 PM", "Visit Hemis Monastery if access and time permit."),
                ("5:30 PM", "Return to Leh and have dinner.")
            ]
        },
        {
            "day": "Day 5 — Sham Valley",
            "events": [
                ("8:00 AM", "Breakfast in Leh."),
                ("9:00 AM", "Visit the Indus–Zanskar confluence."),
                ("12:30 PM", "Enjoy lunch at a local restaurant."),
                ("2:00 PM", "Explore Alchi Monastery, subject to access."),
                ("5:30 PM", "Return to Leh.")
            ]
        },
        {
            "day": "Day 6 — Nubra Valley",
            "events": [
                ("7:00 AM", "Begin the journey only if road and health conditions permit."),
                ("11:00 AM", "Enjoy scenic stops along the route."),
                ("1:00 PM", "Lunch at a local eatery in Nubra."),
                ("3:00 PM", "Explore Diskit or Hunder, depending on access."),
                ("Evening", "Dinner at a local restaurant.")
            ]
        },
        {
            "day": "Day 7 — Local Experiences",
            "events": [
                ("8:00 AM", "Breakfast at a local cafe."),
                ("9:30 AM", "Explore village life or visit Turtuk if permits and time allow."),
                ("1:00 PM", "Enjoy a local lunch."),
                ("3:00 PM", "Discover Balti culture, crafts and apricot orchards."),
                ("Evening", "Follow a locally confirmed return or onward travel plan.")
            ]
        },
        {
            "day": "Day 8 — Farewell Ladakh",
            "events": [
                ("Morning", "Enjoy a relaxed morning and nearby sightseeing."),
                ("12:30 PM", "Have a final Ladakhi lunch."),
                ("Afternoon", "Explore local markets and handicrafts."),
                ("Evening", "Allow enough time for onward travel.")
            ]
        }
    ]

    if st.button(
        "✨ Generate My Trip",
        type="primary",
        use_container_width=True
    ):

        st.markdown("## Your Ladakh Itinerary")

        st.write(f"**Duration:** {days} days")
        st.write(f"**Travel pace:** {pace}")

        st.write(
            "**Interests:** " +
            (", ".join(interests) if interests else "General exploration")
        )

        for day in itinerary[:days]:

            with st.expander(day["day"], expanded=True):

                for time, activity in day["events"]:

                    st.markdown(
                        f"**{time}**  \n{activity}"
                    )

                    st.divider()

        st.success(
            "Your personalised sample itinerary has been generated!"
        )

        st.caption(
            "These are illustrative timings and dining suggestions, "
            "not verified live schedules or restaurant bookings."
        )

    st.info(
        "Safety reminder: Allow at least 48 hours to acclimatise "
        "in Leh before heading to higher-altitude destinations. "
        "Check current local travel advice before finalising routes."
    )


# ==========================================
# PAGE 5 - ECO EXPLORER
# ==========================================

with eco:

    st.subheader("Eco Explorer 🌿")

    st.image(
        "https://media2.thrillophilia.com/images/photos/000/379/786/original/1646117020_Snow_Leopard.jpg?dpr=1.5&h=450&w=753",
        caption="Protecting the wildlife and fragile habitats of Ladakh",
        use_container_width=True
    )

    st.markdown("""
    <div class="hero">
        <h1>Leave only<br>good memories.</h1>
        <p>Explore responsibly. Protect the beauty of Ladakh.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("Responsible Traveller Challenge")

    st.write(
        "Select the actions you promise to follow "
        "during your journey."
    )

    tips = [
        "Carry a reusable water bottle.",
        "Avoid single-use plastics.",
        "Never litter in natural areas.",
        "Do not disturb wildlife.",
        "Never pick wildflowers.",
        "Respect local traditions and monasteries.",
        "Support local businesses and artisans."
    ]

    score = 0

    for i, tip in enumerate(tips):

        if st.checkbox(tip, key=f"eco_{i}"):
            score += 1

    st.progress(score / len(tips))

    st.metric(
        "Responsible travel score",
        f"{score}/{len(tips)}"
    )

    if score == len(tips):
        st.success("Amazing! You're ready to be a responsible explorer.")

    st.caption(
        "This is an educational checklist, not an official "
        "environmental certification."
    )


# ------------------ FOOTER ------------------

st.markdown("""
<div class="footer">
    HIMORA · DISCOVER LADAKH<br>
    A STUDENT TOURISM APP PROTOTYPE<br>
    Discover responsibly. Travel thoughtfully.
</div>
""", unsafe_allow_html=True)
