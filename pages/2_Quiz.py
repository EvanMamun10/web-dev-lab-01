import streamlit as st

st.title("Welcome to the career Quiz!")
st.write("Answer these 5 questions to find your perfect job")

st.subheader("1. Rate how much you value money on a scale of 1-10")
st.image("Images/Money].jpg", width=300)
q1 = st.number_input("Enter a number", min_value=0, max_value=10, value=5) #NEW

st.subheader("2. What is your favorite subject in school?")
st.image("Images/school.jpg", width=300)
q2 = st.radio("Choose one:", ["Math", "Science", "History", "English"]) #NEW

st.subheader("3. Describe specific traits you have!")
st.image("Images/profile.jpeg", width=200)
traits = st.multiselect("Select traits:", ["Funny", "Smart", "Brave"]) #NEW

st.subheader("4. How much do you value work life balance?")
q4 = st.number_input("Enter a number for balance", min_value=0, max_value=10, value=5)

st.subheader("5. What City would you most feel you would enjoy?")
st.image("Images/city.jpeg", width=300)
q5 = st.radio("Choose one city:", ["New York City", "Miami", "San Francisco", "Omaha"]) 

st.write("---")

if st.button("Find my Career"):
    if q2 == "Math" and q5 == "New York City" and q1 >= 8:
        st.header("Result: Wall Street Quant")
        st.write("You love numbers and the fast-paced city life.")
        st.balloons() #NEW
    elif q2 == "Science" or "Smart" in traits:
        st.header("Result: Research Scientist")
        st.write("Your brain is your best tool. You belong in a lab!")
        st.balloons()
    elif q5 == "Omaha":
        st.header("Result: Modern Farmer")
        st.write("Omaha is calling! You belong out in the open fields.")
        st.balloons()
    elif q5 == "Miami" or "Funny" in traits:
        st.header("Result: Entertainment Host")
        st.write("You have the energy and the personality for the big stage!")
        st.balloons()
    elif q2 == "English" or q2 == "History":
        st.header("Result: Journalist")
        st.write("You have a way with words and a curiosity for the world.")
        st.balloons()
    elif q1 >= 7:
        st.header("Result: Corporate Executive")
        st.write("You have your eyes on the prize. Success is in your future.")
        st.balloons()
    elif "Brave" in traits or q4 <= 3:
        st.header("Result: Emergency Responder")
        st.write("You handle pressure well and put others first.")
        st.balloons()
    else:
        st.header("Result: You are an Enigma!")
        st.write("Your tastes are too unique for a standard job. Find your own path!")
