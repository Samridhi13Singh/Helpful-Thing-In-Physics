import streamlit as st
import G,g,c

def calculate_gravitational_force(mass1,mass2,r):
    return (G*mass1*mass2)/(r**2)

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def calculate_nuclear_energy(mass):
    return mass * c ** 2

def calculate_pressure(density, depth):
    return density * g * depth

st.title("Simple Physics Calculator")

st.header("1. Gravitational Force")
mass1 = st.number_input("Enter mass (kg)", value=1.0)
mass2 = st.number_input("Enter mass (KG)", value=1.0)
distance=st.number_input("Enter a distance ",value=1.0)
if st.button("Calculate Gravitational Force"):
    force = calculate_gravitational_force(mass1,mass2,distance)
    st.write(f"Gravitational Force: {force} N")

st.header("2. Kinetic Energy")
mass_ke = st.number_input("Enter mass (kg)", value=1.0, key="mass_ke")
velocity = st.number_input("Enter velocity (m/s)", value=1.0)
if st.button("Calculate Kinetic Energy"):
    ke = calculate_kinetic_energy(mass_ke, velocity)
    st.write(f"Kinetic Energy: {ke} J")

st.header("3. Nuclear Energy")
mass_c=st.number_input("Enter mass (Kg)",value=1.0)
if st.button("Calculate Nuclear Energy"):
    mx=calculate_nuclear_energy(mass_c)
    st.write(f"Nuclear Energy: {mx}")

st.header("4.Pressure")
depth=st.number_input("Enter a depth (m)", value=1.0)
density=st.number_input("Enter a density ",value=1)
if st.button("Calculate Pressure"):
    pa=calculate_pressure(density,depth)
    st.write(f"Pressure: {pa}  Pa")

