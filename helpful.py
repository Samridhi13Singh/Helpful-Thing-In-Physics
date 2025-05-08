import streamlit as st
from scipy.constants import g, c

def calculate_gravitational_force(mass):
    return mass * g

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def calculate_nuclear_energy(mass):
    return mass * c ** 2

def calculate_pressure(density, depth):
    return density * g * depth

st.title("Simple Physics Calculator")

st.header("1. Gravitational Force")
mass_g = st.number_input("Enter mass (kg)", value=1.0)
if st.button("Calculate Gravitational Force"):
    force = calculate_gravitational_force(mass_g)
    st.write(f"Gravitational Force: {force:.2f} N")

st.header("2. Kinetic Energy")
mass_ke = st.number_input("Enter mass (kg)", value=1.0, key="mass_ke")
velocity = st.number_input("Enter velocity (m/s)", value=1.0)
if st.button("Calculate Kinetic Energy"):
    ke = calculate_kinetic_energy(mass_ke, velocity)
    st.write(f"Kinetic Energy: {ke:.2f} J")


st.header("3. Nuclear Energy")
mass_ne = st.number_input("Enter mass (kg)", value=1.0, key="mass_ne")
if st.button("Calculate Nuclear Energy"):
    nuclear_energy = calculate_nuclear_energy(mass_ne)
    st.write(f"Nuclear Energy: {nuclear_energy:.2f} J")


st.header("4. Pressure")
density = st.number_input("Enter density (kg/m³)", value=1025)
depth = st.number_input("Enter depth (m)", value=1.0)
if st.button("Calculate Pressure"):
    pressure = calculate_pressure(density, depth)
    st.write(f"Pressure: {pressure:.2f} Pa")
