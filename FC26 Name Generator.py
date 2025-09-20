import random
import csv
import pandas as pd
import requests
import streamlit as st  # if making web app
# or import tkinter for GUI

# ---> Expand the sample lists above into your big lists
first_names = [

    "Diego", "Lucas", "Jamal", "Rafael", "Tariq", "Emil", "Kaito", "Omar", "Noah", "Liam",
    "Henry", "Mohamed", "Yuki", "Mateo", "Ethan", "Sebastian", "Kai", "Marcus", "Jaden", "Theo",
    "Finn", "Adrian", "Leon", "Ali", "Hugo", "Marcos", "Santiago", "Arlo", "Zane", "Elias",
    "Victor", "Isaac", "Luka", "Julian", "Enzo", "Axel", "Remy", "Omarion", "Dario", "Thierry",
    "Malik", "Jace", "Rowan", "Bjorn", "Cassius", "Dante", "Kian", "Niall", "Rocco", "Tobias",
    "Cristian", "Declan", "Giovanni", "Raheem", "Aarav", "Mustafa", "Giannis", "Nico", "Andres", "Bruno",
    "Callum", "Ismael", "Zion", "Luciano", "Keanu", "Amir", "Fabian", "Jayden", "Bastian", "Dragan",
    "Elian", "Ignacio", "Samir", "Jordi", "Denzel", "Khalil", "Maxim", "Anwar", "Jerome", "Nelson",
    "Otis", "Harvey", "Zaki", "Faris", "Arman", "Kenji", "Hamza", "Imran", "Joaquin", "Valentin",
    "Rayan", "Eren", "Milan", "Esteban", "Rami", "Benoit", "Cesar", "Damian", "Ezio", "Alessio",
    "Franco", "Kareem", "Idris", "Tarique", "Yassine", "Viktor", "Haris", "Mehdi", "Luc", "Toma",
    "Rafael", "Musa", "Zen", "Eli", "Cristiano", "Ezequiel", "Mahmoud", "Mahir", "Arda", "Onur",
    "Aziz", "Bekir", "Osman", "Cenk", "Yunus", "Batuhan", "Reza", "Aryan", "Dariush", "Sina",
    "Kian", "Amjad", "Bilal", "Nizar", "Zubair", "Qasim", "Ibrahim", "Jibril", "Salim", "Yahya",
    "Rashid", "Tamer", "Emre", "Ferdi", "Hakan", "Kenan", "Suat", "Taylan", "Umut", "Volkan",
    "Yasin", "Leandro", "Thiago", "Gabriel", "Vinicius", "Pedro", "Rony", "Anderson", "Marquinhos", "Paulo",
    "Renan", "Wesley", "Lucio", "Antonio", "Douglas", "Felipe", "Rui", "Tiago", "Joao", "Mateus",
    "Guilherme", "Adriano", "Miguel", "Daniel", "Ivan", "Alexis", "Loic", "Jordan", "Killian", "Adrien",
    "Mathis", "Tom", "Clément", "Florian", "Benjamin", "Nicolas", "Lucas", "Maxence", "Alexandre", "Enzo",
    "Aymeric", "Julien", "Gael", "Kylian", "Amine", "Youssef", "Anas", "Walid", "Zakaria", "Abdellah",
    "Aymen", "Karim", "Aliou", "Habib", "Mame", "Cheikh", "Pape", "Naby", "Issa", "Souleymane",
    "Mouhamed", "Abdou", "Kouame", "Jean", "Junior", "Serge", "Franck", "Wilfried", "Maxwel", "Kevin",
    "Bryan", "Elvis", "Freddy", "Joel", "Chris", "Justin", "Nathan", "Trevor", "Zeke", "Devon",
    "Jamal", "Clarence", "Ronnie", "Luther", "Corey", "Tyson", "Lamont", "Terrence", "Darnell", "Travis",
    "Shawn", "Rashawn", "Demetrius", "Leonard", "Malachi", "Darius", "Tyrone", "Deandre", "Maurice", "Lamar",
    "Kwame", "Tavon", "Jalen", "Antwan", "Daquan", "Marquis", "Deshawn", "Javon", "Kaleb", "Tyrese",
    "Zayden", "Emmitt", "Omari", "Nasir", "Zaire", "Micah", "Makai", "Nehemiah", "Cassian", "Dimitri",
    "Orion", "Caius", "Alaric", "Zephyr", "Lazaro", "Santino", "Kairo", "Romeo", "Jairo", "Matias",
    "Aurelio", "Elias", "Niklas", "Yannick", "Lorenz", "Tim", "Moritz", "Fabio", "Pascal", "Jan",
    "Timo", "Sven", "Marco", "Philipp", "Rene", "Bastian", "Dominik", "Julian", "Manuel", "Stefan",
    "Hans", "Erik", "Lukas", "Tobias", "Martin", "Daniel", "Andreas", "Florian", "Christian", "Rafael"

]  # ~300
last_names = [
"Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Campbell", "Mitchell", "Carter", "Roberts", "Edwards", "Collins", "Rivera", "Murphy",
    "Watson", "Brooks", "Reed", "Kelly", "Howard", "Cox", "Ward", "Diaz", "Richardson", "Wood",
    "Watkins", "Stone", "West", "Jordan", "Bryant", "Foster", "Hamilton", "Graham", "Sullivan", "Wallace",
    "Woods", "Cole", "Freeman", "Hunter", "Palmer", "Arnold", "Spencer", "Holland", "Webb", "Payne",
    "Barrett", "Day", "Fox", "Dean", "Keller", "Brady", "French", "Higgins", "Hodges", "Nash",
    "Blackwell", "Vega", "Boone", "Conrad", "Maddox", "Vaughn", "Blake", "Carver", "Decker", "Kane",
    "Harmon", "Brock", "Finch", "Rivers", "Dalton", "Whitaker", "Brennan", "Knox", "Parks", "Santos",
    "Silva", "Ferreira", "Almeida", "Pereira", "Costa", "Lima", "Teixeira", "Cardoso", "Rocha", "Moura",
    "Barros", "Franco", "Oliveira", "Souza", "Castro", "Campos", "Dias", "Moreira", "Ramos", "Vieira",
    "Antunes", "Aguiar", "Borges", "Figueira", "Machado", "Azevedo", "Henrique", "Camacho", "Galindo", "Delgado",
    "Roldan", "Escobar", "Medina", "Solano", "Avila", "Rosales", "Benitez", "Correa", "Cortes", "Espinoza",
    "Salazar", "Zamora", "Miranda", "Cuevas", "Ojeda", "Solis", "Arroyo", "Castillo", "Valdez", "Palacios",
    "Alvarez", "Mendoza", "Villanueva", "Ortega", "Ibarra", "Trejo", "Bravo", "Serrano", "Beltran", "Quintero",
    "Urbina", "Montoya", "Delacruz", "Acevedo", "Zavala", "Velasquez", "Pineda", "Pacheco", "Gallegos", "Camacho",
    "Salinas", "Lozano", "Arriaga", "Fuentes", "Arellano", "Espinosa", "Del Toro", "Cisneros", "Del Rio", "Varela",
    "Tovar", "Quiroz", "Marquez", "Solis", "Cuevas", "Delgado", "Cortez", "Valencia", "Rosario", "Santana",
    "De La Cruz", "Padilla", "Herrera", "Barrera", "Olguin", "Vasquez", "Angulo", "Moya", "Sandoval", "Peralta",
    "Quintana", "Trujillo", "Reyes", "Guzman", "Morales", "Ponce", "Ochoa", "Navarro", "Barron", "Lucero",
    "Renteria", "Burgos", "Tamayo", "Carranza", "Villalobos", "Verdugo", "Rico", "Cabrera", "Soto", "Jimenez",
    "Castaneda", "Guerrero", "Cano", "Alarcon", "Cedillo", "Grimaldo", "Escalante", "Madrigal", "Ledesma", "Saucedo",
    "Treviño", "Cedeno", "Betancourt", "Lara", "Cardona", "Baez", "Rosado", "Sanabria", "Villegas", "Alfaro",
    "Quezada", "Olvera", "Giron", "Melendez", "Bautista", "Barrientos", "Tapia", "Gallardo", "Chavez", "Espino",
    "Celis", "Valle", "Lugo", "Mata", "Moreno", "Aceves", "Nieto", "Tamez", "Juarez", "Meraz",
    "Caballero", "Venegas", "Reynoso", "Mojica", "Huerta", "Parra", "Montes", "Godoy", "Leyva", "Iturbe"

]   # ~300
countries = [ "Brazil", "England", "Senegal", "Belgium", "Japan", "Morocco", "Argentina",
    "Croatia", "Egypt", "USA", "France", "Germany", "Spain", "South Korea", "Italy" ]    # dozens
positions = ["GK", "RB", "CB", "LB", "CDM", "CM", "CAM", "RW", "LW", "ST"]
footed = ["Left", "Right", "Both"]
traits = ["Pace Specialist", "Set Piece Specialist", "Dribbler", "Defensive Wall", "Weak Foot", "Injury Prone"]

clubs = [
    "Real Madrid", "Barcelona", "Manchester United", "Manchester City", "Liverpool",
    "Bayern Munich", "Juventus", "Paris Saint-Germain", "Chelsea", "Arsenal",
    "Borussia Dortmund", "AC Milan", "Inter Milan", "Atletico Madrid", "Ajax",
    "Benfica", "Porto", "Tottenham Hotspur", "Roma", "Napoli",
    "Sevilla", "Lyon", "Bayer Leverkusen", "RB Leipzig", "Celtic",
    "Glasgow Rangers", "Galatasaray", "Fenerbahce", "Besiktas", "PSV Eindhoven",
    "Feyenoord", "Sporting CP", "Olympique Marseille", "Monaco", "Valencia",
    "Villarreal", "Atalanta", "Lazio", "ACF Fiorentina", "Inter Miami",
    "LA Galaxy", "Corinthians", "Flamengo", "Santos", "Boca Juniors",
    "River Plate", "Chivas Guadalajara", "Pachuca", "Club America", "Universitario",
    "Ajax Cape Town", "Kaizer Chiefs", "Al Ahly", "Zamalek", "TP Mazembe",
    "Wydad Casablanca", "Espérance de Tunis", "Al Hilal (Saudi)", "Al Nassr",
    "Urawa Reds", "Kashima Antlers", "Shakhtar Donetsk", "Dynamo Kyiv", "Celtic",
    "Rangers", "FC Red Bull Salzburg", "RB Salzburg", "BSC Young Boys",
    "FC Basel", "FC Zürich", "Club Brugge", "Anderlecht", "Genk",
    "PSV Eindhoven", "AZ Alkmaar", "FC Twente", "Vitesse", "Wolfsburg",
    "Schalke 04", "Bayer Leverkusen", "Eintracht Frankfurt", "Borussia M’gladbach",
    "Bayern Leverkusen", "Hertha Berlin", "Tigres UANL", "Cruz Azul", "Pumas UNAM",
    "Atlas", "Monterrey", "Santos Laguna", "Club América"
]  # ~100 club names

def generate_player(
    preferred_country=None,
    preferred_position=None,
    preferred_foot=None,
    preferred_trait=None,
    preferred_club=None,
    age_range=(16, 23),
    overall_range=(50, 75),
    potential_increase=(10, 25)
):
    first = random.choice(first_names)
    last = random.choice(last_names)
    name = f"{first} {last}"

    country = preferred_country if preferred_country else random.choice(countries)
    position = preferred_position if preferred_position else random.choice(positions)
    age = random.randint(*age_range)
    overall = random.randint(*overall_range)
    potential = min(overall + random.randint(*potential_increase), 99)
    club = preferred_club if preferred_club else random.choice(clubs)
    foot = preferred_foot if preferred_foot else random.choice(footed)
    special = preferred_trait if preferred_trait else random.choice(traits)

    player = {
        "Name": name,
        "Country": country,
        "Position": position,
        "Age": age,
        "Overall": overall,
        "Potential": potential,
        "Club": club,
        "Footed": foot,
        "Trait": special
    }
    return player

    return player

# Function to generate many players and export to CSV
def generate_players(n=10, **kwargs):
    players = []
    for _ in range(n):
        p = generate_player(**kwargs)
        players.append(p)
    return players

def export_to_csv(players, filename="players.csv"):
    if not players:
        return
    keys = players[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(players)

# Optional: Web app using Streamlit
def streamlit_app():
    st.title("FC‑like Career Mode Player Generator")

    country = st.selectbox("Preferred Country", ["Any"] + countries)
    position = st.selectbox("Preferred Position", ["Any"] + positions)
    age_min, age_max = st.slider("Age range", 16, 35, (16, 23))
    overall_min, overall_max = st.slider("Overall rating range", 50, 90, (60, 75))
    generate_n = st.number_input("How many players to generate", min_value=1, max_value=100, value=5)

    if st.button("Generate Players"):
        result = generate_players(
            preferred_country=(None if country == "Any" else country),
            preferred_position=(None if position == "Any" else position),
            age_range=(age_min, age_max),
            overall_range=(overall_min, overall_max)
        )
        for p in result:
            st.write(p)
        # offer CSV download
        csv_str = "Name,Country,Position,Age,Overall,Potential,Club,Footed,Trait\n"
        for p in result:
            csv_str += f"{p['Name']},{p['Country']},{p['Position']},{p['Age']},{p['Overall']},{p['Potential']},{p['Club']},{p['Footed']},{p['Trait']}\n"
        st.download_button("Download CSV", csv_str, "players.csv", mime="text/csv")


def streamlit_app():
    st.set_page_config(page_title="FC Career Player Generator", layout="centered")
    st.title("⚽ FC26 Career Mode Player or Manager Career Mode Name Generator")

    st.markdown("Generate fictional football players for your custom Career Mode save!")

    # --- Filters ---
    col1, col2 = st.columns(2)

    with col1:
        country = st.selectbox("🌍 Preferred Country", ["Any"] + countries)
        position = st.selectbox("📌 Preferred Position", ["Any"] + positions)
        foot_filter = st.selectbox("🦶 Preferred Foot", ["Any"] + footed)

    with col2:
        age_min, age_max = st.slider("🎂 Age Range", 16, 35, (16, 23))
        overall_min, overall_max = st.slider("⭐ Overall Rating", 50, 90, (60, 75))
        club_filter = st.selectbox("🏟️ Preferred Club", ["Any"] + clubs)

    trait_filter = st.selectbox("🎯 Preferred Trait", ["Any"] + traits)

    generate_n = st.slider("🔢 Number of Players", 1, 50, 5)

    if st.button("🎲 Generate Players"):
        # Generate players based on filter settings
        result = generate_players(
            n=generate_n,
            preferred_country=None if country == "Any" else country,
            preferred_position=None if position == "Any" else position,
            preferred_foot=None if foot_filter == "Any" else foot_filter,
            preferred_trait=None if trait_filter == "Any" else trait_filter,
            preferred_club=None if club_filter == "Any" else club_filter,
            age_range=(age_min, age_max),
            overall_range=(overall_min, overall_max)
        )

        df = pd.DataFrame(result)

        st.success(f"✅ Generated {len(df)} players")
        st.dataframe(df, use_container_width=True)

        # Download CSV
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="⬇️ Download CSV",
            data=csv,
            file_name="career_mode_players.csv",
            mime="text/csv"
        )
if __name__ == "__main__":
    streamlit_app()
